from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, RiseInTransition
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup

from View.Wellcome import Funtions as Wellcome
from View.Menu import Funtions as Menu
from View.Reading import Funtions as Reading
from View.Classification import Funtions as Classification
from View.Result import Funtions as Result

import numpy as np
import matplotlib.pyplot as plt
from pypercorn.algorithms.images.segmentation import Segmentation

# Initialize the API
segmentation = Segmentation()

class MDTextFieldPassword(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class MDTextFieldUser(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class MDRoundButtonLayout(MDRelativeLayout):
    pass


class HyperApp(MDApp):
    def build(self):
        Builder.load_file("View/Wellcome/Design.kv")
        Builder.load_file("View/Menu/Design.kv")
        Builder.load_file("View/Reading/Design.kv")
        Builder.load_file("View/Classification/Design.kv")
        Builder.load_file("View/Result/Design.kv")
        SM = ScreenManager(transition=RiseInTransition())
        SM.add_widget(Wellcome.Wellcome(name="Wellcome"))
        SM.add_widget(Menu.Menu(name="Menu"))
        SM.add_widget(Reading.Reading(name="Reading"))
        SM.add_widget(Classification.Classification(name="Classification"))
        SM.add_widget(Result.Result(name="Result"))
        self.theme_cls.theme_style = "Dark"
        return SM


    def change_screen(self, screen_name):
        self.root.current = screen_name
        self.root.transition = RiseInTransition()


    def logger(self):
        wellcome_screen = self.root.get_screen('Wellcome')
        user = wellcome_screen.ids.user.text
        password = wellcome_screen.ids.password.text
        if user == "admin" and password == "1234":
            self.change_screen('Menu')
            wellcome_screen.ids.user.text = ""
            wellcome_screen.ids.password.text = ""
        else:
            self.show_error_dialog()


    def show_error_dialog(self):
        self.dialog = MDDialog(
            type="custom",
            content_cls=MDBoxLayout(
                Label(
                    text="Usuario o contraseña incorrecta",
                    halign="center",
                    color=(1, 1, 1, 1),
                    font_size="20sp",
                ),
                orientation="vertical",
                padding="20dp",
                spacing="10dp",
            ),
            buttons=[
                MDFlatButton(
                    text="OK",
                    font_size="20sp", 
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_dialog
                ),
            ],
        )
        self.dialog.open()


    def close_dialog(self, instance):
        self.dialog.dismiss()
        wellcome_screen = self.root.get_screen('Wellcome')
        wellcome_screen.ids.user.text = ""
        wellcome_screen.ids.password.text = ""


    def open_file_chooser(self):
        self.file_chooser = FileChooserIconView(filters=["*.tif", "*.tiff"])
        self.popup = Popup(title="Seleccionar Imagen", content=self.file_chooser, size_hint=(0.9, 0.9))
        self.file_chooser.bind(selection=self.update_image)
        self.popup.open()


    def update_image(self, instance, value):
        if value:
            selected_image_path = value[0]
            reading_screen = self.root.get_screen('Reading')
            image_box = reading_screen.ids.image_box
            image_box.clear_widgets()
            image_box.add_widget(
                Image(
                    source=selected_image_path,
                    size_hint=(1, 1),  # Ajustar la imagen al tamaño del box
                    allow_stretch=True,  # Permitir que la imagen se estire para llenar el espacio
                )
            )
            estado_label = reading_screen.ids.estado
            estado_label.text = "CULTIVO ENFERMO"
            self.popup.dismiss()
            print(selected_image_path)
            ruta_invertida = selected_image_path
            self.ruta_normal = ruta_invertida.replace("\\", "/")
            print(self.ruta_normal)


    def segment_image(self):
        if hasattr(self, 'ruta_normal') and self.ruta_normal:

            image_array = plt.imread(self.ruta_normal)
            segmented_image_kmeans_dict = segmentation.kmeans(image_array)
            segmented_image_kmeans  = segmented_image_kmeans_dict.pop("image")
            plt.imshow(segmented_image_kmeans, cmap='RdYlGn', interpolation='bicubic')
            plt.axis("off")
            plt.savefig("segmented_image.png", bbox_inches='tight', pad_inches=0)
            plt.close()
            classification_screen = self.root.get_screen('Classification')
            segment_box = classification_screen.ids.segment_box
            segment_box.clear_widgets()
            segment_box.add_widget(
                Image(
                    source="segmented_image.png",
                    size_hint=(1, 1),  # Ajustar la imagen al tamaño del box
                    allow_stretch=True,  # Permitir que la imagen se estire para llenar el espacio
                )
            )
            self.change_screen('Classification')
        else:
            self.dialog = MDDialog(
                type="custom",
                content_cls=MDBoxLayout(
                    Label(
                        text="Cargue una imagen",
                        halign="center",
                        color=(1, 1, 1, 1),
                        font_size="20sp",
                    ),
                    orientation="vertical",
                    padding="20dp",
                    spacing="10dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="OK",
                        font_size="20sp", 
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    ),
                ],
            )
            self.dialog.open()


    def cargar_otra_imagen(self):
        self.ruta_normal = ""
        reading_screen = self.root.get_screen('Reading')
        estado_label = reading_screen.ids.estado
        estado_label.text = ""
        image_box = reading_screen.ids.image_box
        image_box.clear_widgets()
        image_box.add_widget(
                Label(
                    text = "Aquí se mostrará tu imagen",
                    halign = "center",
                    color = (0, 0, 0, 1),  # Color negro
                    font_size="15sp",
                    bold = True
                )       
            )
        reading_screen = self.root.get_screen('Classification')
        segment_box = reading_screen.ids.segment_box
        segment_box.clear_widgets()
        segment_box.add_widget(
                Label(
                    text = "Aquí se mostrará tu imagen K-MEANS",
                    halign = "center",
                    color = (0, 0, 0, 1),  # Color negro
                    font_size="15sp",
                    bold = True
                )       
            )
        self.change_screen('Reading')

HyperApp().run()
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout

class MDRoundButtonLayout(MDRelativeLayout):
    pass

class Menu(Screen):
    def go_back(self):
        self.manager.current = 'Wellcome'  # Cambia a la pantalla de bienvenida (Welcome)
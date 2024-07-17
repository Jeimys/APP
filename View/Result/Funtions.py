from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout


class MDRoundButtonLayout(MDRelativeLayout):
    pass

class Result(Screen):
    def go_back(self):
        self.manager.current = 'Classification'  # Cambia a la pantalla de atrás

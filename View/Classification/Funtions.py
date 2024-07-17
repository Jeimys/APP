from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineListItem
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton


class MDRoundButtonLayout(MDRelativeLayout):
    pass

class Classification(Screen):
    def go_back(self):
        self.manager.current = 'Reading'  # Cambia a la pantalla de atrás

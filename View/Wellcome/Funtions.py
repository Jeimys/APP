from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout

class MDTextFieldPassword(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    id = StringProperty()

class MDTextFieldUser(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    id = StringProperty()

class MDRoundButtonLayout(MDRelativeLayout):
    pass

class Wellcome(Screen):
    pass
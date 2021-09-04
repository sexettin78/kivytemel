#pip install kivy
from typing import Text
from kivy.app import App
from kivy.uix.label import Label
class program(App):
    def on_start(self):
        self.title = "yeşil kivi"
    def build(self):
        return Label(text = "Mayk taysın ")

program().run()
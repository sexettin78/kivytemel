#pip install kivy
from typing import Text
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
class program(App):
    def on_start(self):
        self.title = "kovi"

    def on_resume(self):
        return Label(text = "Naber kanka")
        
program().run()
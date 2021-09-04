#pip install kivy
from kivy.app import App
from kivy.uix.label import Label
class program(App):
    def build(self):
        yazi = Label(text = "Merhaba ")
        return yazi

program().run()
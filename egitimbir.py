from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class uygulama(App):
    def build(self):
        #vertical yukarıdan aşağı olur tuşlar,horizontal yaparsan yatay
        temellayout = BoxLayout(orientation='vertical')
        ustlayout = BoxLayout()
        altlayout = BoxLayout()


        username = Label(text = "Username")
        password = Label(text = "Password")

        username_input = TextInput()
        password_input = TextInput()


        button = Button(text = "login")

        ustlayout.add_widget(username)
        ustlayout.add_widget(username_input)


        altlayout.add_widget(password)
        altlayout.add_widget(password_input)

        temellayout.add_widget(ustlayout)
        temellayout.add_widget(altlayout)
        temellayout.add_widget(button)


        return temellayout


uygulama().run()
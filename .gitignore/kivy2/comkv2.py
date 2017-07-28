from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class Widgets(Widget):
    pass

class SimplesKivyTApp(App):
    def build(self):
        return Widgets()

if __name__ == '__main__':
    SimplesKivyTApp().run()

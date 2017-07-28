from kivy.app import App
from kivy.uix.label import Label

class SimplesKivyApp(App):
    def build(self):
        return Label()

if __name__ == '__main__':
    SimplesKivyApp().run()
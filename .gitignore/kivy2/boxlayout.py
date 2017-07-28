import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image

class Imagem(Image):
    pass

class GridApp(App):
    def build(self):
        return Imagem(source='WIN_20170529_18_43_11_Pro (2).jpg', pos=(-175,0), size=(50,50))


myapp = GridApp()
myapp.run()

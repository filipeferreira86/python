import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class RpnCalculatorForm(BoxLayout):
    def __init__(self, **kwargs):
        super(RpnCalculatorForm, self).__init__(**kwargs)
        self.desloquePilha = 1
        registrador_x = ObjectProperty(None)
        registrador_y = ObjectProperty(None)
        registrador_z = ObjectProperty(None)
        registrador_t = ObjectProperty(None)

    def entradigito(self, valor):
        if (self.desloquePilha==1):
            self.processa_enter()
        else:
            self.desloquePilha=0

        valorAnterior = int(self.registrador_x.text)
        self.registrador_x.text = str(valor + 10 * valorAnterior)

    def processa_enter(self):
        print('Reiniciando processa_enter')
        valorz = self.registrador_z.text
        print('Var valorz: ', valorz)
        self.registrador_t.text=valorz
        valory = self.registrador_y.text
        print('Var valory: ', valory)
        self.registrador_z.text=valory
        valorx = self.registrador_x.text
        print('Var valorz: ', valorx)
        self.registrador_y.text=valorx
        self.registrador_x.text="0"
        print('-'*50)
        self.desloquePilha=0


    def processaDivide(self):
        valorx = float(self.registrador_x.text)
        valory = float(self.registrador_y.text)
        self.registrador_x.text = str(valorx/valory)
        self.registrador_y.text = self.registrador_z.text
        self.registrador_z.text = self.registrador_t.text
        self.desloquePilha = 1


    def processaVezes(self):
        valorx = int(self.registrador_x.text)
        valory = int(self.registrador_y.text)
        self.registrador_x.text = str(valorx*valory)
        self.registrador_y.text = self.regitrador_z.text
        self.registrador_z.text = self.registrador_t.text
        self.desloquePilha = 1


    def processa_mais(self):
        print('Inicia o processo mais')
        valorx = int(self.registrador_x.text)
        valory = int(self.registrador_y.text)
        self.registrador_x.text = str(valorx+valory)
        self.registrador_y.text = self.registrador_z.text
        self.registrador_z.text = self.registrador_t.text
        self.desloquePilha = 1


    def processa_Menos(self):
        valorx = int(self.registrador_x.text)
        valory = int(self.registrador_y.text)
        self.registrador_x.text = str(valorx-valory)
        self.registrador_y.text = self.registrador_z.text
        self.registrador_z.text = self.registrador_t.text
        self.desloquePilha = 1


class RpnApp(App):
    pass

if __name__=='__main__':
    RpnApp().run()

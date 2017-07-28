from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class TelaLogin(GridLayout):
    def __init__(self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Login:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Senha:"))
        self.senha = TextInput(multiline=False, password=True)
        self.add_widget(self.senha)


class Exemplo1(App):
    def build(self):
        return TelaLogin()

if __name__ == '__main__':
    Exemplo1().run()

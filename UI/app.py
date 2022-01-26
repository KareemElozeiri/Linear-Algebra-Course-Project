import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from MainPage import MainPage


class MyApp(App):
    def __init__(self,**kwargs):
        super(MyApp,self).__init__(**kwargs)

    def build(self):
        return MainPage()


if __name__ == "__main__":

    app = MyApp()
    app.run()


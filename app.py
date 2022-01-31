import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from kivy.uix.screenmanager import ScreenManager, Screen 
from UI.main_page import MainPage
from UI.processing_page import ProcessingPage 
import cv2 

class MyApp(App):
    def __init__(self,**kwargs):
        super(MyApp,self).__init__(**kwargs)
        self.title = "Matrix Effects"

    def build(self):
        self.screen_manager = ScreenManager()
        self.main_page = MainPage(self)
        self.processing_page = None

        screen = Screen(name="main")
        screen.add_widget(self.main_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    app = MyApp()
    app.run()


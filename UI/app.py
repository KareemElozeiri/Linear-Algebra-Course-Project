import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from main_page import MainPage
from processing_page import ProcessingPage 

import cv2 


class MyApp(App):
    def __init__(self,**kwargs):
        super(MyApp,self).__init__(**kwargs)
        self.title = "Matrix Effects"

    def build(self):
        return MainPage()
        #return ProcessingPage(cv2.imread("Ggstokes.jpg"))  


if __name__ == "__main__":

    app = MyApp()
    app.run()


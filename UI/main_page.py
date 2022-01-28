import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen 
from processing_page import ProcessingPage 
import cv2 
import numpy as np 

class MainPage(GridLayout):
    def __init__(self,app,**kwargs):
        super(MainPage,self).__init__(**kwargs)
        
        self.app = app 
        
        self.cols = 1
        self.padding = 50
        self.spacing  = 10
        self.add_widget(Label(text="Welcome to Matrix Effect!"))

        self.load_img_btn = Button(text="Load An Image")
        self.load_img_btn.on_press = self.load_img 
        self.add_widget(self.load_img_btn)

        self.capture_img_btn = Button(text="Capture An Image")
        self.capture_img_btn.on_press = self.capture_img
        self.add_widget(self.capture_img_btn)

        self.status_bar = Label()
        self.status_bar.height = 30
        self.add_widget(self.status_bar)
    

    def switch_to_processing(self,_):
        self.app.screen_manager.current = "processing page"

    def empty_status_bar(self,*_):
        self.status_bar.text = ""

    def load_img(self):
        self.app.processing_page = ProcessingPage(self.app,cv2.imread("img.jpg"))
        screen = Screen(name="processing page")
        screen.add_widget(self.app.processing_page)
        self.app.screen_manager.add_widget(screen)
        self.status_bar.text = "loading an image"      
        Clock.schedule_once(self.empty_status_bar,1)
        Clock.schedule_once(self.switch_to_processing,1)
    
    def capture_img(self):
        self.status_bar.text = "capturing an image"      
        Clock.schedule_once(self.empty_status_bar,1) 


        
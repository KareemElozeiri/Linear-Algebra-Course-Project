import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen 
from UI.processing_page import ProcessingPage 
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
    
    #removes the content of the status bar of the main page
    def empty_status_bar(self,*_):
        self.status_bar.text = ""
          
    #function for loading image that is going to be processed 
    def load_img(self):
        # self.app.create_processing_page(cv2.imread("C:\\Kareem El-ozeiri\\Linear-Algebra-Course-Project\\UI\\img.jpg"))
        self.status_bar.text = "Opening load page.."      
        Clock.schedule_once(self.empty_status_bar,1)
        Clock.schedule_once(self.app.switch_to_load,1)

    #function for capturing the image that is going to be processed by the web cam of the computer 
    def capture_img(self):
        self.status_bar.text = "Switching to camera.."      
        Clock.schedule_once(self.empty_status_bar,1) 
        Clock.schedule_once(self.app.switch_to_camera,1)

import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from kivy.uix.image import Image 
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.uix.textinput import TextInput 
import cv2 
import numpy as np 

class ProcessingPage(GridLayout):

    def __init__(self,app,img,**kwargs):
        super(ProcessingPage,self).__init__(**kwargs)
        
        self.app = app
        
        self.img = img
        self.img_texture = ""
        self.convert_to_texture()
        
        self.cols = 3
        self.orientation = "lr-tb"
        
        self.main_scene = Image(texture = self.img_texture)
        self.add_widget(self.main_scene)

        self.side_bar = SideBar()
        self.side_bar.size_hint_x = None 
        self.side_bar.width = 200
        self.add_widget(self.side_bar)

    def convert_to_texture(self,colorfmt="bgr"):
        buf0 = cv2.flip(self.img,0)
        buf1 =  buf0.tostring() 
        self.img_texture = Texture.create(size=(self.img.shape[1],self.img.shape[0]),colorfmt=colorfmt)
        self.img_texture.blit_buffer(buf1, colorfmt=colorfmt, bufferfmt='ubyte')
        return self.img_texture


class SideBar(GridLayout):
    
    def __init__(self,**kwargs):
        super(SideBar,self).__init__(**kwargs)
        self.cols = 1
        self.common_height = 50

        self.gauss_blur_sec = GaussBlurSec()
        self.add_widget(self.gauss_blur_sec)

        self.save_subgrid = GridLayout(cols=2,size_hint_y=None,height=self.common_height)

        self.save_textinput = TextInput()
        
        self.save_btn = Button(text="Save",size_hint_x=None,width=50)
        self.save_btn.on_press = self.save_action

        self.save_subgrid.add_widget(self.save_textinput)
        self.save_subgrid.add_widget(self.save_btn)
        self.add_widget(self.save_subgrid)

        self.status_bar = Label(text="",size_hint_y=None,height=self.common_height)
        self.add_widget(self.status_bar)

    def empty_status_bar(self,_):
        self.status_bar.text = ""  

    def save_action(self):
        self.status_bar.text = "saving frame..."
        Clock.schedule_once(self.empty_status_bar,1)



class GaussBlurSec(GridLayout):
    def __init__(self,**kwargs):
        super(GaussBlurSec,self).__init__(**kwargs)
        self.cols = 1
        self.common_height = 50
        self.label = Label(text="Guassian Blur",size_hint_y=None,height=self.common_height/2)
        self.add_widget(self.label)

        self.subGrid0 = GridLayout(size_hint_y=None,height=self.common_height)
        self.subGrid0.cols = 2
        self.kernel_size_label = Label(text="Kernel size:")
        self.kernel_size_textinput = TextInput(multiline=False)

        self.subGrid0.add_widget(self.kernel_size_label)
        self.subGrid0.add_widget(self.kernel_size_textinput)

        self.add_widget(self.subGrid0)

        self.apply_btn = Button(text="Apply Gauss",size_hint_y=None,height=self.common_height)
        self.add_widget(self.apply_btn)
    
    
import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from kivy.uix.image import Image 
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.uix.textinput import TextInput


class SideBar(GridLayout):
    
    def __init__(self,master,**kwargs):
        super(SideBar,self).__init__(**kwargs)
        self.cols = 1
        self.common_height = 50
        self.master = master 
        
        #gaussian blur section
        self.gauss_label = Label(text="Guassian Blur")
        self.gauss_kernel_label = Label(text="Kernel Size: ")
        self.gauss_kernel_textinput = TextInput()
        self.gauss_btn = Button(text="Apply Guassian Blur")
        gauss_elements = {"main_label":self.gauss_label,"kernel_label":self.gauss_kernel_label,"kernel_textinput":self.gauss_kernel_textinput,"apply_btn":self.gauss_btn}
        self.gauss_toolbox = EffectToolBox(gauss_elements)
        self.add_widget(self.gauss_toolbox)
        #median blur section 
        self.median_label = Label(text="Median Blur")
        self.median_kernel_label = Label(text="Kernel Size: ")
        self.median_kernel_textinput = TextInput()
        self.median_btn = Button(text="Apply Median Blur")
        median_elements = {"main_label":self.median_label,"kernel_label":self.median_kernel_label,"kernel_textinput":self.median_kernel_textinput,"apply_btn":self.median_btn}
        self.median_toolbox = EffectToolBox(median_elements)
        self.add_widget(self.median_toolbox)
        
        #save section 
        self.save_subgrid = GridLayout(cols=2,size_hint_y=None,height=self.common_height)
        self.save_textinput = TextInput()
        self.save_btn = Button(text="Save",size_hint_x=None,width=50)
        self.save_btn.on_press = self.save_action
        self.save_subgrid.add_widget(self.save_textinput)
        self.save_subgrid.add_widget(self.save_btn)
        self.add_widget(self.save_subgrid)
    
        #status bar section 
        self.status_bar = Label(text="",size_hint_y=None,height=self.common_height)
        self.add_widget(self.status_bar)

    #removes the content of the status bar of the processing page 
    def empty_status_bar(self,_):
        self.status_bar.text = ""  

    #saves the image after the user has applied the effects on it
    def save_action(self):
        self.status_bar.text = "saving frame..."
        Clock.schedule_once(self.empty_status_bar,1)
        Clock.schedule_once(self.master.app.switch_to_save)
      
class EffectToolBox(GridLayout):
    def __init__(self,elements,**kwargs):
        super(EffectToolBox,self).__init__(**kwargs)
        self.cols = 1
        self.common_height = 50
        elements["main_label"].size_hint_y=None
        elements["main_label"].height=self.common_height/2
        self.add_widget(elements["main_label"])
        
        self.subGrid0 = GridLayout(size_hint_y=None,height=self.common_height)
        self.subGrid0.cols = 2

        self.subGrid0.add_widget(elements["kernel_label"])
        self.subGrid0.add_widget(elements["kernel_textinput"])

        self.add_widget(self.subGrid0)
        elements["apply_btn"].size_hint_y = None 
        elements["apply_btn"].height = self.common_height/2
        self.add_widget(elements["apply_btn"])


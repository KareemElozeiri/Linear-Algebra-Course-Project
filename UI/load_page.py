import kivy
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 
from kivy.uix.filechooser import FileChooserListView 
from kivy.uix.label import Label 
from kivy.clock import Clock
from PIL import Image 
import cv2 

class LoadPage(GridLayout):
    def __init__(self,app,**kwargs):
        super(LoadPage,self).__init__(**kwargs)
        self.app = app 
        self.cols = 1
        
        #file chooser
        self.file_chooser = FileChooserListView()
        self.add_widget(self.file_chooser)
        #load button 
        self.load_btn = Button(text="Load",size_hint_y=None,height=50)
        self.load_btn.on_press = self.load_action
        self.add_widget(self.load_btn)
        #status bar
        self.status_bar = Label(size_hint_y=None,height=50)
        self.add_widget(self.status_bar)
    
    def empty_status_bar(self,_):
        self.status_bar.text = ""
    '''
    checks that the file to be loaded is an image 
    reads the image if so and sets it to the app.img properity
    '''
    def load_action(self):
        if(len(self.file_chooser.selection)!=0):
            try:
                Image.open(self.file_chooser.selection[0])
                self.app.img = cv2.imread(self.file_chooser.selection[0])
                self.app.create_processing_page()
                self.status_bar.text = "Image loaded ! Switching to processing page.."

                Clock.schedule_once(self.empty_status_bar,1) 
                Clock.schedule_once(self.app.switch_to_processing,1) 
            
            except IOError:
                self.status_bar.text = "File chosen is not an image"
                Clock.schedule_once(self.empty_status_bar,2) 
           
        else:
            self.status_bar.text = "No file is chosen to load !"
            Clock.schedule_once(self.empty_status_bar,1) 

       

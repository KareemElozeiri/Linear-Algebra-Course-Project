import kivy
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 
from kivy.uix.filechooser import FileChooserIconView 


class LoadPage(GridLayout):
    def __init__(self,app,**kwargs):
        super(LoadPage,self).__init__(**kwargs)
        self.cols = 1
        
        #file chooser
        self.file_chooser = FileChooserIconView()
        self.add_widget(self.file_chooser)
        #load button 
        self.load_btn = Button(text="Load",size_hint_y=None,height=50)
        self.add_widget(self.load_btn)
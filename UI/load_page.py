import kivy
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 
from kivy.uix.filechooser import FileChooserListView 
from kivy.uix.label import Label 


class LoadPage(GridLayout):
    def __init__(self,app,**kwargs):
        super(LoadPage,self).__init__(**kwargs)
        self.cols = 1
        
        #file chooser
        self.file_chooser = FileChooserListView()
        self.add_widget(self.file_chooser)
        #load button 
        self.load_btn = Button(text="Load",size_hint_y=None,height=50)
        self.add_widget(self.load_btn)
        #status bar
        self.status_bar = Label(size_hint_y=None,height=50)
        self.add_widget(self.status_bar)
    
    def empty_status_bar(self,_):
        self.status_bar.text = ""

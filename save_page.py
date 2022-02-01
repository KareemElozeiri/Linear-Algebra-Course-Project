import kivy
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 
from kivy.uix.filechooser import FileChooserIconView 
from kivy.uix.textinput import TextInput

class SavePage(GridLayout):
    def __init__(self,app,**kwargs):
        super(SavePage,self).__init__(**kwargs)
        self.cols = 1
        
        #file chooser
        self.file_chooser = FileChooserIconView()
        self.add_widget(self.file_chooser)
        #save textinput (takes in the name to save by)
        self.save_text_input = TextInput()
        #save button 
        self.save_btn = Button(text="save")
        
        save_section = GridLayout(cols=2,size_hint_y=None,height=50)
        save_section.add_widget(self.save_text_input)
        save_section.add_widget(self.save_btn)
        self.add_widget(save_section)

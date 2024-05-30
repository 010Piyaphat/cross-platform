from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty,StringProperty
from kivy.lang import Builder
from kivy.core.window import Window
import os

_file_path=os.path.dirname(os.path.abspath(__file__))
Builder.load_file(os.path.join(_file_path,'ui6.kv'))

class UI6Screen(Screen):
    obj=ObjectProperty(None)
    _file_path=StringProperty(_file_path)
    def on_enter(self):
        Window.softinput_mode='below_target'
    def on_leave(self):
        Window.softinput_mode=''



class  MyLogIn(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return UI6Screen(obj=self)

if __name__=='__main__':
    MyLogIn().run() 


#####№################
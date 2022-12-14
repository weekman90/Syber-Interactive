from kivy.app import App
from kivy.config import Config
Config.set('graphics','resizable',0)
Config.set('graphics','height',500)
Config.set('graphics','width',400)

from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from kivy.uix.widget import Widget



class gl (App):



    def add_operation(self,instance):
        if( str(instance.text).lower()=='x'):
            self.formula += '*'
        else:
            self.formula += str (instance.text)
        self.update_label()

    def add_number (self,instance):
        if (self.formula=='0'):
            self.formula=''
        self.formula += str(instance.text)
        self.update_label()
    def update_label(self):
        self.lbl.text=self.formula


    def calc_result(self, instance):
        self.lbl.text=str(eval(self.lbl.text))
        self.formula ="0"
    def build (self):
        self.formula = '0'
        bl=BoxLayout(orientation='vertical',padding=20,)



        gl=GridLayout(cols=4,spacing=3,size_hint=(1,.6))
        self.lbl=Label(text='01234', halign='right',valign='center',font_size=40,size_hint=(1,.4),text_size=(400-50,500*.4-20))
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='7',on_press=self.add_number))
        gl.add_widget(Button(text='8',on_press=self.add_number))
        gl.add_widget(Button(text='9',on_press=self.add_number))
        gl.add_widget(Button(text='X',on_press=self.add_operation))

        gl.add_widget(Button(text='4',on_press=self.add_number))
        gl.add_widget(Button(text='5',on_press=self.add_number))
        gl.add_widget(Button(text='6',on_press=self.add_number))
        gl.add_widget(Button(text='-',on_press=self.add_operation))

        gl.add_widget(Button(text='1',on_press=self.add_number))
        gl.add_widget(Button(text='2',on_press=self.add_number))
        gl.add_widget(Button(text='3',on_press=self.add_number))
        gl.add_widget(Button(text='+',on_press=self.add_operation))

        gl.add_widget(Widget())
        gl.add_widget(Button(text='0',on_press=self.add_number))
        gl.add_widget(Button(text='.',on_press=self.add_number))
        gl.add_widget(Button(text='=',on_press=self.calc_result))
        bl.add_widget(gl)
        return bl

if __name__=='__main__':
    gl().run()




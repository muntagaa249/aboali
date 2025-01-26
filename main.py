from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
Builder.load_file('main.kv')
class CustomWidget(Widget):
    def __init__(self, **kwargs):
        super(CustomWidget,self).__init__(**kwargs)

class MainApp(App):
    def build(self):
        return CustomWidget()
    
if __name__ == '__main__':
    MainApp().run()

        
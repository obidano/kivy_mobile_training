from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

Window.size = (350, 600)

class WindowManager(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        manager = WindowManager()
        return manager
        # return Builder.load_file('main.kv')

app = MainApp()
app.run()
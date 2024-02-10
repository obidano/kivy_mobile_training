# from kivy.core.window import Window
# from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp

Window.size = (350, 600)

class WindowManager(ScreenManager):
    def route_initial(self):
        self.transition = NoTransition()
        self.current = "etudiants"

class MainApp(MDApp):
    def build(self):
        manager = WindowManager()
        manager.route_initial()
        return manager
        # return Builder.load_file('main.kv')

app = MainApp()
app.run()
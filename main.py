# from kivy.core.window import Window
from kivy import Config
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp

Config.set('kivy', 'exit_on_escape', '0')

# Window.size = (350, 600)

class WindowManager(ScreenManager):
    def route_initial(self):
        self.transition = NoTransition()
        self.current = "intro"


class MainApp(MDApp):
    def build(self):
        manager = WindowManager()
        manager.route_initial()
        return manager

app = MainApp()
app.run()

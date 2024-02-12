# from kivy.core.window import Window
# from kivy.lang import Builder
from kivy.base import EventLoop
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp


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

    def on_pause(self):
        return True

app = MainApp()
EventLoop.ensure_window()
app.run()

from kivy.clock import Clock
from kivy.uix.screenmanager import SlideTransition
from kivymd.uix.screen import MDScreen


class IntroScreen(MDScreen):
    def redirection_automatique(self, *args):
        self.manager.transition = SlideTransition()
        self.manager.current = "login"

    def on_enter(self, *args):
        print("Intro screen on enter")
        Clock.schedule_once(self.redirection_automatique, 3.5)

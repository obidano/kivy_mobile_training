from kivy.uix.screenmanager import SlideTransition
from kivymd.uix.screen import MDScreen
from faker import Faker
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget


class ListeEtudiantsScreen(MDScreen):

    def __init__(self, **kwargs):
        print("ListeEtudiantsScreen, on_init")
        self.etudiants = self.recuperer_etudiants()
        super().__init__()

    def retour_page_precedente(self):
        self.manager.transition = SlideTransition()
        self.manager.current = "login"

    def recuperer_etudiants(self):
        faker = Faker()
        source_donnees = [faker.name() for i in range(20)]
        return source_donnees

    def quand_la_page_sera_prete(self, *args):

        self.ids.label_id.text = f"Etudiants ({len(self.etudiants)})"

        for data in self.etudiants:
            ligne = OneLineAvatarIconListItem(
                IconLeftWidget(icon="lock"),
                text=data
            )
            self.ids.ma_liste_de_donnees.add_widget(ligne)

    def on_enter(self, *args):
        from kivy.clock import Clock
        Clock.schedule_once(self.quand_la_page_sera_prete, 0.5)

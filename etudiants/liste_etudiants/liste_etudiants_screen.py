from kivy.uix.screenmanager import SlideTransition
from kivymd.uix.screen import MDScreen
from faker import Faker
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget


class ListeEtudiantsScreen(MDScreen):

    def retour_page_precedente(self):
        self.manager.transition = SlideTransition()
        self.manager.current = "login"

    def recuperer_etudiants(self):
        faker = Faker()
        etudiants = [faker.name() for i in range(50)]
        return etudiants

    def quand_la_page_sera_prete(self, *args):
        etudiants = self.recuperer_etudiants()
        self.ids.label_id.text = f"Etudiants ({len(etudiants)})"

        for data in etudiants:
            ligne = OneLineAvatarIconListItem(
                IconLeftWidget(icon="lock"),
                text=data
            )
            self.ids.ma_liste_de_donnees.add_widget(ligne)

    def on_enter(self, *args):
        from kivy.clock import Clock
        Clock.schedule_once(self.quand_la_page_sera_prete, 0.5)

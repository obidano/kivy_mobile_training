from kivymd.uix.screen import MDScreen


class ListeEtudiantsScreen(MDScreen):
    def recuperer_etudiants(self):
        from faker import Faker
        faker=Faker()

    def quand_la_page_sera_prete(self, *args):
        self.ids.label_id.text = "Etudiants (1)"

    def on_enter(self, *args):
        from kivy.clock import Clock
        Clock.schedule_once(self.quand_la_page_sera_prete, 0.5)

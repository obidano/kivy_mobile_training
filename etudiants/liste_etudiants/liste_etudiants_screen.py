from kivymd.uix.screen import MDScreen


class ListeEtudiantsScreen(MDScreen):
    def recuperer_etudiants(self):
        from faker import Faker
        faker=Faker()

        # premiere version
        # etudiants=[]
        # for i in range(50):
        #     nom= faker.name()
        #     etudiants.append(nom)
        # version 2
        etudiants = [faker.name() for i in range(50)]
        return etudiants

    def quand_la_page_sera_prete(self, *args):
        from kivymd.uix.list import MDListItem, MDListItemLeadingIcon, \
            MDListItemHeadlineText
        self.ids.label_id.text = "Etudiants (1)"
        etudiants=self.recuperer_etudiants()
        for data in etudiants:
            ligne=MDListItem(
                MDListItemLeadingIcon(icon="lock"),
                MDListItemHeadlineText(text=data)
            )
            self.ids.ma_liste_de_donnees.add_widget(ligne)

    def on_enter(self, *args):
        from kivy.clock import Clock
        Clock.schedule_once(self.quand_la_page_sera_prete, 0.5)

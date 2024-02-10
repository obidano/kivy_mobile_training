from kivymd.uix.screen import MDScreen


class LoginScreen(MDScreen):
    nom=""
    mot_de_passe=""
    def saisie_username(self, nom_clavier):
        self.nom = nom_clavier
        print(self.nom)
    def saisie_mot_passe(self, mot_de_passe_clavier):
        self.mot_de_passe= mot_de_passe_clavier
    def valider(self):
        print("Envoie du formulaire", self.nom, self.mot_de_passe)
        self.manager.current = "etudiants"
    def on_enter(self, *args):
        pass
class Match:
    def __init__(self, equipe1, equipe2, score1, score2):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.score1 = score1
        self.score2 = score2

    def saisir_resultat(self):
        # Logique pour saisir le résultat du match
        self.equipe1.jouer_match((self.score1, self.score2))
        self.equipe2.jouer_match((self.score2, self.score1))

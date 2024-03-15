class Equipe:
    def __init__(self, nom, stade, capacite_stade, entraineur):
        self.nom = nom
        self.stade = stade
        self.capacite_stade = capacite_stade
        self.entraineur = entraineur
        self.points = 0
        self.matches_joues = 0
        self.victoires = 0
        self.nuls = 0
        self.defaites = 0
        self.but_marque = 0
        self.but_encaisse = 0
        self.difference_buts = 0  # Ajout de l'attribut difference_buts avec une valeur initiale de 0

    def calculer_difference_buts(self):
        self.difference_buts = self.but_marque - self.but_encaisse


    def jouer_match(self, resultat):
        # Méthode pour mettre à jour les statistiques de l'équipe après un match
        self.matches_joues += 1
        self.but_marque += resultat[0]
        self.but_encaisse += resultat[1]
        
        if resultat[0] > resultat[1]:
            self.victoires += 1
            self.points += 3
        elif resultat[0] == resultat[1]:
            self.nuls += 1
            self.points += 1
        else:
            self.defaites += 1

        self.calculer_difference_buts()


class Championnat:
    def __init__(self, nom, pays, nb_equipes, pts_victoire, pts_nul, pts_defaite, type_classement):
        self.nom = nom
        self.pays = pays
        self.nb_equipes = nb_equipes
        self.pts_victoire = pts_victoire
        self.pts_nul = pts_nul
        self.pts_defaite = pts_defaite
        self.type_classement = type_classement
        self.equipes = []

    def ajouter_equipe(self, equipe):
        if len(self.equipes) < self.nb_equipes:
            self.equipes.append(equipe)
            print(f"L'équipe {equipe.nom} a été ajoutée au championnat {self.nom}.")
        else:
            print("Le nombre maximum d'équipes pour ce championnat a déjà été atteint.")

    def saisir_resultat(self, equipe1, equipe2, score1, score2):
        # Logique pour saisir le résultat du match entre equipe1 et equipe2
        # Mettre à jour les statistiques des équipes en conséquence
        pass

    def afficher_classement(self):
        print("Classement du championnat", self.nom)
        print("Pts  J.  G.  N.  P.")
        if self.type_classement == "buts_marques":
            classement_trie = sorted(self.equipes, key=lambda x: (x.points, x.but_marque), reverse=True)
        elif self.type_classement == "buts_encaisses":
            classement_trie = sorted(self.equipes, key=lambda x: (x.points, x.but_encaisse), reverse=True)
        elif self.type_classement == "difference_buts":
            classement_trie = sorted(self.equipes, key=lambda x: (x.points, x.difference_buts), reverse=True)
        else:
            print("Type de classement non pris en charge.")
            return
        
        for i, equipe in enumerate(classement_trie, start=1):
            print(f"{i} {equipe.nom} {equipe.points} {equipe.matches_joues} {equipe.victoires} {equipe.nuls} {equipe.defaites}")


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

    def calculer_difference_buts(self):
        self.difference_buts = self.but_marque - self.but_encaisse

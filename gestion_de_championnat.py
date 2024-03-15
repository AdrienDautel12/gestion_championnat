from championnat import Championnat
from equipe import Equipe
from match import Match


# Import des classes
from championnat import Championnat
from equipe import Equipe
from match import Match

# Liste pour stocker les championnats
liste_des_championnats = []

# Ajouter des championnats
# Liste pour stocker les championnats
liste_des_championnats = []

# Ajouter des championnats
championnat_1 = Championnat("Ligue 1", "Angleterre", 20, 3, 1, 0, "difference_buts")
championnat_2 = Championnat("Serie A", "France", 20, 3, 1, 0, "difference_buts")

# Ajouter chaque championnat individuellement à la liste
liste_des_championnats.append(championnat_1)
liste_des_championnats.append(championnat_2)


# Ajouter des équipes
equipe_1 = Equipe("Lille", "Old Trafford", 75000, "Ole Gunnar Solskjær")
equipe_2 = Equipe("Intermilan", "Anfield", 54074, "Jurgen Klopp")
equipe_3 = Equipe("Paris Saint-Germain", "Parc des Princes", 47929, "Mauricio Pochettino")
equipe_4 = Equipe("AC Milan", "Stade", 54074, "Pasta Pizza")

# Ajouter les équipes aux championnats
championnat_1.ajouter_equipe(equipe_1)
championnat_2.ajouter_equipe(equipe_2)
championnat_2.ajouter_equipe(equipe_4)
championnat_1.ajouter_equipe(equipe_3)

# Ajouter des matchs
match_1 = Match(equipe_1, equipe_2, 2, 1)
match_2 = Match(equipe_2, equipe_3, 3, 3)

# Saisir les résultats des matchs
match_1.saisir_resultat()
match_2.saisir_resultat()

# Afficher le classement
championnat_1.afficher_classement()


def trouver_championnat_par_nom(nom_championnat):
    for championnat in liste_des_championnats:
        if championnat.nom == nom_championnat:
            return championnat
    return None


def afficher_menu():
    print("Menu :")
    print("1. Ajouter un championnat")
    print("2. Ajouter une équipe")
    print("3. Ajouter un match")
    print("4. Afficher les championnats")
    print("5. Afficher la liste des équipes d'un championnat")
    print("6. Afficher le classement d'un championnat")
    print("7. Quitter l'application")

def ajouter_championnat():
    nom = input("Entrez le nom du championnat : ")
    pays = input("Entrez le pays du championnat : ")
    nb_equipes = int(input("Entrez le nombre d'équipes : "))
    pts_victoire = int(input("Entrez le nombre de points pour une victoire : "))
    pts_nul = int(input("Entrez le nombre de points pour un match nul : "))
    pts_defaite = int(input("Entrez le nombre de points pour une défaite : "))
    type_classement = input("Entrez le type de classement des ex aequo (buts_marques, buts_encaisses, difference_buts) : ")
    championnat = Championnat(nom, pays, nb_equipes, pts_victoire, pts_nul, pts_defaite, type_classement)
    liste_des_championnats.append(championnat)  # Ajouter le championnat à la liste


def ajouter_equipe():
    nom = input("Entrez le nom de l'équipe : ")
    stade = input("Entrez le nom du stade : ")
    capacite_stade = int(input("Entrez la capacité du stade : "))
    entraineur = input("Entrez le nom de l'entraîneur : ")
    equipe = Equipe(nom, stade, capacite_stade, entraineur)
    nom_championnat = input("Entrez le nom du championnat où ajouter l'équipe : ")
    championnat = trouver_championnat_par_nom(nom_championnat)
    if championnat:
        championnat.ajouter_equipe(equipe)
    else:
        print("Championnat non trouvé.")

def ajouter_match():
    nom_championnat = input("Entrez le nom du championnat : ")
    championnat = trouver_championnat_par_nom(nom_championnat)
    if championnat:
        nom_equipe1 = input("Entrez le nom de la première équipe : ")
        nom_equipe2 = input("Entrez le nom de la deuxième équipe : ")
        score1 = int(input(f"Entrez le score de {nom_equipe1} : "))
        score2 = int(input(f"Entrez le score de {nom_equipe2} : "))
        
        equipe1 = trouver_equipe_par_nom(championnat, nom_equipe1)
        equipe2 = trouver_equipe_par_nom(championnat, nom_equipe2)
        
        if equipe1 and equipe2:
            match = Match(equipe1, equipe2, score1, score2)
            match.saisir_resultat() 
            print("Résultat du match ajouté avec succès.")
        else:
            print("Une ou plusieurs équipes saisies ne sont pas présentes dans ce championnat.")
    else:
        print("Championnat non trouvé.")


def trouver_equipe_par_nom(championnat, nom_equipe):
    for equipe in championnat.equipes:
        if equipe.nom == nom_equipe:
            return equipe
    return None


def afficher_championnats():
    print("Liste des championnats :")
    for championnat in liste_des_championnats:
        print(championnat.nom)
        

def afficher_classement_championnat(championnat):
    classement = sorted(championnat.equipes, key=lambda equipe: equipe.points, reverse=True)
    for i, equipe in enumerate(classement, start=1):
        print(f"{i}. {equipe.nom} - {equipe.points} points")
        

def afficher_equipes_championnat(championnat):
    print(f"Liste des équipes du championnat {championnat.nom}:")
    for equipe in championnat.equipes:
        print(equipe.nom)


def afficher_classement(self):
    print("Pts  J.  G.  N.  P.")
    classement_trie = sorted(self.equipes, key=lambda x: (x.points, x.victoires, x.nuls, -x.defaites), reverse=True)
    for i, equipe in enumerate(classement_trie, start=1):
        print(f"{i} {equipe.nom} {equipe.points} {equipe.matches_joues} {equipe.victoires} {equipe.nuls} {equipe.defaites}")


def saisir_resultats_equipes():
    equipe1_nom = input("Entrez le nom de la première équipe : ")
    equipe2_nom = input("Entrez le nom de la deuxième équipe : ")
    score1 = int(input(f"Entrez le score de {equipe1_nom} : "))
    score2 = int(input(f"Entrez le score de {equipe2_nom} : "))
    


def trouver_championnat_par_nom(nom_championnat):
    for championnat in liste_des_championnats:
        if championnat.nom == nom_championnat:
            return championnat
    return None

# Programme principal
while True:
    afficher_menu()
    choix = input("Entrez votre choix : ")
    if choix == "1":
        ajouter_championnat()
    elif choix == "2":
        ajouter_equipe()
    elif choix == "3":
        nom_championnat = input("Entrez le nom du championnat : ")
        championnat = trouver_championnat_par_nom(nom_championnat)
        if championnat:
            afficher_equipes_championnat(championnat)
            saisir_resultats_equipes()
            ajouter_match_input = input("Voulez-vous ajouter un match ? (oui/non) : ")
            if ajouter_match_input.lower() in ["oui", "o"]:
                ajouter_match()
        else:
            print("Championnat non trouvé.")
    elif choix == "4":
        afficher_championnats()
    elif choix == "5":
        nom_championnat = input("Entrez le nom du championnat : ")
        championnat = trouver_championnat_par_nom(nom_championnat)
        if championnat:
            afficher_equipes_championnat(championnat)
        else:
            print("Championnat non trouvé.")
    elif choix == "6":
        nom_championnat = input("Entrez le nom du championnat : ")
        championnat = trouver_championnat_par_nom(nom_championnat)
        if championnat:
            championnat.afficher_classement()
        else:
            print("Championnat non trouvé.")
    elif choix == "7":
        print("Merci d'avoir utilisé l'application.")
        break
    else:
        print("Choix invalide. Veuillez choisir une option valide.")


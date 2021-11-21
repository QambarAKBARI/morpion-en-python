import random

def affichage_grille(tableau):
    pion = ""
    bord = "\t-------------------------------------------------"
    for i in range(0, len(tableau[0])):
        chaine = "\t|"
        for j in range(0, len(tableau[0])):
            if tableau[i][j] == 1:
                pion = "X"
            elif tableau[i][j] == 10:
                pion = "O"
            else:
                pion = "-"
            chaine += "\t"+pion+"\t|"
        print(bord)
        print(chaine)
    print(bord)

def poser_pion(case_joueur, val_case):
    index_ligne = 0
    index_colonne = 0
    for i in range(0, len(jeu)):
        if mapping[i].count(case_joueur):
            index_ligne = i
            index_colonne = mapping[i].index(case_joueur)
    
    if jeu[index_ligne][index_colonne] == 0:
        jeu[index_ligne][index_colonne] = val_case
        return 1
    
    else:
        print("Case déjà occupée !")
        return 0

def verification_grille(tableau):
    #verification fin du jeu
    nombre_cases_libres = 0
    for i in tableau:
        nombre_cases_libres += i.count(0)
    
    #Verification des lignes
    for i in tableau:
        if sum(i) == 3:
            return 1
        elif sum(i) == 30:
            return 2
    
    #Verification des colonnes
    for i in range(0, len(tableau[0])):
        somme = 0
        for j in range(0, len(tableau[0])):
            somme += tableau[j][i]
        if somme == 3:
            return 1
        elif somme == 30:
            return 2
    
    #Verification des diagonales
    somme = 0
    somme2 = 0
    for i in range(0, len(tableau[0])):
        somme += tableau[i][i]
        somme2 += tableau[len(tableau[0])-i-1][i]
    if somme == 3 or somme2 == 3:
        return 1
    elif somme == 30 or somme2 == 30:
        return 2
    
    if nombre_cases_libres == 0:
        return 3
    else: 
        return 0

jeu = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]
mapping = [[7, 8, 9],
           [4, 5, 6], 
           [1, 2, 3]]
etat_jeu = 0
touche = 0
nom_joueur_1, nom_joueur_2 = "Bob", "Alice"
victoire_joueur_1, victoire_joueur_2 = 0, 0
start = 0
score_atteindre = 0
numero_partie = 0

score_atteindre = int(input("Quel score souhaitez-vous atteindre ? "))
nom_joueur_1 = input("Prénom du joueur 1 : ")
nom_joueur_2 = input("Prénom du joueur 2 : ")

# Tant que le score n'est pas atteint on continue de jouer
while (victoire_joueur_1 < score_atteindre) and (victoire_joueur_2 < score_atteindre):
    print(f"PARTIE N°{numero_partie}")
    # Qui commence la partie ?
    start = random.randint(0, 1)
    nombre_tours = 0
    
    # etat_jeu == 0, la partie continue
    # etat_jeu == 1, le joueur 1 gagne
    # etat_jeu == 2, le joueur 2 gagne
    # etat_jeu == 3, il n'y a pas de gagnant toutes les cases sont occupées
    etat_jeu = 0
    
    # On initialise le plateau du jeu
    jeu = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

    # Tant que personne n'a gagné et que les cases ne sont pas remplies, on continue
    while etat_jeu == 0 :
        affichage_grille(jeu)

        # C'est au joueur 1 de commencer
        if nombre_tours%2 == start:
                touche = int(input(f"{nom_joueur_1} veuillez poser votre pion : "))
                if poser_pion(touche, 1):
                    nombre_tours += 1
        
        # sinon ca sera le joueur 2
        else:
                touche = int(input(f"{nom_joueur_2} veuillez poser votre pion : "))
                if poser_pion(touche, 10):
                    nombre_tours += 1

        # On vérifie la grille du jeu, un gagnant ? Toutes les cases sont occupées ?
        etat_jeu = verification_grille(jeu) 

        if etat_jeu == 1:
            print(f"Victoire de {nom_joueur_1} !")
            victoire_joueur_1 += 1
            affichage_grille(jeu)
        elif etat_jeu == 2:
            print(f"Victoire de {nom_joueur_2} !")
            affichage_grille(jeu)
            victoire_joueur_2 += 1
        elif etat_jeu == 3:
            print(f"Fin du jeu aucun gagnant !")
            affichage_grille(jeu)

    print ("\n-------------------")
    print ("\nTABLEAU DES SCORES")
    print (f"{nom_joueur_1} : {victoire_joueur_1}\t{nom_joueur_2} : {victoire_joueur_2}")
    numero_partie += 1

print ("\n-------------------")

# Finallement qui remporte les parties ?
if victoire_joueur_1 > victoire_joueur_2:
    print(f"C'est {nom_joueur_1} qui remporte la partie !")    
else:
    print(f"C'est {nom_joueur_2} qui remporte la partie !")
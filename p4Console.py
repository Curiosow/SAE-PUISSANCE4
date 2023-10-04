def matrice(ligne, colonne):
    grande_liste = []
    for y in range(ligne):
        petite_liste = []
        for x in range(colonne):
            petite_liste.append("  ")
        grande_liste.append(petite_liste)
    return grande_liste


x = 7
y = 6
grille = matrice(y, x)


def affichage(grille):
    for x in range(0, 6):
        print("----------------------")
        print("|", end="")
        for y in range(0, 7):
            print(grille[x][y], end="")
            print("|", end="")
        print()
    print("----------------------")
    print(" 1  2  3  4  5  6  7")


def saisir_pseudos():
    joueur1 = input("Entrez le pseudo du joueur 1 : ")
    joueur2 = input("Entrez le pseudo du joueur 2 : ")
    return joueur1, joueur2


def colone_valide(pion, couleur, joueur1, joueur2):
    case = False
    index = y - 1
    while not case:
        if index < 0:
            case = True

        if grille[index][pion - 1] == "  ":
            case = True
            grille[index][pion - 1] = couleur
        else:
            index -= 1

    detection_result = detection_victoire(grille)
    if detection_result:
        gagnant = joueur1 if detection_result == "J " else joueur2
        print(f"Le joueur {gagnant} a gagné !")
        exit()  # Quitte le programme après la victoire

    return grille


def change_player(isJoueur1):
    if isJoueur1:
        return False
    else:
        return True


def remplissage():
    isJoueur1 = True
    couleur = None
    for i in range(0, 42):
        if isJoueur1:
            couleur = "J "
        elif not isJoueur1:
            couleur = "R "

        pion = int(input("dans quelle colone voulez vous mettre votre pion ? : "))
        if not (pion <= x) and (pion >= 0):
            while pion >= x and pion >= 0:
                pion = int(input("La colone n'existe pas, saisissez une autre colone : "))
        colone_valide(pion, couleur)
        affichage(grille)
        isJoueur1 = change_player(isJoueur1)
        detection_victoire(grille)


def detection_victoire(grille):
    # Vérification horizontale
    for ligne in range(y):
        for colonne in range(x - 3):
            if grille[ligne][colonne] == grille[ligne][colonne + 1] == grille[ligne][colonne + 2] == grille[ligne][colonne + 3] != "  ":
                return grille[ligne][colonne]

    # Vérification verticale
    for colonne in range(x):
        for ligne in range(y - 3):
            if grille[ligne][colonne] == grille[ligne + 1][colonne] == grille[ligne + 2][colonne] == grille[ligne + 3][colonne] != "  ":
                return grille[ligne][colonne]

    # Vérification diagonale (de gauche à droite)
    for ligne in range(y - 3):
        for colonne in range(x - 3):
            if grille[ligne][colonne] == grille[ligne + 1][colonne + 1] == grille[ligne + 2][colonne + 2] == grille[ligne + 3][colonne + 3] != "  ":
                return grille[ligne][colonne]

    # Vérification diagonale (de droite à gauche)
    for ligne in range(y - 3):
        for colonne in range(3, x):
            if grille[ligne][colonne] == grille[ligne + 1][colonne - 1] == grille[ligne + 2][colonne - 2] == grille[ligne + 3][colonne - 3] != "  ":
                return grille[ligne][colonne]

    return None


def afficher_victoire(joueur):
    print(f"Félicitations, {joueur} a gagné !")

def main():
    global grille

    joueur1, joueur2 = saisir_pseudos()
    affichage(grille)
    isJoueur1 = True

    gagnant = None
    while not gagnant:
        pion = int(
            input(f"{joueur1 if isJoueur1 else joueur2}, dans quelle colonne voulez-vous mettre votre pion ? : "))
        if not (1 <= pion <= x):
            print("La colonne n'existe pas, veuillez saisir un numéro de colonne entre 1 et 7.")
            continue

        grille = colone_valide(pion, "J " if isJoueur1 else "R ", joueur1, joueur2)

        affichage(grille)
        isJoueur1 = not isJoueur1

    afficher_victoire(gagnant)

if __name__ == '__main__':
    main()



"""
Importation des ressources nécessaires

PyGame: Bibliothèque graphique
Body: Fichier contenant les couleurs
pions: Fichier contenant la gestion des pions
time: Bibliothèque de gestion du temps

"""
import pygame
import body
import pions
from time import sleep

"""
Paramètres de l'interface graphique

DIM_GRILLE: Dimension de la grille de jeu (modulable)
TAILLE_CELLULE: Taille d'une cellule de la grille (carré du pion)
TAILLE_FENETRE: Calcul automatique de la taille de la fenêtre en fonction de la taille de la grille et de la taille d'une cellule
RADIUS: Rayon du pion

"""
DIM_GRILLE = (7, 6)
TAILLE_CELLULE = 100
TAILLE_FENETRE = (DIM_GRILLE[0] * TAILLE_CELLULE, (DIM_GRILLE[1] + 1) * TAILLE_CELLULE)
RADIUS = TAILLE_CELLULE // 2 - 5

"""
Initialisation de l'interface

pygame.display.set_caption: Définir le titre de la fenêtre
pygame.display.set_mode: Définir la taille de la fenêtre avec notre variable TAILLE_FENETRE 

"""
pygame.init()
pygame.display.set_caption("Puissance 4")
fenetre = pygame.display.set_mode(TAILLE_FENETRE)

"""
Variables dynamiques du jeu

grille: Définition de la matrice de jeu
running: Variable de la boucle principale
all_pions: Liste des pions de la partie
isFirstPlayer: Si c'est le tour du premier joueur ou non
hasStartGame: Si la partie a commencé ou non
menuId: Identifiant du menu actuel

joueur1: Pseudo du joueur 1
joueur2: Pseudo du joueur 2

pygame.font.init: Initialisation des polices d'écriture
vicFont: Police d'écriture pour le message de victoire
txtFont: Police d'écriture pour les textes

pygame.display.update: Mise à jour de l'interface

"""
grille = [[" " for _ in range(DIM_GRILLE[0])] for _ in range(DIM_GRILLE[1])]
running = True
all_pions = []
isFirstPlayer = True
hasStartGame = False
menuId = "GAMEMODE"


pygame.font.init()
police = pygame.font.SysFont('Arial', 30)

joueur1 = ""
rectangleJoueur1 = pygame.Rect(50, 200, 200, 50)

joueur2 = ""
rectangleJoueur2 = pygame.Rect(50, 300, 200, 50)


vicFont = pygame.font.SysFont("monospace", 40)
txtFont = pygame.font.SysFont("monospace", 20)

pygame.display.update()

"""
Fonctions appelées tout au long de la partie 
Nommées généralement getters et setters.

changePlayer: Changer le joueur actuel
getLetter: Récupérer la lettre du joueur actuel
getJoueurWithD: Récupérer le joueur actuel avec un "d'" ou "de" en fonction de la première lettre de son pseudo
getJoueurByLetter: Récupérer le pseudo du joueur en fonction de sa lettre
getColor: Récupérer la couleur du joueur actuel
getNameColorByLetter: Récupérer le nom de la couleur du joueur actuel

"""
def changePlayer():
    global isFirstPlayer

    if(isFirstPlayer):
        isFirstPlayer = False
    else:
        isFirstPlayer = True

def getLetter():
    letter = "R"
    if (isFirstPlayer):
        letter = "J"
    return letter

def getJoueurWithD(letter):
    base = getJoueurByLetter(letter)
    voyelles = ["a","A","e","E","i","I","o","O","u","U","y","Y"]
    char = base[0]
    if(char in voyelles):
        return "d'" + base
    else:
        return "de " + base

def getJoueurByLetter(letter):
    if(letter == "J"):
        return joueur1
    elif(letter == "R"):
        return joueur2

def getColor():
    color = "Rouge"
    if (isFirstPlayer):
        color = "Jaune"
    return color

def getNameColorByLetter(letter):
    if (letter == "J"):
        return "Jaune"
    elif (letter == "R"):
        return "Rouge"
    else:
        return None


"""
Mises à jour visuel

draw_grid: Dessiner la grille de jeu et les pions
set_pions: Création d'un pion avec notre objet pion de pions.py et ajout dans la liste all_pions
updateDemarrage: Mise à jour de l'écran de démarrage
updateScreen: Mise à jour de l'écran de jeu
updateConsole: Mise à jour de la console pour suivre le dérouler de la partie
getGoodPionInGril: Récupérer la bonne case de la grille pour placer le pion

"""
def draw_grid():
    for col in range(DIM_GRILLE[0]):
        for lig in range(DIM_GRILLE[1]):
            pygame.draw.circle(fenetre, body.Blanc, (col * TAILLE_CELLULE + TAILLE_CELLULE // 2, (lig + 1) * TAILLE_CELLULE + TAILLE_CELLULE // 2), RADIUS)

    for pion in all_pions:
        pygame.draw.circle(fenetre, pion.realColor(), (pion.x + TAILLE_CELLULE // 2, (pion.y + 1) + TAILLE_CELLULE // 2), RADIUS)


def set_pions(x,y):
    pion = pions.pion(getColor(), x * TAILLE_CELLULE, y * TAILLE_CELLULE)
    all_pions.append(pion)

logoStartButton = pygame.image.load("start-button.png")
# logoStartButtonRct : Définition de la zone cliquable du bouton de démarrage
logoStartButtonRct = logoStartButton.get_rect()

def updateDemarrage():
    if(menuId == "GAMEMODE"):
        logoStartGraphic = pygame.image.load("start-graphic.png")
        fenetre.blit(logoStartGraphic, (TAILLE_FENETRE[0] // 4, TAILLE_FENETRE[1] // 5))

        logoStartConsole = pygame.image.load("stop-game.png")
        fenetre.blit(logoStartConsole, (TAILLE_FENETRE[0] // 4, TAILLE_FENETRE[1] // 2))
    elif(menuId == "CHOOSENAME"):
        writeYourName = txtFont.render(f"Écrivez vos pseudos ici", 1, body.Blanc)
        fenetre.blit(writeYourName, [50, 150])

        wherePlaceCursor = txtFont.render(f"Mettez votre curseur à l'endroit où vous voulez écrire", 1, body.Blanc)
        fenetre.blit(wherePlaceCursor, [50, 170])

        pygame.draw.rect(fenetre, body.Gris, rectangleJoueur1)
        texteJoueur1 = police.render(joueur1, True, body.Noir)
        fenetre.blit(texteJoueur1, (rectangleJoueur1.x, rectangleJoueur1.y))

        pygame.draw.rect(fenetre, body.Gris, rectangleJoueur2)
        texteJoueur2 = police.render(joueur2, True, body.Noir)
        fenetre.blit(texteJoueur2, (rectangleJoueur2.x, rectangleJoueur2.y))

        fenetre.blit(logoStartButton, (TAILLE_FENETRE[0] // 1.8, TAILLE_FENETRE[1] // 5))

def updateScreen():
    fenetre.fill(body.Noir)

    logo = pygame.image.load('p4-logo.png')
    fenetre.blit(logo, (0, 0))

    # Ligne de séparation entre le logo et la grille
    pygame.draw.line(fenetre, body.LightBlanc, (0, 101), (800, 101), 5)


    if(hasStartGame):
        draw_grid()

        playerTo = txtFont.render(f"C'est au tour {getJoueurWithD(getLetter())}.", 1, body.Gris)
        pionColorTo = txtFont.render(f"La couleur est {getNameColorByLetter(getLetter())}.", 1, body.Gris)
        fenetre.blit(playerTo, [350, 5])
        fenetre.blit(pionColorTo, [420, 30])
    else:
        updateDemarrage()

    pygame.display.flip()

"""
Mises à jour console
"""
def updateConsole():
    # Permet de mieux visualiser la console
    for n in range(0, 10):
        print("")

    for lig in grille:
        print(lig)


def getGoodPionInGril(col):
    # Va de en bas en haut pour trouver la première case vide
    for lig in reversed(range(DIM_GRILLE[1])):
        if (grille[lig][col] == " "):
            grille[lig][col] = getLetter()
            set_pions(col, lig + 1)
            break # Coupe la boucle


"""
Système de victoire

check_victoire: Vérifier si un joueur a gagné
check_range: Vérifier si un joueur a gagné en fonction de la direction
victoire: Afficher l'écran de victoire

"""
def check_victoire():
    def check_range(lig, col, di, dj):
        pion = grille[lig][col]
        if pion == ' ':
            return False
        for _ in range(3):
            lig, col = lig + di, col + dj
            if lig < 0 or lig >= DIM_GRILLE[1] or col < 0 or col >= DIM_GRILLE[0] or grille[lig][col] != pion:
                return False
        return True

    for lig in range(DIM_GRILLE[1]):
        for col in range(DIM_GRILLE[0]):
            if grille[lig][col] != ' ':
                if check_range(lig, col, 0, 1) or check_range(lig, col, 1, 0) or check_range(lig, col, 1, 1) or check_range(lig, col, 1, -1):
                    return grille[lig][col]

    return None

def victoire():
    global running

    fenetre.fill(body.Noir)
    logo = pygame.image.load('p4-logo.png')
    fenetre.blit(logo, (0, 0))
    pygame.draw.line(fenetre, body.LightBlanc, (0, 101), (800, 101), 5)

    vicJoueurText = vicFont.render(f"Victoire {getJoueurWithD(check_victoire())} !", 1, body.Orange)
    vicText = vicFont.render(f"Il était {getNameColorByLetter(check_victoire())}.", 1, body.Orange)
    fenetre.blit(vicJoueurText, [100, 500])
    fenetre.blit(vicText, [100, 535])

    pygame.display.flip()
    sleep(5)
    running = False


"""
Fonction de démarrage du jeu

runGame: Boucle principale du jeu

"""
def runGame():
    global running,hasStartGame,menuId,joueur1,joueur2

    while (running):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
                pygame.quit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (hasStartGame):
                    if (pygame.mouse.get_pos()[1] >= 102):
                        getGoodPionInGril(pygame.mouse.get_pos()[0] // 100)
                        changePlayer()
                        if (check_victoire() != None):
                            victoire()
                    updateConsole()
                else:
                    if (menuId == "GAMEMODE"):
                        if (pygame.mouse.get_pos()[0] >= 170 and pygame.mouse.get_pos()[0] <= 430):
                            if (pygame.mouse.get_pos()[1] >= 210 and pygame.mouse.get_pos()[1] <= 300):
                                menuId = "CHOOSENAME"
                            elif (pygame.mouse.get_pos()[1] >= 420 and pygame.mouse.get_pos()[1] <= 510):
                                running = False
                    elif (menuId == "CHOOSENAME"):
                        if (pygame.mouse.get_pos()[0] >= 380 and pygame.mouse.get_pos()[0] <= 650):
                            if (pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 300):
                                if(len(joueur1) >= 1 and len(joueur2) >= 1):
                                    hasStartGame = True

            if(event.type == pygame.KEYDOWN):
                if (menuId == "CHOOSENAME"):
                    if (rectangleJoueur1.collidepoint(pygame.mouse.get_pos())):
                        if (event.key == pygame.K_BACKSPACE):
                            if (joueur1 != ""):
                                joueur1 = joueur1[:-1]
                        else:
                            if (len(joueur1) < 10):
                                joueur1 += event.unicode

                    elif (rectangleJoueur2.collidepoint(pygame.mouse.get_pos())):
                        if (event.key == pygame.K_BACKSPACE):
                            if (joueur2 != ""):
                                joueur2 = joueur2[:-1]
                        else:
                            if (len(joueur2) < 10):
                                joueur2 += event.unicode
            if(pygame.display.get_init()):
                updateScreen()
    pygame.quit()

if(__name__ == "__main__"):
    runGame()
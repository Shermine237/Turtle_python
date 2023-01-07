import turtle

t = turtle.Turtle()


def erreur_saissie():
    print("Mauvaise saisie, veuillez recommencer")
    print()


def carre(longueur_carre):
    for i in range(0, 4):
        t.forward(longueur_carre)
        t.left(90)


def escalier(longueur_marche, nb_marche):
    for i in range(0, nb_marche):
        t.left(90)
        t.forward(longueur_marche)
        t.right(90)
        t.forward(longueur_marche)


def tete_etoile(longueur_cote):
    for i in range(0, 5):
        t.forward(longueur_cote)
        t.right(72)
        t.forward(longueur_cote)
        t.left(144)


def etoile(longueur_cote):
    t.left(36)
    tete_etoile(longueur_cote)


def triangle(cote_triangle):
    t.forward(cote_triangle)
    t.left(120)
    t.forward(cote_triangle)
    t.left(120)
    t.forward(cote_triangle)


def plusieurs_carres(taille_depart, nb_carres):
    for i in range(1, nb_carres+1):
        carre(i * taille_depart)


def plusieurs_etoiles(taille_depart, nb_etoiles):
    for i in range(1, nb_etoiles+1):
        etoile(i * taille_depart)


# Menu
print("     MENU")
print("1- Carre")
print("2- Escalier")
print("3- Etoile")
print("4- Triangle")
print("5- Plusieurs carres")
print("6- Plusieurs etoiles")

figure = 0
while figure not in range(1, 7):
    try:
        figure = int(input("Entrez le numero de la figure :  "))
        if figure not in range(1, 7):
            # si le chiffre choisi n'est pas entre 1 et 6
            print("Choisissez un chiffre entre 1 et 6")
    except:
        erreur_saissie()

if figure == 1:
    l_carre_utilisateur = 0
    print("Carre")
    while l_carre_utilisateur == 0:
        try:
            l_carre_utilisateur = int(input("Entrez la longueur du carre :  "))
        except:
            erreur_saissie()
    carre(l_carre_utilisateur)

elif figure == 2:
    l_marche_utilisateur = 0
    nb_marche_utilisateur = 0
    print("Escalier")
    while l_marche_utilisateur == 0 or nb_marche_utilisateur == 0:
        try:
            nb_marche_utilisateur = int(input("Entrez le nombre de marche :     "))
            l_marche_utilisateur = int(input("Entrez la longueur de marche :    "))
        except:
            erreur_saissie()
    escalier(l_marche_utilisateur, nb_marche_utilisateur)

elif figure == 3:
    l_cote_utilisateur = 0
    print("Etoile")
    while l_cote_utilisateur == 0:
        try:
            l_cote_utilisateur = int(input("Entrez la longueur d'un cote :  "))
        except:
            erreur_saissie()
    etoile(l_cote_utilisateur)

elif figure == 4:
    l_cote_utilisateur = 0
    print("Triangle")
    while l_cote_utilisateur == 0:
        try:
            l_cote_utilisateur = int(input("Saisissez la longueur de cote :     "))
        except:
            erreur_saissie()
    triangle(l_cote_utilisateur)

elif figure == 5:
    l_carre_utilisateur = 0
    nb_carre_utilisateur = 0
    print("Plusieurs carres")
    while l_carre_utilisateur == 0 or nb_carre_utilisateur == 0:
        try:
            l_carre_utilisateur = int(input("Entrez la longueur de depart du carre :  "))
            nb_carre_utilisateur = int(input("Entrez le nommbre de carres :  "))
        except:
            erreur_saissie()
    plusieurs_carres(l_carre_utilisateur, nb_carre_utilisateur)

elif figure == 6:
    l_etoiles_utilisateur = 0
    nb_etoiles_utilisateur = 0
    print("Plusieurs etoiles")
    while l_etoiles_utilisateur == 0 or nb_etoiles_utilisateur == 0:
        try:
            l_etoiles_utilisateur = int(input("Entrez la longueur de depart de l'etoile :  "))
            nb_etoiles_utilisateur = int(input("Entrez le nommbre d'etoiles' :  "))
        except:
            erreur_saissie()
    plusieurs_etoiles(l_etoiles_utilisateur, nb_etoiles_utilisateur)

else:
    print("Figure non disponible")

turtle.done()

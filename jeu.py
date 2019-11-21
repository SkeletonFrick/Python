import os # On importe la librairie "os" qui permettra notamment de pouvoir ouvrir le fichier python sans passer par IDLE
import math # On importe la librairie "math" qui permettra l'arrondi lors de la division par 0.5
import random # On importe la librairie "random" qui permettra de sélectionnner un nombre aléatoire entre 0 et 49
import time # On importe la librairie "time" qui permettra de temporiser les messages lorsque la roulette tourne

argentTotal = 1000 # On définit la variable argentTotal qui au départ à une valeur de 1000
continuerPartie = True # On définit la variable continuerPartie en tant que True qui permet de continuer la partie tant que l'utilisateur n'a pas choisi de quitter, ou n'est pas ruiné

print("Vous allez vous installer à la table de roulette avec la somme de", argentTotal, "dollars") # On affiche "Vous allez vous installer à la table de roulette avec la somme de (l'argent total) dollars

while continuerPartie == True: # Boucle principale : tant que la variable continuerPartie est égale à True

    nombreMise = -1 # On définit le nombre misé à -1 pour faire fonctionner la boucle suivante
    while nombreMise < 0 or nombreMise > 49: # Tant que la variable nombreMise est inférieure a 0 ou supérieure à 49
        nombreMise = input("Sélectionnez le nombre sur lequel vous souhaitez miser (entre 0 et 49) : ") # On demande à l'utilisateur de définir le nombre sur lequel il veut miser
        try: # On vérifie
            nombreMise = int(nombreMise) # Si l'utilisateur a bien entré un nombre
        except ValueError: # Si ce n'est pas un nombre
            print("Vous devez taper un nombre !") # On affiche "Vous devez taper un nombre"
            nombreMise = -1 # On redéfinit la variable nombreMise à -1
            continue # Et on relance la boucle pour que l'utilisateur saisisse un nombre
        if nombreMise < 0: # Si le nombre que l'utilisateur a choisi est inférieur à 0
            print("Ce nombre est négatif !") # On affiche "Ce nombre est négatif" et on relance la boucle
        if nombreMise > 49: # Si le nombre que l'utilisateur a choisi est supérieur à 49
            print("Ce nombre est trop grand !") # On affiche "Ce nombre est trop grand" et on relance la boucle

    miseDonnee = 0 # On définit la mise donnée par défaut à 0
    while miseDonnee <= 0 or miseDonnee > argentTotal: # On lance la boucle "Tant que miseDonne est inférieure ou égale à zéro OU supérieure à l'argent total
        miseDonnee = input("Veuillez taper votre mise : ") # On fait choisir à l'utilisateur sa mise
        try: # On vérifie
            miseDonnee = int(miseDonnee) # Si la mise entrée est bien un nombre
        except ValueError: # Sinon
            print("Vous devez taper un nombre !") # On affiche "Vous devez taper un nombre"
            miseDonnee = -1 # On redéfinit la variable miseDonnee à 0
            continue # Et on relance la boucle
        if miseDonnee < 0: # Si la mise donnée est inférieure à zéro
            print("Vous ne pouvez pas donner de mise négative !") # On affiche "Vous ne pouvez pas donner de mise négative !" et on relance la boucle
        if miseDonnee > argentTotal: # Si la mise donnée est supérieure à l'argent possédé par le joueur
            print("Vous n'avez que", argentTotal, "dollars !") # On affiche "Vous n'avez que (argent possédé) dollars !" et on relance la boucle

    numeroGagnant = random.randrange(50) # On définit que le numero gagnant est un numéro au hasard entre 0 et 49

    print("La roulette tourne.........") # On affiche "La roulette tourne........"
    time.sleep(1) # On fait patienter le programme une seconde
    print("Et elle tombe sur le numéro", numeroGagnant, "!") # On affiche "Et elle tombe sur le numéro (numéro choisi au hasard) !

    if nombreMise == numeroGagnant: # Si le nombre sur lequel l'utilisateur a misé est le numéro gagnant
        print("Félicitations, vous obtenez", miseDonnee * 3, "dollars !") # On affiche "Félicitations, vous obtenez (mise * 3) dollars !"
        argentTotal += miseDonnee * 3 # On ajoute 3 fois la mise donnée à l'argent possédé par l'utilisateur
    elif numeroGagnant % 2 == nombreMise % 2: # Sinon si le numéro gagnant est de la même couleur que le nombre misé (rouge ou noir)
        miseDonnee = math.ceil(miseDonnee * 0.5) # On lui redonne la moitié de sa mise, arrondie à l'entier le plus proche
        print("Félicitations, vous avez choisi la bonne couleur, vous obtenez", miseDonnee, "dollars") # On affiche "Félicitations, vous avez choisi la bonne couleur, vous obtenez (la moitié de sa mise) dollars"
        argentTotal += miseDonnee # On ajoute la moitié de sa mise à son argent total
    else: # Sinon, si le numéro choisi n'est ni gagnant ni de la même couleur
        print("Dommage, vous n'avez pas gagné cette-fois !") # On affiche "Dommage, vous n'avez pas gagné cette-fois !"
        argentTotal -= miseDonnee # Et on retire la mise de l'utilisateur à son argent total

    if argentTotal <= 0: # Si l'argent de l'utilisateur atteint 0
        print("Vous êtes ruiné, la partie est terminée !") # On affiche "Vous êtes ruiné, la partie est terminée !"
        continuerPartie = False # On définit la variable continuerPartie en False, ce qui ferme la boucle principale et ferme le programme
    else: # Sinon
        print("Vous avez à présent", argentTotal, "$") # On affiche "Vous avez à présent (argent possédé) $"
        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ") # On demande à l'utilisateur s'il souhaite quitter le jeu
        if quitter == "o" or quitter == "O": # Si l'utilisateur tape "o" ou "O"
            print("Vous quittez le casino avec vos gains.") # On affiche "Vous quitter le casino avec vos gains."
            continuer_partie = False # On définit la variable continuerPartie en False, ce qui ferme la boucle principale, et donc le programme
        # Sinon, on relance la boucle principale du début

os.system("pause") # On met l'os en pause afin de pouvoir lancer le programme

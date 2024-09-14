from gpiozero import LED, Button
from time import sleep
import random
from Partie import  Partie
ledRouge = LED(16)
boutonRouge = Button(12)
boutonRouge.when_pressed = ledRouge.on
boutonRouge.when_released = ledRouge.off

ledJaune = LED(20)
boutonJaune = Button(26)
boutonJaune.when_pressed = ledJaune.on
boutonJaune.when_released = ledJaune.off

ledBleu = LED(21)
boutonBleu = Button(19)
boutonBleu.when_pressed = ledBleu.on
boutonBleu.when_released = ledBleu.off
 # Methode qui demande le niveau de difficulté
def demander_niveau():
    print("Choisissez le niveau:")
    print("1. Facile - appuyez sur bouton rouge")
    print("2. Intermédiaire - appuyez sur bouton bleu")
    print("3. Difficile - appuyez sur bouton jaune")

    while True:
        if boutonRouge.is_pressed:
            return "facile"
        elif boutonBleu.is_pressed:
            return "intermédiaire"
        elif boutonJaune.is_pressed:
            return "difficile"
# Methode qui genere une sequence de lumières
def genererSequence(longueur):
    return [random.choice([ledRouge, ledJaune, ledBleu]) for led in range(longueur)]
# Methode qui affiche la sequence de lumières a l'utilisateur
def afficherSequence(sequence, niveau):
    if niveau == "facile":
        delai = 1
    elif niveau == "intermédiaire":
        delai = 0.5
    else:
        delai = 0.25

    for led in sequence:
        led.on()
        sleep(delai)
        led.off()
        sleep(delai / 2)
# Methode qui fait clignoter les lumières
def clignoter(nombreFois):
    for i in range(nombreFois):
        ledRouge.on()
        ledJaune.on()
        ledBleu.on()
        sleep(0.5)
        ledRouge.off()
        ledJaune.off()
        ledBleu.off()
        sleep(0.5)
# Methode qui permet a l'utilisateur de jouer une partie
def jouer():
    while True:  # Boucle principale pour permettre à l'utilisateur de rejouer
        niveau = demander_niveau()
        print("Niveau choisi :", niveau)
        input("Appuyez sur Entrée pour commencer la partie :)")
        nouvellePartie = Partie(nom, niveau)
        while nouvellePartie.nombreSequences < 20: 
            sequence = genererSequence(nouvellePartie.nombreSequences + 1)  # ajout un led a chaque sequence 
            afficherSequence(sequence, niveau)
            # variable qui stocke la sequence de l'utilisateur
            sequenceDeUtilisateur = []
            for led in sequence:
                while True:
                    if boutonRouge.is_pressed:
                        sequenceDeUtilisateur.append(ledRouge)
                        sleep(0.5)  
                        break
                    elif boutonBleu.is_pressed:
                        sequenceDeUtilisateur.append(ledBleu)
                        sleep(0.5)  
                        break
                    elif boutonJaune.is_pressed:
                        sequenceDeUtilisateur.append(ledJaune)
                        sleep(0.5)  #temps d'attente pour que l'utilisateur appuie sur un autre bouton ( pour eviter les erreurs)
                        break
            ledRouge.off()
            ledJaune.off()
            ledBleu.off()
            # si la sequence de l'utilisateur est différente de la sequence générée un message d'erreur s'affiche
            if sequenceDeUtilisateur != sequence:
                print("Mauvaise séquence ! Tony vous invite a recommencer !")
                clignoter(5)
                print(f"Votre pointage est de {nouvellePartie.pointage} points")
                nouvellePartie.sauvegarder()
                break  

            #sinon la prochaine sequence se lance
            nouvellePartie.nombreSequences += 1  
            #ajoute deux points a chaque sequence reussie
            nouvellePartie.pointage += 2
            #Method qui retourne le nom de la couleur de la led
            def ledStr(led):
                if led == ledRouge:
                    return "Rouge"
                elif led == ledJaune:
                    return "Jaune"
                elif led == ledBleu:
                    return "Bleu"

            #ajoute la sequence a la liste des sequences jouées
            nouvellePartie.ajouterSequence([ledStr(led) for led in sequence])

            sleep(1) # temps entre chaque sequence
        # si l'utilisateur a reussi 20 sequences un message de felicitation s'affiche et la partie se termine
        if nouvellePartie.nombreSequences == 20:
            print("Vous avez atteint le maximum de 20 séquences. Tony vous félicite !")
            clignoter(5)
            print(f"Votre pointage est de {nouvellePartie.pointage} points")
            #sauvegarde les informations de la partie
            nouvellePartie.sauvegarder()
        # Demande à l'utilisateur s'il veut rejouer
        rejouer = input("Voulez-vous rejouer ? (Oui/Non) : ")
        if rejouer.lower() != "oui":
            
            
           
            
            break  # Sortir de la boucle  si il ne veut pas rejouer
        


print("........................................")       
print("Travail pratique 2 - Jeu simon - Tony Mourrah")
print("Vous devez reproduire la séquence de lumières donnée mais avec les boutons")
print("Pour chaque bonne sequence vous gagnez deux points")
print("Vos points vont s'afficher a la fin de la partie")
print("........................................")   

nom = ""
while not nom.strip():  # Continue de demander tant que le nom est vide ou ne contient que des espaces
    nom = input("Entrez votre nom : ")
jouer()
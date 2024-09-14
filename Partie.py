import json, os
#fichier pour les informations des parties 
fichierResultat = "resultat.json"
import datetime
# classe partie
class Partie:
    # Constructeur 
    def __init__(self, nomJoueur, niveau):
        self.datePartie = datetime.datetime.now()
        self.nombreSequences = 0
        self.nomJoueur = nomJoueur
        self.niveau = niveau
        self.sequencesJouee = []
        self.pointage = 0


    def ajouterSequence(self, sequence):
        self.sequencesJouee.append(sequence)
    


    def afficher(self):
        return  self.pointage

    def sauvegarder(self):
        infos = {
            "Date : " : self.datePartie.strftime("%d-%m-%Y à %H:%M:%S"),
            "Nom du joueur: ": self.nomJoueur,
            "Niveau de difficultee: ": self.niveau,
            "Nombre de sequences: ": self.nombreSequences,
            "Sequence jouée: ": self.sequencesJouee,
            "Total de points: ": self.pointage,
        }
        
# ouvrir le fichier resultats.json et ses donnes 
        if os.path.exists(fichierResultat):
            with open(fichierResultat, encoding='utf-8') as fic_json:
                donnees = json.load(fic_json)
        else:
            donnees = []

        donnees.append(infos)
#Ecrire les nouvelles donnees dans le fichier sans ecraser les anciens 
        with open(fichierResultat, "w", encoding='utf-8') as fic_json:
            json.dump(donnees, fic_json, indent=4, ensure_ascii=False, sort_keys=True)
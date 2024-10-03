# Simon-Says

Bienvenue sur Simon-Says, un jeu interactif utilisant des objets connectés pour suivre et répondre aux commandes de jeu. Ce projet implémente la logique de jeu avec des séquences lumineuses, incluant des fonctionnalités de connexion et de communication entre les objets pour offrir une expérience immersive et améliorée.

## Structure du Code

Le code est organisé selon le modèle MVC (Modèle-Vue-Contrôleur).

### Modèle

Le modèle gère les données. Il inclut les interactions avec la base de données et les capteurs.

### Vue

La vue est responsable de l'interface utilisateur. Elle utilise Tkinter pour afficher les boutons, les listes et les étiquettes, ainsi que pour gérer les LED.

### Contrôleur

Le contrôleur gère les interactions entre le modèle et la vue. Il reçoit les entrées de l'utilisateur via la vue , met à jour le modèle, et rafraîchit la vue en conséquence.

## Prérequis

- **Matériel** : Raspberry Pi, LED , boutons-poussoirs.
- **Logiciel** : Python, modules Python pour gérer le matériel connecté .

## Installation

Cloner le dépôt du projet :
   ```bash
   git clone https://github.com/votre-utilisateur/simon-says.git


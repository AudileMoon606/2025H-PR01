# Projet 1 - INF1007 H2025

## Directives
:alarm_clock: Date de remise : Le 23 février 2025

:mailbox_with_mail: À remettre sur Moodle

## Introduction
Dans ce projet, vous aurez comme tâche d'implémenter une version de [Pong](https://en.wikipedia.org/wiki/Pong), l'un des tout premiers jeux vidéo, initialement développé par Atari en 1972. Ce jeu emblématique simule une partie de tennis de table, mettant en scène deux raquettes et une balle qui rebondit entre elles. Un point est marqué chaque fois que l'adversaire ne parvient pas à renvoyer la balle avec sa raquette. La partie se termine lorsque l'un des joueurs atteint 11 points, désignant ainsi le vainqueur.

Cette version du jeu inclura deux options : un mode à deux joueurs ("multi player") ou un mode individuel contre l'ordinateur ("single player"). En mode individuel, trois niveaux de difficulté seront disponibles : "easy", "medium", et "hard".

Afin de simplifier votre travail, l'interface graphique du jeu est déjà fournie. Votre tâche consiste à ajouter les fonctionnalités essentielles du jeu, telles que le mouvement des raquettes et de la balle, ainsi que la logique de gestion des points. 

Le jeu final devrait ressembler à l'exemple visible ici, qui illustre une partie dans l'option 'single player' avec la difficulté 'medium'  : 

https://github.com/user-attachments/assets/b111f7d6-7cfd-4b47-9638-23cd7e1d552f

## Installations requises
Ce projet nécessite l'utilisation de la bibliothèque [`pygame`](https://www.pygame.org/wiki/about), qui permet de créer facilement des interfaces de jeu en Python.

Avant de commencer, vous devez vous assurer que pygame est installé sur votre ordinateur. Pour installer la version 2.6.0, utilisez la commande suivante dans votre terminal :

```
python3 -m pip install -U pygame==2.6.0
```

## Structure du projet
Le projet est organisé de la manière suivante : 

```plaintext
2025H_PR01/
├── config.py
├── game.py
├── main.py
├── menus.py
```
Détails sur les fichiers : 
- Le fichier `config.py` contient les paramètres d'intialisation du jeu, telles que les dimensions et la vitesse des raquettes et de la balle.
- Le fichier `menus.py` contient les menus d'affichage, tels que le menu principal et le menu de sélection de la difficulté. 
- Le fichier `game.py` contient la logique du jeu. 
- Le fichier `main.py` est le fichier qui permet de démarrer le jeu. C'est ce fichier que vous allez exécuter. 

## Travail à réaliser

Vous devez compléter les parties suivantes à l'intérieur des fichier `main.py` et `game.py`. Ces parties sont identifiées par des `#TODO` à l'intérieur des fichiers. 

### Partie 1 : Initialisation de la balle 
*Pour la partie 1, les sections suivantes sont à compléter dans le fichier `main.py`.*

#### 1.1 : Initialisation de la position de la balle
Ici, vous devez d'abord définir la position initiale de la balle (les variables `ball_x` et `ball_y`) afin qu'elle commence sa trajectoire au centre de la fenêtre du jeu en x et en y (c'est-à-dire, au centre de la ligne pointillée). (Fait)

#### 1.2 : Initialisation du mouvement aléatoire de la balle
Par la suite, vous devez implémenter le mouvement de la balle dans une direction aléatoire (en x et en y), en définissant les vecteurs de vitesse de la balle, c'est-à-dire les variables `ball_velocity_x` et `ball_velocity_y`. Pour ce faire, vous devez utiliser les vitesses `BALL_SPEED_X` et `BALL_SPEED_Y` définies dans le fichier `config.py`

### Partie 2 : Fonction `reset_ball`
*Pour cette partie, vous aurez à compléter les sections suivantes à l'intérieur de la fonction `reset_ball` dans le fichier `game.py`. Cette fonction gère la réinitialisation de la balle dans le jeu lorsqu'un joueur compte un point.*

#### 2.1 : Réinitialisation de la position de la balle en x
Ici, vous devez redéfinir la position de la balle pour qu'elle soit centrée en x (c'est-à-dire, sur la ligne pointillée). Sa position en y doit toutefois être aléatoire, permettant à la balle de commencer à un point quelconque sur la ligne pointillée après chaque point. 

#### 2.2 : Réinitialisation de la position de la balle en y 
Si le joueur 2 a gagné un point, relancer la balle de son côté (à la gauche) avec une direction aléatoire en y (par en haut ou par en bas).
Si le joueur 1 a gagné un point, relancer la balle de son côté (à la droite) avec une direction aléatoire en y (par en haut ou par en bas).

### Partie 3 : Fonction `play_game`
*Les sections suivantes sont à réaliser à l'intérieur de la fonction `play_game` à l'intérieur du fichier `game.py`. C'est cette fonction qui lance et gère la logique du jeu.*

#### 3.1 : Implémentation du mouvement des raquettes pour l'option "multi player"
Ici, vous devez implémenter le mouvement des raquettes des joueurs 1 et 2 pour le cas "multi player"

Le mouvement de la raquette du joueur 1 doit être contrôlé par les touches `w` (haut) et `s` (bas) du clavier pour les déplacements de haut en bas, respectivement. 
Le mouvement de la raquette du joueur 2 doit être contrôlé par les flèches `UP` (haut) et `DOWN` (bas) du clavier. 

* Note 1 : Pour la gestion des touches de clavier, utilisez les fonctions du [module `key` de la librairie pygame](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed).
* Note 2 : Vous devez utiliser la variable `paddle_speed` pour gérer le mouvement des raquettes. 
* Note 3 : Lorsque les raquettes atteignent le haut ou le bas de la fenêtre de jeu, elles ne doivent pas dépasser ces limites. Assurez-vous que leur position reste dans les bornes définies par la hauteur de l'écran.

#### 3.2 : Implémentation du mouvement des raquettes pour l'option "single player"
- Le joueur 1 contrôle sa raquette avec les touches `w` (haut) et `s` (bas), comme dans le mode "multi player".

- La raquette du joueur 2 (contrôlée par l'ordinateur) doit suivre la position de la balle. Plus précisément :
     - Si la position y de la balle est inférieure au centre de la raquette, la raquette doit monter.
     - Si la position y de la balle est supérieure au centre de la raquette, la raquette doit descendre.

- Afin de rendre les mouvements de l'adversaire un peu plus vraisemblables, vous devez également ajouter une variable nommée `margin` à la position du centre de la raquette. De cette façon, le centre de la raquette de l'adversaire suivra le mouvement de la balle, mais avec un léger décalage. La valeur de la variable `margin` doit varier de façon aléatoire, c'est-à-dire : 
     - 90% du temps, "margin" doit être égale à 40
     - 10% du temps, "margin" doit être égale à 20

- Adaptez la vitesse de déplacement de la raquette du joueur 2 selon le niveau de difficulté sélectionné dans le menu "SELECT DIFFICULTY" :
     - Pour le niveau "easy", la vitesse de déplacement de la raquette doit être égale à `paddle_speed - 5`
     - Pour le niveau "medium", la vitesse de déplacement de la raquette doit être égale à `paddle_speed - 4`
     - Pour le niveau "hard", la vitesse de déplacement de la raquette doit être égale à `paddle_speed`

#### 3.3 : Gestion du mouvement de la balle
- Mettre à jour la position de la balle (les variables `ball_x` et `ball_y`) en utilisant les variables `ball_velocity_x` et `ball_velocity_y`.

- Gérer les collisions de la balle avec le haut et le bas de la fenêtre de jeu. Lorsque la balle atteint le haut ou le bas, sa direction verticale doit être inversée.

- Gérer les collisions entre la balle et les raquettes. Lorsque la balle frappe une raquette, sa direction horizontale doit être inversée.

#### 3.4 : Gestion des points et réinitialisation de la balle
- Vous devez implémenter l'ajout de 1 point à chaque fois qu'un joueur manque la balle et qu'elle frappe l'un des murs.
   
- Vous devez également faire appel à la fonction `reset_ball` (que vous avez complété à la partie 1) pour faire réapparaître la balle dans le jeu.

## Directives pour la remise 

Pour remettre votre travail, vous devez créez un fichier zip nommé XXXXX_YYYYY-PR01.zip, où XXXXX est votre nom de famille et YYYYY, votre prénom. Ce fichier zip devra contenir tous les fichiers .py du projet (`config.py`, `game.py`, `main.py` et `menus.py`). 

Votre fichier zip est à remettre dans la boîte de remise sur Moodle prévue à cet effet, le 16 février avant minuit. 

## Barème de correction

Le barème de correction est le suivant : 

| **Partie**                                | **Tâche**                                                                   | **Points** |
|-------------------------------------------|-----------------------------------------------------------------------------|------------|
| **Partie 1 : Initialisation de la balle** |                                                                             | **/2**     |
|                                           | 1.1 Initialisation de la position de la balle.                              | 1          |
|                                           | 1.2 Initialisation du mouvement aléatoire de la balle.                      | 1          |
| **Partie 2 : Fonction `reset_ball`** |                                                                                  | **/3**     |
|                                           | 2.1 Réinitialisation de la position de la balle en x.                       | 1          |
|                                           | 2.2 Réinitialisation de la position de la balle en y.                       | 2          |
| **Partie 3 : Fonction `play_game`** |                                                                                   | **/15**    |
|                                           | 3.1 Implémentation du mouvement des raquettes pour l'option "multi player". | 3          |
|                                           | 3.2 Implémentation du mouvement des raquettes pour l'option "single player".| 7          |
|                                           | 3.3 Gestion du mouvement de la balle.                                       | 3          |
|                                           | 3.4 Gestion des points et réinitialisation de la balle.                     | 2          |
| **Total**                                 |                                                                             | **/20**    |

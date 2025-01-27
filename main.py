import pygame
from config import *
from game import play_game
from menus import main_menu, select_difficulty
import random

# Initialiser pygame
pygame.init()

# Contrôle de la fréquence d'images
clock = pygame.time.Clock()

# Positions initiales des raquettes en y 
player1_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
player2_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2

# TODO : INITIALISATION DE LA POSITION INITIALE DE LA BALLE
# Ici, vous devez d'abord définir la position initiale de la balle (les variables ball_x et ball_y) 
# afin qu'elle commence sa trajectoire au centre de la fenêtre du jeu en x et en y (c'est-à-dire, au centre de la ligne pointillée). 
# Vous devez utiliser les variables de dimensions définies dans le fichier config.py. 
ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2 # Remplacer "0" par votre réponse
ball_y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2 # Remplacer "0" par votre réponse
 
# TODO : INITIALISATION DU MOUVEMENT ALÉATOIRE DE LA BALLE
# Ici, vous devez implémenter le mouvement de la balle dans une direction aléatoire (en x et en y), en définissant les vecteurs de vitesse de la balle, 
# c'est-à-dire les variables ball_velocity_x et ball_velocity_y. Pour ce faire, vous devez utiliser les vitesses BALL_SPEED_X et BALL_SPEED_Y définies dans le fichier config.py
ball_velocity_x = [-1,1][random.randint(0,1)] * BALL_SPEED_X # Remplacer "0" par votre réponse
ball_velocity_y = [-1,1][random.randint(0,1)] * BALL_SPEED_Y # Remplacer "0" par votre réponse

# Boucle du jeu
while True:
    play_game(player1_y, player2_y, player1_score, player2_score, ball_x, ball_y, ball_velocity_x, ball_velocity_y) 
  
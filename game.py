import pygame
import random
from config import *
from menus import main_menu, select_difficulty, pause_menu, draw_text, draw_center_line

# Initialiser pygame
pygame.init()

# Initialiser la fenêtre du jeu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Contrôle de la fréquence d'images
clock = pygame.time.Clock()

# Police pour aficher du texte
font = pygame.font.Font(None, 36)

def reset_ball(player1_score, player2_score, ball_x, ball_y, ball_velocity_x, ball_velocity_y, difficulty, game_mode):
    """ 
    Fonction pour réinitialiser la balle lorsqu'un joueur gagne un point
    """
    # TODO : RÉINITIALISER LA POSITION DE LA BALLE AU CENTRE DU JEU
    old_ball_x = ball_x
    ball_velocity_x = 0
    ball_velocity_y = 0
    ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
    ball_y = random.randint(BALL_SIZE**2,SCREEN_HEIGHT-BALL_SIZE**2+1)

    # TODO : LANCEMENT DE LA BALLE APRÈS RÉINITIALISATION
    ball_velocity_x = (-1 if old_ball_x >= SCREEN_WIDTH else 1) * BALL_SPEED_X
    ball_velocity_y =  [-1,1][random.randint(0,1)] * BALL_SPEED_Y

    return play_game(SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, player1_score, player2_score, ball_x, ball_y, ball_velocity_x, ball_velocity_y, True, difficulty, game_mode)

def play_game(player1_y, player2_y, player1_score, player2_score, ball_x, ball_y, ball_velocity_x, ball_velocity_y, passing=False, difficulty=None, game_mode = None):
    """
    Fonction qui lance et gère le jeu 
    """
    if passing == False:
        # Définition de la variable "game_mode" comme étant la sortie du menu principal (soit "single player" ou "multi player")
        game_mode = main_menu()

        # Définition de la variable "difficulty" comme étant la sortie du menu "select difficulty" (soit "easy", "medium", ou "hard")
        if game_mode == 'single player':
            difficulty = select_difficulty() 
        else :
            difficulty = None

    running = True
    while running:
        screen.fill(BLACK)

        # Gestion des touches de clavier 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Show the pause menu and capture the return value
                    result = pause_menu()
                    if result == "main menu":
                        reset_game()  # Reset game and return to main menu
                        return  # Exit the play_game loop
                    # If 'resume', simply break out of the pause logic
                    elif result == 'resume':
                        break  # Continue the main game loop

        
        
        
        # Contrôle des touches de clavier
        keys = pygame.key.get_pressed()

        # mouvement joueur 1
        player1_y += paddle_speed if (keys[pygame.K_s] and (player1_y + PADDLE_HEIGHT + paddle_speed) <= SCREEN_HEIGHT) else -paddle_speed if (keys[pygame.K_w] and (player1_y - paddle_speed) >= 0) else 0
        
        # mouvement joueur 2
        if game_mode == "single player":
            margin = 40 if random.randint(0,100) in range(91) else 20
            paddle_speed_2 = (paddle_speed - 5) if difficulty == "easy" else ((paddle_speed - 4) if difficulty == "medium" else paddle_speed)
            direction = 1 if (ball_y > player2_y + margin//2 + PADDLE_HEIGHT//2) else -1 if (ball_y < player2_y - margin//2) else 0
            player2_y = max(0, min(SCREEN_HEIGHT - PADDLE_HEIGHT, player2_y + direction * paddle_speed_2))

        else:
            player2_y += paddle_speed if (keys[pygame.K_DOWN] and (player2_y + PADDLE_HEIGHT + paddle_speed) <= SCREEN_HEIGHT) else -paddle_speed if (keys[pygame.K_UP] and (player2_y - paddle_speed) >= 0) else 0



        # Mettre à jour la position de la balle (les variables "ball_x" et "ball_y") en utilisant les variables "ball_velocity_x" et "ball_velocity_y".
        ball_velocity_y *= -1 if (ball_y - BALL_SIZE <= 0 or ball_y + BALL_SIZE >= SCREEN_HEIGHT) else 1
        ball_velocity_x *= -1 if (
            ((ball_x - max(0, min(ball_x, PADDLE_WIDTH)))**2 + (ball_y - max(player1_y, min(ball_y, player1_y + PADDLE_HEIGHT)))**2 <= (BALL_SIZE // 2)**2)
            or
            ((ball_x - max(SCREEN_WIDTH - PADDLE_WIDTH, min(ball_x, SCREEN_WIDTH)))**2 + (ball_y - max(player2_y, min(ball_y, player2_y + PADDLE_HEIGHT)))**2 <= (BALL_SIZE // 2)**2)
        ) else 1

        ball_x += ball_velocity_x
        ball_y += ball_velocity_y 
        player1_old_score = player1_score
        player2_old_score = player2_score
        player2_score += 1 if ball_x <= 0 else 0
        player1_score += 1 if ball_x >= SCREEN_WIDTH else 0

        
        # Vérifier s'il y a un gagnant
        if player1_score == 11:
            win("PLAYER 1 WINS!")
            return
        if player2_score == 11:
            win("PLAYER 2 WINS!")
            return      
        
        
        # si un point est marqué
        if player2_score!=player2_old_score:
            reset_ball(player1_score, player2_score, ball_x, ball_y, ball_velocity_x, ball_velocity_y, difficulty, game_mode)
            break
        if player1_old_score!=player1_score:
            reset_ball(player1_score, player2_score, ball_x, ball_y, ball_velocity_x, ball_velocity_y, difficulty, game_mode)
            break
        

        
        
        
        #DO NOT TOUCH <--->

        # Affichage des raquettes, de la balle et des points dans la fenêtre du jeu 
        pygame.draw.rect(screen, WHITE, (0, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - PADDLE_WIDTH, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_SIZE)
        draw_center_line(screen)
        draw_text("PLAYER 1", SCREEN_WIDTH // 4, 18, WHITE, 28, screen)
        draw_text(str(player1_score), SCREEN_WIDTH // 4, 55, WHITE, 36, screen)
        draw_text("PLAYER 2", SCREEN_WIDTH * 3 // 4, 18, WHITE, 28, screen)
        draw_text(str(player2_score), SCREEN_WIDTH * 3 // 4, 55, WHITE, 36, screen)

        # Mise à jour de l'affichage
        pygame.display.flip()

        # Fréquence d'images
        clock.tick(60)
        

def reset_game():
    """
    Réinitialisation du jeu pour débuter une nouvelle partie
    """
    player1_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
    player2_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
    ball_x = SCREEN_WIDTH // 2
    ball_y = SCREEN_HEIGHT // 2
    ball_velocity_x = BALL_SPEED_X
    ball_velocity_y = BALL_SPEED_Y
    player1_score = 0
    player2_score = 0
    play_game(player1_y, player2_y, player1_score, player2_score, ball_x, ball_y, ball_velocity_x, ball_velocity_y)

def win(winner_message):
    """
    Affichage d'un message lorsqu'il y a un gagnant
    """
    screen.fill(BLACK)

    # Afficher le message du gagnant 
    draw_text(winner_message, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3, WHITE, 48, screen)
    draw_text("PRESS 'M' TO RETURN TO MAIN MENU", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, WHITE, 36, screen)

    # Mise à jour de l'affichage
    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    main_menu()  # Retour au menu principal
                    return
                if event.key == pygame.K_r:
                    reset_game()  # Réinitialisation du jeu
                    return


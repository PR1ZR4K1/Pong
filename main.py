"""
Project Name: Pong
Creator: Jaylon

We need:
    Ball Object (Sprite):
        That moves and bounces accordingly
        With a velocity that changes occasionally 
        update pos function


    Paddle Object (Sprite):
        For a player 1 and 2
        That are moved with 'w', 's' and up and down arrows
        move up and move down functions


    Other:
        Current Score (For the game being played)

"""

# This is where we access our other files, library (pygame), module (random)
import pygame
from src.Paddle import Paddle
from src.Constants import Constants
from src.Ball import Ball
from src.Text import Text
from random import randint

pygame.init()  # initializes pygame so we can use it
pygame.display.set_caption(Constants.CAPTION)

# This function literally draws the dotted line in the center of the program
# By drawing multiple lines individually and separating them by Constants.SPACE_LINES


def draw_center(surf, y_pos1, y_pos2):
    for i in range(15):
        pygame.draw.line(surf, Constants.BLACK, (Constants.CENTER_COORD, y_pos1),
                         (Constants.CENTER_COORD, y_pos2), (Constants.LINE_WIDTH))
        y_pos1 = y_pos2 + Constants.SPACE_LINES
        y_pos2 = y_pos1 + Constants.LENGTH_LINES


def main():

    running = True
    clock = pygame.time.Clock()
    # our surface is now called screen
    screen = pygame.display.set_mode(Constants.WINDOW_SIZE)
    # sprite group which can hold our sprites (moving objects)
    all_sprites_list = pygame.sprite.Group()

    # initializing variables
    y_pos1 = 0
    y_pos2 = 15
    player1_score = 0
    player2_score = 0

    # creating Text objects        the x coord
    player1_text = Text(
        "Player 1", 150, Constants.LENGTH_LINES, Constants.GAME_FONT)
    player2_text = Text(
        "Player 2", 450, Constants.LENGTH_LINES, Constants.GAME_FONT)
    game_over = Text(Constants.GAME_OVER, Constants.CENTER_COORD,
                     Constants.CENTER_COORD_Y/2, int(Constants.GAME_FONT*1.5))
    restart = Text(Constants.RESTART, Constants.CENTER_COORD,
                   Constants.CENTER_COORD_Y-20, int(Constants.GAME_FONT*1.5))

    # creating Paddle objects
    paddle1 = Paddle(Constants.BLACK, Constants.LINE_WIDTH *
                     2, Constants.PADDLE_HEIGHT)
    paddle1.rect.x = Constants.PADDLE1_X
    paddle1.rect.y = Constants.PADDLE_Y

    paddle2 = Paddle(Constants.BLACK, Constants.LINE_WIDTH *
                     2, Constants.PADDLE_HEIGHT)
    paddle2.rect.x = Constants.PADDLE2_X
    paddle2.rect.y = Constants.PADDLE_Y

    # creating ball object
    ball = Ball(Constants.BLACK, Constants.LINE_WIDTH*3, Constants.BALL_HEIGHT)
    ball.rect.x = Constants.CENTER_COORD
    ball.rect.y = Constants.CENTER_COORD_Y

    # here we add our sprites to the sprite group
    all_sprites_list.add(paddle1)
    all_sprites_list.add(paddle2)
    all_sprites_list.add(ball)

    while running:
        # color of our screen is white
        screen.fill(Constants.WHITE)
        draw_center(screen, y_pos1, y_pos2)
        # creating score holding text object
        player1_score_text = Text(
            str(player1_score), 150, Constants.SCORE_POS, Constants.GAME_FONT)
        player2_score_text = Text(
            str(player2_score), 450, Constants.SCORE_POS, Constants.GAME_FONT)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

                if event.key == pygame.K_r:
                    if player1_score == Constants.SCORE_TO_END or player2_score == Constants.SCORE_TO_END:
                        main()

        # Check if the ball is bouncing off top or bottom walls
        if ball.rect.y <= 0 or ball.rect.y >= 490:
            ball.velocity[1] = -ball.velocity[1]

        # Check if ball is hitting a paddle
        if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
            ball.bounce()

        # When the ball goes past either sides' paddles the ball resets to the middle
        # at some random point at the y axis and heads towards the player who scored
        if ball.rect.x > 600:
            player1_score += 1
            ball.reset(Constants.CENTER_COORD, False)
        if ball.rect.x < 0:
            player2_score += 1
            ball.reset(Constants.CENTER_COORD, True)

        # handle our paddles movement by adding and subtracting Constants.MOVE_PADDLE "7"
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.moveUp(Constants.MOVE_PADDLE)
        if keys[pygame.K_s]:
            paddle1.moveDown(Constants.MOVE_PADDLE)
        if keys[pygame.K_UP]:
            paddle2.moveUp(Constants.MOVE_PADDLE)
        if keys[pygame.K_DOWN]:
            paddle2.moveDown(Constants.MOVE_PADDLE)

        # Check if either player has won before redrawing our sprites
        if player1_score == Constants.SCORE_TO_END or player2_score == Constants.SCORE_TO_END:
            screen.blit(game_over.name, game_over.rect)
            screen.blit(restart.name, restart.rect)
            if player1_score > player2_score:
                winner = Text(Constants.PLAYER1_W, Constants.CENTER_COORD/2,
                              Constants.CENTER_COORD_Y+150, int(Constants.GAME_FONT*1.25))
                screen.blit(winner.name, winner.rect)
            else:
                winner = Text(Constants.PLAYER2_W, int(Constants.CENTER_COORD*1.5),
                              Constants.CENTER_COORD_Y+150, int(Constants.GAME_FONT*1.25))
                screen.blit(winner.name, winner.rect)
        else:
            # if no one has won yet we continue to update the sprites' positions and values
            all_sprites_list.update()
            all_sprites_list.draw(screen)
            # drawing "Player 1" and "Player 2"
            screen.blit(player1_text.name, player1_text.rect)
            screen.blit(player2_text.name, player2_text.rect)
            # drawing player 1 and 2's scores
            screen.blit(player1_score_text.name, player1_score_text.rect)
            screen.blit(player2_score_text.name, player2_score_text.rect)

        clock.tick(60)
        pygame.display.flip()


if __name__ == "__main__":
    main()

import pygame
from random import randint
from src.Constants import Constants
"""
The ball needs to move from left to right and up and down:
    Basically adding and subtracting numbers from the x and positions of our object
    So when we redraw the object it appears to be moving 
    We also need to handle when it hits one of our four walls in the program (The top and bottom and the two paddles):
        When the ball hits the top the y pos starts increasing n vice versa
    
        When the ball hits the left paddle the x pos increases n vice versa
    
    finally in main if it goes past the X values: 0 or 600 we give the points to the corresponding player

"""



class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

        
        # the ball moves by adding or subtracting the random numbers inside self.velocity 
        # from our ball's x and y-intercepts 
        # so, we make velocity a list to interact with the x and y from one location
        
        self.velocity = [randint(4, 6), randint(-7, 7)]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    # In the event that the ball hits a paddle we send it the opposite direction by making
    # velocity[0] or the ball's x coord to -velocity[0]
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-5, 5)
    
    def reset(self, x_pos, turn: bool):
        self.rect.x = x_pos
        self.rect.y = Constants.CENTER_COORD_Y + randint(-180, 180)
        self.turn = turn

        #when turn is true we send the ball to the winning side or in this case player1
        if self.turn:
            self.velocity[0] = randint(4,6)
        else: 
            self.velocity[0] = -randint(4,6)
import pygame

class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width: int, height: int):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    # we prevent the paddle from going out of bounds by resetting the y coord to the lowest or highest
    # y coord possible before heading off our screen
    def moveUp(self, pixels):
        # to move the paddle up the y coord is subtracted by a set integer in main and vice versa
        self.rect.y -= pixels
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 435:
          self.rect.y = 435
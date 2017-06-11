#Oakley S. Puc
#Period 5
#Final Project

import pygame

import constants
#We just imported the barebones tools now let's get down to business.
class SpriteSheet(object):
    
    sprite_sheet = None

    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()


    def get_image(self, x, y, width, height):
        #This will crop a section of the loaded sheet...
        image = pygame.Surface([width, height]).convert()

        #...and load it into a single sprite.
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        #The black background will be removed and it will be transparent
        image.set_colorkey(constants.BLACK)

        return image

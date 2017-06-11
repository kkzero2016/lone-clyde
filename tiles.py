#Oakley S. Puc
#Period 5
#Final Project

import pygame
import constants
from spritetools import SpriteSheet
DUMMY = (32, 0, 32, 32)
DUMY = (0, 0, 32, 32)
REDDOOR = (64, 0, 32, 32)
BLUEDOOR = (96, 0, 32, 32)
GOAL = (128, 0, 32, 64)
SPIKES = (160, 0, 32, 32)
class SolidTile(pygame.sprite.Sprite):#Basically, a platform

    def __init__(self, sprite_sheet_data):
        pygame.sprite.Sprite.__init__(self)

        sheet = SpriteSheet("bad_tile.png") #The image is grabbed
        self.image = sheet.get_image(sprite_sheet_data[0], #x value
                                           sprite_sheet_data[1], #y value
                                           sprite_sheet_data[2], #width
                                           sprite_sheet_data[3]) #height
        
        self.image.set_colorkey(constants.WHITE)                           
        self.rect = self.image.get_rect()
        #Rect is taken for collision detection later on
        
        
class Goal(pygame.sprite.Sprite): #The end of the level
    def __init__(self, sprite_sheet_data):
        pygame.sprite.Sprite.__init__(self)

        sheet = SpriteSheet("bad_tile.png")

        self.image = sheet.get_image(sprite_sheet_data[0], #x value
                                           sprite_sheet_data[1], #y value
                                           sprite_sheet_data[2], #width
                                           sprite_sheet_data[3]) #height

        self.type = self.image
        self.image.set_colorkey(constants.WHITE)                           
        self.rect = self.image.get_rect()

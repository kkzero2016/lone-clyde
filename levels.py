#Oakley S. Puc
#Period 5
#Final Project

import pygame
import constants
import tiles


class Level():

    platformList = None
    goalList = None

    background = None #Background image

    #How far scrolled

    xworldShift = 0
    yworldShift = 0
    scrollMax = -2000

    def __init__(self, player):
        #Set up lists and player
        self.platformList = pygame.sprite.Group()
        self.goalList = pygame.sprite.Group()
        self.player = player
        
        

    def update(self):
        #Update lists
        self.platformList.update()
        self.goalList.update()

    def draw(self, screen):
        #Prepare screen with the level's goodies
        screen.fill(constants.BLACK)
        screen.blit(self.background,(self.xworldShift - 500 // 3, self.yworldShift - 500// 3))

        self.platformList.draw(screen)
        self.goalList.draw(screen)

    def shift(self, xshift, yshift):
        #Shift the world if the player is going through the boundary
        self.xworldShift += xshift
        self.yworldShift += yshift

        for platform in self.platformList:
            platform.rect.x += xshift
            platform.rect.y += yshift

        for goalThing in self.goalList:
            goalThing.rect.x += xshift
            goalThing.rect.y += yshift

class TestLevel(Level):

    def __init__(self, player):

        Level.__init__(self, player)
        
        self.background = pygame.image.load("testbg.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500
        self.finishX = 1000
        self.finishY = 1000

        level = [ [tiles.DUMMY, 32, 40],
                  [tiles.SPIKES, 64, 40],
                  [tiles.DUMY, 100, 200],
                  [tiles.DUMY, 132, 200],
                  [tiles.DUMY, 164, 200],
                  [tiles.DUMY, 196, 200],
                  [tiles.DUMMY, 200, 40],
                  [tiles.DUMY, 68, 232],
                  [tiles.DUMY, 36, 264],
                  [tiles.DUMY, 228, 232],
                  [tiles.DUMY, 100, 360],
                  [tiles.DUMY, 132, 360],
                  [tiles.DUMY, 164, 360],
                  [tiles.DUMY, 196, 360],
                  [tiles.DUMY, 228, 360],
                  [tiles.DUMY, 68, 360],
                  [tiles.DUMY, -32, 360],
                  [tiles.DUMY, 0, 360],
                  [tiles.DUMY, 32, 360],
                  [tiles.DUMY, 260, 360],
                  [tiles.DUMY, 292, 360],
                  [tiles.DUMY, 324, 392],
                  [tiles.DUMY, 356, 424],
                  [tiles.DUMY, 388, 456],
                  
                  [tiles.DUMY, 574, 424],
                  [tiles.DUMY, 926, 392],
                  [tiles.DUMY, 958, 392],
                  [tiles.DUMY, 990, 392],
                  [tiles.REDDOOR, 1118, 424],
                  [tiles.BLUEDOOR, 1118, 232],
                  [tiles.REDDOOR, 1214, 232],
                  [tiles.REDDOOR, 1214, 264],
                  [tiles.REDDOOR, 1214, 296],
                  [tiles.REDDOOR, 1214, 328],
                  [tiles.REDDOOR, 1214, 360],
                  [tiles.DUMY, 1086, 262],
                  [tiles.DUMMY, 990, 424],
                  [tiles.DUMMY, 32, 936],
                  [tiles.DUMMY, 64, 936],
                  [tiles.DUMMY, 96, 936],
                  [tiles.DUMMY, -32, 1448],
                  [tiles.DUMMY, -128, 1448],
                  [tiles.DUMMY, -160, 1448],
                  [tiles.DUMMY, -256, 1448],
                  [tiles.DUMMY, 0, 1326],
                  ]

      

        for tile in level:
            block = tiles.SolidTile(tile[0])
            block.rect.x = tile[1] 
            block.rect.y = tile[2]
            block.mapX = tile[1]
            block.mapY = tile[2]
            block.player = self.player
            self.platformList.add(block)

class MainLevel(Level):

    def __init__(self, player):

        Level.__init__(self, player)
        #Prepare stuff like background and limit
        self.background = pygame.image.load("testbg.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500
        

        level = [ #Starting platform
                  [tiles.DUMY, -64, -128],
                  [tiles.DUMY, -32, -128],
                  [tiles.DUMY, 0, -128],
                  [tiles.DUMY, 32, -128],
                  
                  [tiles.DUMY, 64, -128],
                  [tiles.DUMY, 96, -128],
                  [tiles.DUMY, 128, -128],
                  #Long Wall at Starting Left
                  [tiles.DUMY, -64, -96],
                  [tiles.DUMY, -64, -64],
                  [tiles.DUMY, -64, -32],
                  [tiles.DUMY, -64, 0],
                  [tiles.DUMY, -64, 32],
                  [tiles.DUMY, -64, 64],
                  [tiles.DUMY, -64, 96],
                  #Tiles from first fall left
                  [tiles.DUMY, -96, 96],
                  [tiles.DUMY, -128, 96],
                  [tiles.DUMY, -192, 96],
                  [tiles.DUMY, -224, 96],
                  [tiles.DUMY, -256, 96],
                  [tiles.DUMY, -320, 96],
                  #Stairs from first fall left
                  [tiles.DUMY, -128, 640],
                  [tiles.DUMY, -96, 608],
                  [tiles.DUMY, -64, 576],
                  [tiles.DUMY, -32, 544],
                  [tiles.DUMY, 0, 512],
                  [tiles.DUMY, 32, 480],
                  [tiles.DUMY, 64, 448],
                  [tiles.DUMY, 96, 416],
                  [tiles.DUMY, 128, 384],
                  [tiles.DUMY, 160, 352],
                  #Platform after stairs from first fall left
                  [tiles.DUMY, 192, 352],
                  [tiles.DUMY, 224, 352],
                  [tiles.DUMY, 256, 352],
                  [tiles.DUMY, 288, 352],
                  [tiles.DUMY, 320, 352],
                  [tiles.DUMY, 352, 352],
                  [tiles.DUMY, 384, 352],
                  [tiles.DUMY, 416, 352],
                  [tiles.DUMY, 448, 352],
                  [tiles.DUMY, 480, 352],
                  #Long Wall at Starting Right
                  [tiles.DUMY, 128, -96],
                  [tiles.DUMY, 128, -64],
                  [tiles.DUMY, 128, -32],
                  [tiles.DUMY, 128, 0],
                  [tiles.DUMY, 128, 32],
                  [tiles.DUMY, 128, 64],
                  [tiles.DUMY, 128, 96],
                  #Tiles from first fall right
                  [tiles.DUMY, 160, 96],
                  [tiles.DUMY, 224, 96],
                  [tiles.DUMY, 544, 96],
                  [tiles.DUMY, 576, 96],
                  #Platform right below above tiles
                  [tiles.DUMY, 160, 256],
                  [tiles.DUMY, 192, 256],
                  [tiles.DUMY, 224, 256],
                  [tiles.DUMY, 256, 256],
                  [tiles.DUMY, 288, 256],
                  [tiles.DUMY, 320, 256],
                  [tiles.DUMY, 352, 256],
                  [tiles.DUMY, 384, 256],
                  [tiles.DUMY, 416, 256],
                  [tiles.DUMY, 448, 256],
                  [tiles.DUMY, 480, 288],
                  #Pillar blocking left start path and right tiles path
                  [tiles.DUMY, 96 , 96],
                  [tiles.DUMY, 96 , 128],
                  [tiles.DUMY, 96 , 160],
                  [tiles.DUMY, 96 , 192],
                  [tiles.DUMY, 128 , 224],
                  #Floor below first fall right
                  [tiles.DUMY, 160, 960],
                  [tiles.DUMY, 192, 960],
                  [tiles.DUMY, 224, 960],
                  [tiles.DUMY, 256, 960],
                  [tiles.DUMY, 288, 960],
                  [tiles.DUMY, 320, 960],
                  [tiles.DUMY, 352, 960],
                  [tiles.DUMY, 384, 960],
                  [tiles.DUMY, 416, 960],
                  [tiles.DUMY, 448, 960],
                  [tiles.DUMY, 480, 960],
                  [tiles.DUMY, 512, 960],
                  [tiles.DUMY, 544, 960],
                  [tiles.DUMY, 576, 960],
                  [tiles.DUMY, 608, 960],
                  [tiles.DUMY, 640, 960],
                  [tiles.DUMY, 672, 960],
                  [tiles.DUMY, 704, 960],
                  [tiles.DUMY, 736, 960],
                  [tiles.DUMY, 768, 960],
                  [tiles.DUMY, 800, 960],
                  [tiles.DUMY, 832, 960],
                  [tiles.DUMY, 864, 992],
                  #Path to the finish
                  [tiles.REDDOOR, 928, 994],
                  [tiles.REDDOOR, 864, 1058],
                  [tiles.REDDOOR, 832, 1058],
                  [tiles.REDDOOR, 800, 1058],
                  [tiles.REDDOOR, 768, 1058],
                  [tiles.REDDOOR, 736, 1058],
                  [tiles.REDDOOR, 704, 1058],
                  [tiles.REDDOOR, 672, 1058],
                  [tiles.REDDOOR, 640, 1058],
                  #Platforms leading back up
                  [tiles.DUMY, 160, 834],
                  [tiles.DUMY, 320, 740],
                  [tiles.DUMY, 32, 704],
                  [tiles.DUMY, 256, 602],
                  [tiles.DUMY, 480, 512],
                  [tiles.DUMY, 192, 512],
                  [tiles.DUMY, -96, 960],
                  [tiles.DUMY, -64, 704],
                  [tiles.DUMY, -128, 886],
                  [tiles.DUMY, -192, 822],
                  [tiles.DUMY, -288, 788],
                  ]

      

        for tile in level:
            #Get properties of each tile
            block = tiles.SolidTile(tile[0])
            
            #Place it on the map
            block.rect.x = tile[1] 
            block.rect.y = tile[2]
            
            block.player = self.player
            #And there it goes onto the list
            self.platformList.add(block)

        #Goal flag placement

        goalflag = [tiles.GOAL, 640, 994]

        goalblock = tiles.Goal(goalflag[0])
        goalblock.rect.x = goalflag[1]
        goalblock.rect.y = goalflag[2]
        goalblock.player = self.player
        self.goalList.add(goalblock)

        


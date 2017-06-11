#Oakley S. Puc
#Period 5
#Final Project

import pygame

import constants

import tiles
from spritetools import SpriteSheet
#Open the sound system
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
sndJump = pygame.mixer.Sound('jump.wav')
class Player(pygame.sprite.Sprite):

    #Speed of movement of the player for each value
    xvel = 0
    yvel = 0
    #Arrays holding sprite animations
    walkframesL = []
    walkframesR = []
    idleframesR = []
    idleframesL = []
    #direction to move in
    direction = "R"
  
    

    canJump = True #Checks if the player can jump or not
    level = None


    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("clydesheet.png")

        #Load all right-facing sprites to a list
        image = sprite_sheet.get_image(5, 4, 22, 27)
        self.idleframesR.append(image)
        image = sprite_sheet.get_image(37, 5, 22, 27)
        self.walkframesR.append(image)
        image = sprite_sheet.get_image(69, 4, 22, 27)
        self.walkframesR.append(image)

        #Do the same but now flip them to the left
        image = sprite_sheet.get_image(5, 4, 22, 27)
        image = pygame.transform.flip(image, True, False)
        self.idleframesL.append(image)
        image = sprite_sheet.get_image(37, 5, 22, 27)
        image = pygame.transform.flip(image, True, False)
        self.walkframesL.append(image)
        image = sprite_sheet.get_image(69, 4, 22, 27)
        image = pygame.transform.flip(image, True, False)
        self.walkframesL.append(image)

        self.image = self.idleframesR[0]
        
        self.rect = self.image.get_rect()

    def update(self):
        self.gravity()
        self.image.set_colorkey(constants.BLACK)
        
        self.rect.x += self.xvel #Position checking
        pos = self.rect.x + self.level.xworldShift
        
        if self.direction == "R":
            if self.yvel == 1 or self.yvel == 0:
                #Cycle through these frames if player is moving
                frame = (pos // 30) % len(self.walkframesR)
                self.image = self.walkframesR[frame]
            else:
                self.image = self.idleframesR[0]
        else:
            if self.yvel == 1 or self.yvel == 0:
                frame = (pos // 30) % len(self.walkframesL)
                self.image = self.walkframesL[frame]
            else:
                self.image = self.idleframesL[0]
        
        tileHit = pygame.sprite.spritecollide(self, self.level.platformList, False)
        for tile in tileHit:
            #We collided. WHich isde are we on? Move the opposite direction of where we hit.
            
            if self.xvel > 0:
                self.rect.right = tile.rect.left
            elif self.xvel < 0:
                self.rect.left = tile.rect.right

           

            
                
        self.rect.y += self.yvel

        

        tileHit = pygame.sprite.spritecollide(self, self.level.platformList, False)
        for tile in tileHit:
            
            if self.yvel > 0:
                self.rect.bottom = tile.rect.top
                self.canJump = True
            elif self.yvel < 0:
                self.rect.top = tile.rect.bottom

            
            

            self.yvel = 0

        

    def gravity(self):
        #Check if not touching ground and bring em down if so.
        if self.yvel == 0:
            self.yvel = 1
        else:
            self.yvel += 0.35
        self.canJump = False

        

    def jump(self):
        #Jump if it's possible
        if self.canJump:
            sndJump.play()
            self.rect.y += 2
            hitPlatforms = pygame.sprite.spritecollide(self, self.level.platformList, False)
            self.rect.y -= 2
            self.yvel = -10
            self.canJump = False
        
                
    #Horizontal Movement
    def go_left(self):
        #Move left
        
        self.xvel = -6
        self.direction = "L"

    def go_right(self):
        #Move right
        
        self.xvel = 6
        self.direction = "R"

    def stop(self):
        #Cease all movement
        
        self.xvel = 0

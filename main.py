#Oakley S. Puc
#Period 5
#Final Project

#So, we gotta import everything
import pygame, random, sys

from pygame.locals import *
from constants import *
from player import Player
from tiles import SolidTile

from spritetools import SpriteSheet
import levels

#This is a comment. I am helping!

print("\nCreated in 2017 by kkzero Interactive")
print("\nBuilt off from an example on programarcadegames.com")

#Below loads the sound mixer. Frequency is at CD Quality, the only
#setting different than without putting anything in the init
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
#creates sounds
sndTitle = pygame.mixer.Sound('loneclydetitle.wav')
sndGoal = pygame.mixer.Sound('clydewin.wav')

#Below is the 'scale' variable. It upscales the screen resolution by
#whatever value it has. 1 keeps it at the smallest resolution, 320x240.

scale = 3


    
def main():
    pygame.init()
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
    #pygame.display.set_icon(pygame.image.load('windowicon.png'))
    size = (SCREEN_WIDTH * scale, SCREEN_HEIGHT * scale)
    dispScreen = pygame.display.set_mode(size)
    screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Lone Clyde")
    #Create the player in the game
    player = Player()

    #Sort out levels
    levelList = []
    levelList.append(levels.MainLevel(player))

    #sets level properties
    currentLevelNo = 0
    currentLevel = levelList[currentLevelNo]

    
    
    
    #Setting up sprites
    activeSprites = pygame.sprite.Group()
    player.level = currentLevel

    
    #Sets variable to track frame rate
    clock = pygame.time.Clock()

    #Sets up sprites & images
    player.rect.x = 148
    player.rect.y = -160
    activeSprites.add(player)
    titleScreen = pygame.image.load('title.png').convert()
    stageClear = pygame.image.load('stageclear.png').convert()
    onTitle = True
    #Title Screen Loop
    sndTitle.play()
    while onTitle:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                done = True
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                #Waits for key input. If i is pressed, instructions
                #will show. If Space is pressed, game will commence.
                if event.key == pygame.K_SPACE:
                    onTitle = False
                elif event.key == pygame.K_i:
                    titleScreen = pygame.image.load('howtoplay.png').convert()
            #sets display up for main game
            screen.fill(BLACK)
            screen.blit(titleScreen, (0, 0))
            dispScreen.blit(pygame.transform.scale(screen, (SCREEN_WIDTH * scale, SCREEN_HEIGHT * scale)), dest = (0, 0))
            pygame.display.update()
            clock.tick(60)
        
    #Main Game Loop  
    done = False
    sndTitle.stop()
    while not done:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                done = True
                pygame.quit()
                sys.exit()
            #Player controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.xvel < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.xvel > 0:
                    player.stop()

        #Update sprites & level
        activeSprites.update()
        currentLevel.update()
        
        #Scroll detection
        if player.rect.x >= 180:
            diff = player.rect.x - 180
            player.rect.x = 180
            currentLevel.shift(-diff, False)


        if player.rect.x <= 122:
            diff = 122 - player.rect.x
            player.rect.x = 122
            currentLevel.shift(diff, False)


        if player.rect.y >= 128:
            vdiff = 128 - player.rect.y
            player.rect.y = 128
            currentLevel.shift(False, vdiff)

        if player.rect.y <= 96:
            vdiff = player.rect.y - 96
            player.rect.y = 96
            currentLevel.shift(False, -vdiff)
        #Check if goal is touched
        touchGoal = pygame.sprite.spritecollide(player, currentLevel.goalList, False)
        if touchGoal:
            done = True
            

        
        #updating display
        currentLevel.draw(screen)
        activeSprites.draw(screen)
        #Scales small display to bigger frame
        dispScreen.blit(pygame.transform.scale(screen, (SCREEN_WIDTH * scale, SCREEN_HEIGHT * scale)), dest = (0, 0))
        pygame.display.update()
        clock.tick(60)
    #Stage clear loop
    goalSoundDone = False
    while not goalSoundDone:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                goalSoundDone = True
                pygame.quit()
                pygame.mixer.quit()
                sys.exit()
        screen.blit(stageClear, (0, 0))
        dispScreen.blit(pygame.transform.scale(screen, (SCREEN_WIDTH * scale, SCREEN_HEIGHT * scale)), dest = (0, 0))
        pygame.display.update()
        sndGoal.play()
        
        
    pygame.quit()

if __name__ == "__main__":
    main()




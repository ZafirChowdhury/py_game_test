import sys

import pygame

pygame.init() 

window = pygame.display.set_mode((640, 480)) # insilizing window and seeting resolution

clock = pygame.time.Clock() # can be used to limit fps

while True:
    events = pygame.event.get() # all the events
    for event in events:
        if event.type == pygame.QUIT: # user clicks "X" in the window
            pygame.quit()   # quiting pygame
            sys.exit()  #quiting the program

    pygame.display.update() # updating the display
    clock.tick(60)  # seting the fps to 60

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    my_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        
        for item in updatable:
            item.update(dt)

        for item in drawable:
            item.draw(screen)
        
        #my_player.draw(screen)
        #my_player.update(dt)
        pygame.display.flip()
        dt = (clock.tick(60)/1000)

        #Prints FPS
        #print(1/dt)

if __name__ == "__main__":
    main()
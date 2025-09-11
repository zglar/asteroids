import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()

    #Starting text prompt
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Set screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Set clock
    clock = pygame.time.Clock()
    dt = 0

    #Add player
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    updatable = [player]
    drawable = [player]

    #Initializing game setup
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Update player
        for obj in updatable:
            obj.update(dt)

        #Fill Screen
        screen.fill((0, 0, 0))
        
        #Draw player
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #Cap FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

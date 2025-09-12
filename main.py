import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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

    #Grouping
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #Create objects
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    #Initializing game setup
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Update objects
        for obj in updatable:
            obj.update(dt)

        #Collision check
        for rock in asteroids.sprites():
            if player.collision_check(rock):
                print("Game over!")
                pygame.quit()
                sys.exit()

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

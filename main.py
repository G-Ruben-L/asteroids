import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Get key states
        keys = pygame.key.get_pressed()

        # Handle player input
        if keys[pygame.K_SPACE] and player.timer <= 0:
            new_shot = player.shoot()
            shots.add(new_shot)
            player.timer = PLAYER_SHOOT_COOLDOWN

        screen.fill("black")
        updatable.update(dt)

        # Shot killing asteroid block
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.kill()

        # Collision detection block
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                return

        for flying_saucer in drawable:
            flying_saucer.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()


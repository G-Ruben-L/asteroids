from circleshape import *
import pygame
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
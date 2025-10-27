import pygame
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def collision(self, object_position):
        distance = self.position.distance_to(object_position)
        return distance < (self.radius + 25)  # Assuming player radius is 25
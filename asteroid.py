import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            asteroid_split_radius = self.radius - ASTEROID_MIN_RADIUS
            split_vector1 = self.velocity.rotate(rand_angle)
            split_vector2 = self.velocity.rotate(-rand_angle)
            split_asteroid1 = Asteroid(self.position.x, self.position.y, asteroid_split_radius)
            split_asteroid2 = Asteroid(self.position.x, self.position.y, asteroid_split_radius)
            split_asteroid1.velocity = split_vector1 * 1.2
            split_asteroid2.velocity = split_vector2 * 1.2

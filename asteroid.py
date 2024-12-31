import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        self.kill()

        random_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)

        new_radius_small = self.radius - ASTEROID_MIN_RADIUS

        small_1 = Asteroid(self.position.x, self.position.y, new_radius_small)
        small_2 = Asteroid(self.position.x, self.position.y, new_radius_small)

        small_1.velocity = vector1 * 1.2
        small_2.velocity = vector2 * 1.2

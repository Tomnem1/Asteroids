import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_KINDS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        asteroid_sprite = pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            log_event("asteroid_split")

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            
            split_angle = random.uniform(20, 50)
            velocity_split_1 = self.velocity.rotate(split_angle)
            velocity_split_2 = self.velocity.rotate(-split_angle)

            asteroid1.velocity = velocity_split_1 * 1.2
            asteroid2.velocity = velocity_split_2 * 1.2
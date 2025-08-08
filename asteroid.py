import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):

    def draw(self, screen):
        pygame.draw.circle(x, y, radius, 2)
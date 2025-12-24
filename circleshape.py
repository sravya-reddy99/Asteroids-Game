from typing import ClassVar, Iterable
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: ClassVar[Iterable[pygame.sprite.AbstractGroup]]
    def __init__(self, x, y, radius):
        # we will be using this later
        containers = getattr(self, "containers", None)
        if containers:
            super().__init__(*containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass
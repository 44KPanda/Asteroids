import pygame
from circleshape import *
from constants import *
from shot import *
#from main import *
class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group
    # in the player class

    def shoot(self):
        #print("Shoot method called!")
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shots_group.add(shot)
        #print(f"Shot created at {self.position}, velocity: {shot.velocity}")
        #print(f"Shots group size: {len(self.shots_group)}")

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    def rotate(self, dt):
        self.rotation = (PLAYER_TURN_SPEED * dt) + self.rotation
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)  
        if keys[pygame.K_s]:
            self.move(-dt)  
        if keys[pygame.K_SPACE]:
            #print("SPACE pressed!")
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
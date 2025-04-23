import pygame
from constants import *
from circleshape import *
import random

#pygame.mixer.pre_init(48000, -16, 1, 1024) 
#pygame.init()
#pygame.mixer.init(44100, -16, 2, 2048)
pygame.mixer.init()

#pygame.mixer.music.load(filename)
#pygame.mixer.music.play()
#try:
#    pygame.mixer.init()
 #   sound_available = True
#except pygame.error:
 #   sound_available = False
  #  print("Sound disabled: No audio device available")
sound = pygame.mixer.Sound('explosion_sound.wav')

#/*
#def play(filename):
#    # test this
 #   pygame.mixer.init(frequency=16000)
  #  pygame.mixer.music.load(filename)
   # pygame.mixer.music.play()
    #sound = pygame.mixer.Sound('explosion_sound.wav')

    

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        #These are already set in the parent class CircleShape
        #self.position = pygame.Vector2(x, y)
        #self.velocity = pygame.Vector2(0, 0)
        #self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        sound.play()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        blue_angle = random.uniform(20, 50)
        new_angle_1 = self.velocity.rotate(blue_angle)
        new_angle_2 = self.velocity.rotate(-blue_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_angle_1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_angle_2 * 1.2

    def update(self, dt):
        # sub-classes must override
        self.position += (self.velocity * dt)
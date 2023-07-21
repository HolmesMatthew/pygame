import pygame
from settings import *
from support import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0

        # gen setup

        # self.image = pygame.Surface((32, 64))
        # self.image.fill('green')
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        # movements attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def import_assets(self):
        self.animations = {
            'up': [], 'down': [], 'left': [], 'right': [], 'right_idle': [], 'left_idle': [], 'up_idle': [],
            'down_idle': [], 'left_hoe': [], 'up_hoe': [], 'down _hoe': [], 'right_axe': [], 'right_hoe': [],
            'left_axe': [], 'up_axe': [], 'down_axe': [], 'right_water': [], 'left_water': [], 'up_water': [],
            'down_water': []
        }
        for animation in self.animations.keys():
            full_path = 'dewvally_imports/s2-basic player/graphics/character/' + animation
            # full_path = '../graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self, dt):
        self.frame_index += 4*dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]
        # self.animations[down folder][image frame]

    def input(self):
        keys = pygame.key.get_pressed()
        # vertical
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        # horizontal
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'

    def get_status(self):
        # if the player is not moving
        if self.direction.magnitude() > 0:
            self.status = self.status.split('_')[0] + '_idle'
        # add _idle to status

    def move(self, dt):

        # normalizing a vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        # horizontal
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        # vertical
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.get_status()
        self.move(dt)
        self.animate(dt)

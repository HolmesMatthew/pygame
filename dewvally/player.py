import pygame
from settings import *
from support import *
from timer import Timer


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

        # timers
        self.timers = {
            'tool use': Timer(350, self.use_tool),
            'tool switch': Timer(200)
        }

        # tools
        self.tools = ['hoe', 'axe', 'water']
        self.tool_index = 0
        self.selected_tool = self.tools[self.tool_index]

    def use_tool(self):
        print('use tool')

    def import_assets(self):

        self.animations = {
            'up': [], 'down': [], 'left': [], 'right': [], 'right_idle': [], 'left_idle': [], 'up_idle': [],
            'down_idle': [], 'left_hoe': [], 'up_hoe': [], 'down_hoe': [], 'right_axe': [], 'right_hoe': [],
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
        tool_use_active = self.timers['tool use'].active
        tool_switch_active = self.timers['tool switch'].active

        if not tool_use_active:
            # directions
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

            # tool use
            if keys[pygame.K_SPACE]:
                # timer for tool use after timer is done player should end animation
                self.timers['tool use'].activate()
                if self.timers['tool use'].active:
                    print('activated')
                self.direction = pygame.math.Vector2()
                self.frame_index = 1
                    # self.direction = pygame.Vector2()

        

            # else:
            #     if not keys[pygame.K_SPACE]:
            #         self.timers['tool use'].deactivate()
            # change tool
            # if keys[pygame.K_q] and not self.timers['tool switch'].active:
            if keys[pygame.K_q] and not tool_switch_active:
                self.timers['tool switch'].activate()
                self.tool_index += 1
                self.tool_index = self.tool_index if self.tool_index < len(
                    self.tools) else 0

                self.selected_tool = self.tools[self.tool_index]
        # Tests that pressing the space key activates the tool use timer, sets direction and frame index to 0, and stops the tool usage timer

    def get_status(self):
        # idle
        if self.direction.magnitude() > 0:
            self.status = self.status.split('_')[0] + '_idle'
            

        # tool use
        elif self.timers['tool use'].active:

            # self.status = 'right_axe'
            self.status = self.status.split('_')[0] + '_' + self.selected_tool
        # else:
        #     self.status = self.status.split('_')[0] + '_idle'


    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

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
        self.update_timers()
        self.move(dt)
        self.animate(dt)
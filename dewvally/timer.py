import pygame


class Timer:
    def __init__(self, duration, func=None):
        self.duration = duration
        self.func = func
        self.start_time = 0
        self.active = False
        self.not_active = True
    def activate(self):
        self.active = True
        self.not_active = False
        # print(self.not_active)
        self.start_time = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.not_active = True
        # print(self.not_active)
        self.start_time = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        # var = current_time - self.start_time
        # if self.active:
        # print(var)
        if current_time - self.start_time >= self.duration and self.start_time > 0:
            # if current_time - self.start_time >= self.duration:
            # print('update', current_time, self.start_time)
            # print('math', current_time - self.start_time)

            self.deactivate()
            print(self.not_active, 'not active')
            if self.func:
                self.func()

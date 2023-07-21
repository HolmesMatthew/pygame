import pygame
from sys import exit  # closes any code
from random import randint, choice


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load(
            'graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load(
            'graphics/player/player_walk_2.png').convert_alpha()
        self.player_jump = pygame.image.load(
            'graphics/player/jump.png').convert_alpha()

        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.image = self.player_walk[self.player_index]
        # self.image
        self. rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(.3)

    def player_input(self):
        keys = pygame.key.get_pressed()  # get key method will affect speed
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


class Obstacle(pygame.sprite.Sprite):
    # required
    # def __init__(self, type):
    #     super().__init__()
    #     self.image
    #     self.rect
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load(
                'graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load(
                'graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(
            midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f"{current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    return current_time


# def obstacle_movement(obstacle_list):
#     if obstacle_list:  # checking for empty list
#         for obstacle_rect in obstacle_list:
#             obstacle_rect.x -= 5
#             if obstacle_rect.bottom == 300:
#                 screen.blit(snail_surface, obstacle_rect)
#             else:
#                 screen.blit(fly_surface, obstacle_rect)
#         #
#         # Copy current list
#         # delete if off screen
#         obstacle_list = [
#             obstacle for obstacle in obstacle_list if obstacle.x > -100]
#         return obstacle_list
#     else:
    # return []


# def collisions(player, obstacles):
#     if obstacles:
#         for obstacle_rect in obstacles:
#             if player.colliderect(obstacle_rect):
#                 return False
#     return True
def collisions_sprite():
    # pygame.sprite.spritecollide(sprite, group, bool)

    # player.sprite only works with GroupSingle()
    # on true sprite is deleted
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True


# def player_animation():
#     # play walking if player is on the floor
#     # play jumping animation if player is not
#     global player_surface, player_index
#     if player_rect.bottom < 300:
#         # jump
#         player_surface = player_jump
#     else:
#         # walk
#         player_index += 0.1
#         if player_index >= len(player_walk):
#             player_index = 0
#         player_surface = player_walk[int(player_index)]


pygame.init()  # starts pygame
# screen = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((800, 400))  # display surface
pygame.display.set_caption('G-One')  # title
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(.6)
bg_music.play(loops=-1)


# groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()


# test_surface = pygame.Surface((w, h))
# test_surface = pygame.Surface((100, 200))  # surface
# test_surface.fill('Red')
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert()

# score_surface = test_font.render('My game', False, (64, 64, 64))
# score_rect = score_surface.get_rect(center=(400, 50))

# -----obstacles-----
# --Snail--

# snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
# snail_frames = [snail_frame_1, snail_frame_2]
# snail_frame_index = 0
# snail_surface = snail_frames[snail_frame_index]
# snail_x_pos = 600
# snail_rect = snail_surface.get_rect(midbottom=(600, 300))

# --Fly--
# fly_surface = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
# fly_frame_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
# fly_frame_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
# fly_frames = [fly_frame_1, fly_frame_2]
# fly_frame_index = 0
# fly_surface = fly_frames[fly_frame_index]

# obstacle_rect_list = []

# --Player--
# player_walk_1 = pygame.image.load(
#     'graphics/player/player_walk_1.png').convert_alpha()
# player_walk_2 = pygame.image.load(
#     'graphics/player/player_walk_2.png').convert_alpha()
# player_walk = [player_walk_1, player_walk_2]
# player_index = 0
# player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

# player_surface = player_walk[player_index]
# # player_rect= pygame.Rect(left,top,width,height)
# player_rect = player_surface.get_rect(midbottom=(80, 300))
# player_gravity = 0


# -----intro screen-----
game_name = test_font.render('Game one', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

player_stand = pygame.image.load(
    'graphics/player/player_stand.png').convert_alpha()
# player_stand = pygame.transform.scale2x(player_stand)
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 320))


# -----timer-----
# add +1 to avoid collfliction with pygaME
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)
# --------------------------------------------------------------------------------------------------------------


# -----game loop-----
while True:
    # close game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # close code entirely
        if game_active:
            test = 0
            # if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom == 300:
            #     if player_rect.collidepoint(event.pos):
            #         player_gravity = -20

            # if event.type == pygame.KEYDOWN and player_rect.bottom == 300:
            #     if event.key == pygame.K_SPACE:
            #         player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                # snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

    # -----draw all out elements-----
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(
                    Obstacle(choice(['fly', 'fly', 'snail', 'snail', 'snail', ])))
                # if randint(0, 2):  # create true or false statement
                #     obstacle_rect_list.append(
                #         snail_surface.get_rect(bottomright=(randint(900, 1100), 300)))
                # else:
                #     obstacle_rect_list.append(fly_surface.get_rect(
                #         bottomright=(randint(900, 1100), 210)))
            # if event.type == snail_animation_timer:
            #     if snail_frame_index == 0:
            #         snail_frame_index = 1
            #     else:
            #         snail_frame_index = 0
            #     snail_surface = snail_frames[snail_frame_index]
            # if event.type == fly_animation_timer:
            #     if fly_frame_index == 0:
            #         fly_frame_index = 1
            #     else:
            #         fly_frame_index = 0
            #     fly_surface = fly_frames[fly_frame_index]
    if game_active:        # screen.blip((surface,pos))
        # (0,0) = origin point /top-left. increase y=moves down and increase x= moves right, x, y)
        # screen.blit(test_surface, ((200, 100))
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        score = display_score()

        # pygame.draw.line(screen, 'gold', (0, 0), pygame.mouse.get_pos(), 10)
        # pygame.draw.ellipse(screen,'brown', pygame.rect(left,top,width,height))

        # screen.blit(score_surface, score_rect)
        # snail_x_pos -= 4
        # if snail_x_pos < -100:
        #     snail_x_pos = 800
        # screen.blit(snail_surface, (snail_x_pos, 250))
        # screen.blit(snail_surface, snail_rect)

        # snail_rect.x -= 4
        # if snail_rect.right <= 0:
        #     snail_rect.left = 800
        # print(player_rect.left) #48

        # -----player-----
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 300:
        #     player_rect.bottom = 300
        # player_animation()
        # screen.blit(player_surface, player_rect)
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()
        # -----obstacle movement-----
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # -----collision-----
        game_active = collisions_sprite()
        # game_active = collisions(player_rect, obstacle_rect_list)
        # if snail_rect.colliderect(player_rect):
        #     game_active = False

        # if keys[pygame.K_SPACE]:
        #     print("jump")
        # print(player_rect.colliderect(snail_rect))
        # if player_rect.colliderect(snail_rect) == True:
        #     print('dead')
        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     print(pygame.mouse.get_pressed())
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        score_message = test_font.render(
            f"Your score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))
        screen.blit(game_name, game_name_rect)
        # obstacle_rect_list.clear()
        # player_rect.midbottom = (80, 300)
        player_gravity = 0
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
        #  -----update everything-----
    pygame.display.update()  # updates screen = pygame.display
    clock.tick(60)  # game should not run more than 60 times per second


"""
            ---NOTES---

ceiling- easy to tell the computer to pause between frames
floor- really hard to get a computer to run faster, you need to change the game tyo ensure it runs well

surface:
    display surface- the game window. Anything displayed goes on here
    (regular)surface- essentially a single image(something imported, rendered text or plain color) needs to bve put on display surface

rectangle:
    points-
        (x,y), top, bottom, left, right, centerx, centery
        (top,left), (mid,top), (top, right), (mid,right)...ect
Sprite class
    - A class that contains a surface and a rectangle; and it can be drawn and updated very easily
"""

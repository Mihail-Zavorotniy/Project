import pygame
from constants import *

class Player:
    def __init__(self, x, y, screen: pygame.Surface):
        '''Параметры игрока
                х - положение по оси х
                у - положение по оси у
                v - базовая скорость
                move - показывает, двигается ли игрок вверх, вправо, вниз, влево'''
        self.x = x
        self.y = y
        self.v = 0.5
        self.screen = screen
        self.move = {'up': False, 'down': False, 'right': False, 'left': False}

    def does_player_move(self, event):
        '''Изменение данных кортежа move рпи зажимании клавиш-стрелок пользователем'''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.move['left'] = True
            elif event.key == pygame.K_d:
                player.move['right'] = True
            elif event.key == pygame.K_w:
                player.move['up'] = True
            elif event.key == pygame.K_s:
                player.move['down'] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.move['left'] = False
            elif event.key == pygame.K_d:
                player.move['right'] = False
            elif event.key == pygame.K_w:
                player.move['up'] = False
            elif event.key == pygame.K_s:
                player.move['down'] = False

    def move_player(self):
        '''Изменяет координаты игрока, если зажаты клавиши движения'''
        if self.move['right']:
            self.x += self.v
        if self.move['left']:
            self.x -= self.v
        if self.move['up']:
            self.y -= self.v
        if self.move['down']:
            self.y += self.v

    def draw_player(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 20)


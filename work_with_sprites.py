import pygame
import os.path
from visuals import *
from constants import *

all_sprites = {'starting_background': None,
               'inventory_bar': None,
               'empty_slot': None,
               'mushroom': None,
               'window': None
               }

player_sprites = {'down': None, 'down1': None, 'down2': None, 'down3': None, 'down4': None, 'down5': None, 'down6': None,
                  'right': None, 'right1': None, 'right2': None, 'right3': None, 'right4': None, 'right5': None, 'right6': None,
                  'up': None, 'up1': None, 'up2': None, 'up3': None, 'up4': None, 'up5': None, 'up6': None,
                  'left': None, 'left1': None, 'left2': None, 'left3': None, 'left4': None, 'left5': None, 'left6': None
                  }

def fill_sprites():
    for key in all_sprites.keys():
        file_name = key + '.png'
        all_sprites[key] = pygame.image.load(os.path.join('sprites', file_name)).convert()
        all_sprites[key].set_colorkey((0xFFFFFF))
    for key in player_sprites.keys():
        file_name = 'player_' + key + '.png'
        player_sprites[key] = pygame.image.load(os.path.join('sprites', file_name)).convert()
        player_sprites[key].set_colorkey((0xFFFFFF))

fill_sprites()

'''Создание одного бэкграунда'''

obj1 = Object(screen, [all_sprites['window']], [200, 30],
              [[all_sprites['window'].get_width(), all_sprites['window'].get_height() / 8]])

inter_obj = None
inter_list = []
for i in range(1, 10):
    inter_obj = ObjectInteractable(screen, [all_sprites['mushroom']], [i*100, 550],
                  [[all_sprites['mushroom'].get_width(), all_sprites['mushroom'].get_height()/i]], True)
    inter_list.append(inter_obj)

bg1 = Background(screen, all_sprites['starting_background'], [obj1], inter_list)
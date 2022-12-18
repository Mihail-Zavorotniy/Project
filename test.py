import os.path
from constants import *
from keyboard import *
from player import *
from visuals import *
from inventory_and_menu import *
from managers import *

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
    for key in player_sprites.keys():
        file_name = 'player_' + key + '.png'
        player_sprites[key] = pygame.image.load(os.path.join('sprites', file_name)).convert()


fill_sprites()
all_sprites['mushroom'].set_colorkey((0xFFFFFF))
for key in player_sprites.keys():
    player_sprites[key].set_colorkey((0xFFFFFF))

inventory = Inventory(screen, [0, 100], all_sprites['inventory_bar'], 9, 7, all_sprites['empty_slot'])

player = Player(screen, player_sprites, player_starting_coord, 8,
                [player_sprites['down'].get_width() / 2, player_sprites['down'].get_height() / 16])

obj1 = Object(screen, [all_sprites['mushroom']], [200, 500],
              [[all_sprites['mushroom'].get_width(), all_sprites['mushroom'].get_height() / 8]])

obj2 = Object(screen, [all_sprites['mushroom']], [100, 200],
              [[all_sprites['mushroom'].get_width(), all_sprites['mushroom'].get_height() / 16]])

obj3 = Object(screen, [all_sprites['mushroom']], [300, 300],
              [[all_sprites['mushroom'].get_width(), all_sprites['mushroom'].get_height() / 32]])

inter_obj = None
inter_list = []
for i in range(1, 10):
    inter_obj = ObjectInteractable(screen, [all_sprites['mushroom']], [i*100, 550],
                  [[all_sprites['mushroom'].get_width(), all_sprites['mushroom'].get_height()/i]], True)
    inter_list.append(inter_obj)

bg1 = Background(screen, all_sprites['starting_background'], [obj1, obj2, obj3], inter_list)

bg_manager = BackgroundManager([bg1], 0)

while not finished:
    finished = input_handler(inventory, player, bg_manager)
    check_collisions(player, bg_manager)
    bg_manager.draw_scenery(player)
    inventory.draw()
    pygame.display.update()
    clock.tick(FPS)
    keyboard.update()

pygame.quit()

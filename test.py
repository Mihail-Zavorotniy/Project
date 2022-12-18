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
               'player': None
               }

player_sprites = {'down1': None, 'down2': None, 'down3': None, 'down4': None, 'down5': None, 'down6': None,
                  'right1': None, 'right2': None, 'right3': None, 'right4': None, 'right5': None, 'right6': None,
                  'up1': None, 'up2': None, 'up3': None, 'up4': None, 'up5': None, 'up6': None,
                  'left1': None, 'left2': None, 'left3': None, 'left4': None, 'left5': None, 'left6': None
                  }

def fill_sprites():
    for key in all_sprites.keys():
        file_name = key + '.png'
        all_sprites[key] = pygame.image.load(os.path.join('sprites', file_name)).convert()
    for key in player_sprites.keys():
        file_name = 'player_' + key + '.png'
        player_sprites[key] = pygame.image.load(os.path.join('sprites', file_name)).convert()


def check_interaction():
    interacted = False
    for obj in bg_manager.current_bg.interactable_objects:
            if ((abs(player.hitbox_x - obj.hitbox_x) <= (player.hitbox_width + obj.hitbox_width)/2 + obj.inter_area) and
                (abs(player.hitbox_y - obj.hitbox_y) <= (player.hitbox_height + obj.hitbox_height)/2 + obj.inter_area)):
                print(obj.pickup)
                interacted = True
                if obj.pickup:
                    inventory.add_item(obj)
                    bg_manager.current_bg.interactable_objects.remove(obj)
                    bg_manager.current_bg.all_objects.remove(obj)
            if interacted:
                break



def input_handler():
    global finished
    if keyboard.key_pressed['quit'][1]:
        finished = True
    else:
        if keyboard.key_pressed['q'][1]:
            inventory.active = True
            player.immobile = True
        elif keyboard.key_pressed['e'][1]:
            inventory.active = False
            player.immobile = False
        if keyboard.key_pressed['f'][1] and not keyboard.key_pressed['f'][0]:
            check_interaction()
        if inventory.active:
            if keyboard.key_pressed['w'][1] and not keyboard.key_pressed['w'][0]:
                inventory.selected_up()
            elif keyboard.key_pressed['s'][1] and not keyboard.key_pressed['s'][0]:
                inventory.selected_down()
        elif not player.immobile:
            if keyboard.key_pressed['w'][1] and keyboard.key_pressed['d'][1]:
                player.move('u', 2 ** (1 / 2))
                player.move('r', 2 ** (1 / 2))
            elif keyboard.key_pressed['w'][1] and keyboard.key_pressed['a'][1]:
                player.move('u', 2 ** (1 / 2))
                player.move('l', 2 ** (1 / 2))
            elif keyboard.key_pressed['s'][1] and keyboard.key_pressed['d'][1]:
                player.move('d', 2 ** (1 / 2))
                player.move('r', 2 ** (1 / 2))
            elif keyboard.key_pressed['s'][1] and keyboard.key_pressed['a'][1]:
                player.move('d', 2 ** (1 / 2))
                player.move('l', 2 ** (1 / 2))
            else:
                if keyboard.key_pressed['w'][1]:
                    player.move('u')
                if keyboard.key_pressed['a'][1]:
                    player.move('l')
                if keyboard.key_pressed['s'][1]:
                    player.move('d')
                if keyboard.key_pressed['d'][1]:
                    player.move('r')


def check_collisions():
    if player.hitbox_x - player.hitbox_width / 2 < left_barrier:
        player.hitbox_x = left_barrier + player.hitbox_width / 2
    if player.hitbox_x + player.hitbox_width / 2 > right_barrier:
        player.hitbox_x = right_barrier - player.hitbox_width / 2
    if player.hitbox_y - player.hitbox_height / 2 < top_barrier:
        player.hitbox_y = top_barrier + player.hitbox_height / 2
    if player.hitbox_y + player.hitbox_height / 2 > bottom_barrier:
        player.hitbox_y = bottom_barrier - player.hitbox_height / 2

    for obj in bg_manager.current_bg.all_objects:
        if (abs(player.hitbox_x - obj.hitbox_x) < (player.hitbox_width + obj.hitbox_width) / 2 and
                abs(player.hitbox_y - obj.hitbox_y) < (player.hitbox_height + obj.hitbox_height) / 2):
            if ((player.hitbox_width + obj.hitbox_width) / 2 - abs(player.hitbox_x - obj.hitbox_x) <
                    (player.hitbox_height + obj.hitbox_height) / 2 - abs(player.hitbox_y - obj.hitbox_y)):
                if player.prev_hitbox_x > obj.hitbox_x:
                    player.hitbox_x = obj.hitbox_x + (player.hitbox_width + obj.hitbox_width) / 2
                else:
                    player.hitbox_x = obj.hitbox_x - (player.hitbox_width + obj.hitbox_width) / 2
            elif ((player.hitbox_width + obj.hitbox_width) / 2 - abs(player.hitbox_x - obj.hitbox_x) >
                  (player.hitbox_height + obj.hitbox_height) / 2 - abs(player.hitbox_y - obj.hitbox_y)):
                if player.prev_hitbox_y > obj.hitbox_y:
                    player.hitbox_y = obj.hitbox_y + (player.hitbox_height + obj.hitbox_height) / 2
                else:
                    player.hitbox_y = obj.hitbox_y - (player.hitbox_height + obj.hitbox_height) / 2
            else:
                if player.prev_hitbox_x > obj.hitbox_x:
                    player.hitbox_x = obj.hitbox_x + (player.hitbox_width + obj.hitbox_width) / 2
                else:
                    player.hitbox_x = obj.hitbox_x - (player.hitbox_width + obj.hitbox_width) / 2
                if player.prev_hitbox_y > obj.hitbox_y:
                    player.hitbox_y = obj.hitbox_y + (player.hitbox_height + obj.hitbox_height) / 2
                else:
                    player.hitbox_y = obj.hitbox_y - (player.hitbox_height + obj.hitbox_height) / 2
    player.moved = False


fill_sprites()
all_sprites['mushroom'].set_colorkey((0xFFFFFF))
all_sprites['player'].set_colorkey((0xFFFFFF))
for key in player_sprites.keys():
    player_sprites[key].set_colorkey((0xFFFFFF))

inventory = Inventory(screen, [0, 100], all_sprites['inventory_bar'], 9, 7, all_sprites['empty_slot'])

player = Player(screen, player_sprites, player_starting_coord, 8,
                [player_sprites['down1'].get_width() / 2, all_sprites['player'].get_height() / 16])

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
    input_handler()
    check_collisions()
    bg_manager.draw_scenery(player)
    inventory.draw()
    pygame.display.update()
    clock.tick(FPS)
    keyboard.update()

pygame.quit()

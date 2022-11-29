from constants import *
from keyboard import *
from player import *
from visuals import *
from inventory_and_menu import *
from managers import *


all_sprites = {'starting_background': 0,
               'inventory_bar': 0,
               'empty_slot': 0,
               'mushroom': 0,
               'player': 0,
               }

def fill_sprites():
    for key in all_sprites.keys():
        all_sprites[key] = pygame.image.load('C:\\Users\\Dell\\Desktop\\sprites\\' + key + '.png').convert()

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
        if inventory.active:
            if (not keyboard.key_pressed['w'][0]) and keyboard.key_pressed['w'][1]:
                inventory.selected_up()
            elif (not keyboard.key_pressed['s'][0]) and keyboard.key_pressed['s'][1]:
                inventory.selected_down()
        elif not player.immobile:
            if keyboard.key_pressed['w'][1] and keyboard.key_pressed['d'][1]:
                player.move('u', 2**(1/2))
                player.move('r', 2**(1/2))
            elif keyboard.key_pressed['w'][1] and keyboard.key_pressed['a'][1]:
                player.move('u', 2**(1/2))
                player.move('l', 2**(1/2))
            elif keyboard.key_pressed['s'][1] and keyboard.key_pressed['d'][1]:
                player.move('d', 2**(1/2))
                player.move('r', 2**(1/2))
            elif keyboard.key_pressed['s'][1] and keyboard.key_pressed['a'][1]:
                player.move('d', 2**(1/2))
                player.move('l', 2**(1/2))
            else:
                if keyboard.key_pressed['w'][1]:
                    player.move('u')
                if keyboard.key_pressed['a'][1]:
                    player.move('l')
                if keyboard.key_pressed['s'][1]:
                    player.move('d')
                if keyboard.key_pressed['d'][1]:
                    player.move('r')

def check_collisions(bg_number):
    if player.hitbox_x - player.hitbox_width/2 < left_barrier:
        player.hitbox_x = left_barrier + player.hitbox_width/2
    if player.hitbox_x + player.hitbox_width/2 > right_barrier:
        player.hitbox_x = right_barrier - player.hitbox_width/2
    if player.hitbox_y - player.hitbox_height/2 < top_barrier:
        player.hitbox_y = top_barrier + player.hitbox_height/2
    if player.hitbox_y + player.hitbox_height/2 > bottom_barrier:
        player.hitbox_y = bottom_barrier - player.hitbox_height/2

    for obj in bg_manager.backgrounds[bg_number].objects:
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


inventory = Inventory(screen, [0, 100], all_sprites['inventory_bar'], 9, 7, all_sprites['empty_slot'])
player = Player(screen, [all_sprites['player']], player_starting_coord, 8,
                [all_sprites['player'].get_width()/2, all_sprites['player'].get_height()/16])
obj1 = Object(screen, [all_sprites['mushroom']], [200, 500],
                          [[all_sprites['mushroom'].get_width(), all_sprites['mushroom'].get_height()/8]])
obj2 = Object(screen, [all_sprites['mushroom']], [500, 400],
                          [[all_sprites['mushroom'].get_width(), all_sprites['mushroom'].get_height()/16]])
obj3 = Object(screen, [all_sprites['mushroom']], [300, 300],
                          [[all_sprites['mushroom'].get_width(), all_sprites['mushroom'].get_height()/32]])
bg1 = Background(screen, all_sprites['starting_background'], [obj1, obj2, obj3])
bg_manager = BackgroundManager([bg1])

for j in range(3):
    inventory.add_item(obj3)
for j in range(1):
    inventory.remove_item(obj3)

while not finished:
    input_handler()
    check_collisions(0)
    bg_manager.draw_scenery(0, player)
    inventory.draw()
    pygame.display.update()
    clock.tick(FPS)
    keyboard.update()

pygame.quit()

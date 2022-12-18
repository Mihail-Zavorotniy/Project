from copy import copy
from keyboard import *
from player import *
from inventory_and_menu import *





def check_interaction(bg_manager, player: Player, inventory: Inventory):
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

def input_handler(inventory: Inventory, player: Player, bg_manager):
    finished = False
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
            check_interaction(bg_manager, player, inventory)
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
                if (not keyboard.key_pressed['d'][1]) and (not keyboard.key_pressed['s'][1]) and (not keyboard.key_pressed['a'][1]) and (not keyboard.key_pressed['w'][1]):
                    if keyboard.key_pressed['w'][0]:
                        player.stay('u')
                    if keyboard.key_pressed['a'][0]:
                        player.stay('l')
                    if keyboard.key_pressed['s'][0]:
                        player.stay('d')
                    if keyboard.key_pressed['d'][0]:
                        player.stay('r')
    return finished




class BackgroundManager:

    '''класс BackgroungManager
    backgrounds - список всех бэкграундов в игре
    current_bg - бэкграунд локации, в которой надожится персонаж
    '''
    def __init__(self, backgrounds, current_bg_number):
        '''Конструктор'''
        self.backgrounds = backgrounds
        self.current_bg = backgrounds[current_bg_number]

    def update(self, new_bg_number):
        '''Изменение бэкграунда'''
        self.current_bg = self.backgrounds[new_bg_number]

    def draw_scenery(self, player):
        '''Отрисовка бэкграунда и объектов в комнате'''
        self.current_bg.draw()
        objects_to_draw = copy(self.current_bg.all_objects)
        player_drawn = False
        for obj in objects_to_draw:
            if obj.y + obj.sprite.get_height() < player.hitbox_y + player.hitbox_height/2 or player_drawn:
                obj.draw()
            else:
                player.draw()
                obj.draw()
                player_drawn = True
        if not player_drawn:
            player.draw()

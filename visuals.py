import pygame
from constants import *
from player import *

class Object:
    '''класс объекта
    screen - экран, на котором расположен объект
    current_state - текущее состояние объекта (только для объектов с возможным взаимодействием)
    sprites - кортеж возможных спрайтов
    sprite - спрайт, который сейчас отображается на экране
    x, y - координаты лекого верхнего угла объекта
    hitbox_sizes - размеры объетов для всех спрайтов
    hitbox_wigth, hitbox_height - размеры предмета в текущем состоянии
    hitbox_x, hitbox_y - координаты центра объекта
    '''
    def __init__(self, screen: pygame.Surface, sprites: list, coord: list, hitbox_sizes):
        '''Конструктор'''
        self.screen = screen
        self.current_state = 0
        self.sprites = sprites
        self.sprite = self.sprites[self.current_state]
        self.x = coord[0]
        self.y = coord[1]
        self.hitbox_sizes = hitbox_sizes
        self.hitbox_width = self.hitbox_sizes[self.current_state][0]
        self.hitbox_height = self.hitbox_sizes[self.current_state][1]
        self.hitbox_x = self.x + self.sprite.get_width()/2
        self.hitbox_y = self.y + self.sprite.get_height() - self.hitbox_height/2

    def draw(self):
        '''Отрисовка объекта'''
        self.screen.blit(self.sprite, (self.x, self.y))


class ObjectInteractable(Object):
    '''класс объектов, с которыми можно взаимодействовать
    наследует класс объектов
    inter_area - зона вокруг предмета, находясь в которой можно взаимодействовать с объектом
    pickup - опрееляет, как происходит взаимодействие с объектом. true - можно подобрать, false - меняетс прайт при взаимодействии
    inventory_sprite - спрайт этого объекта в инветаре
    required_item - объект, необходимый для взаимодействия с этим объектом
    given_item - объект, получаемый после взаимодействия
    '''
    def __init__(self, screen: pygame.Surface, sprites: list, coord: list, hitbox_sizes, pickup: bool, interaction_area=4,
                 inventory_sprite=None, required_item=None, given_item=None ):
        super().__init__(screen, sprites, coord, hitbox_sizes)
        self.inter_area = interaction_area
        self.pickup = pickup
        if self.pickup:
            if inventory_sprite != None:
                self.inventory_sprite = inventory_sprite
            else:
                self.inventory_sprite = self.sprite
        elif required_item != None:
            self.required_item = required_item

    def change_state(self, new_state):
        '''Изменить состояние объекта
        nex_state - номер состояния объекта
        '''
        self.current_state = new_state
        self.sprite = self.sprites[self.current_state]
        self.hitbox_width = self.hitbox_sizes[self.current_state][0]
        self.hitbox_height = self.hitbox_sizes[self.current_state][1]
        self.hitbox_x = self.x + self.sprite.get_width() / 2
        self.hitbox_y = self.y + self.sprite.get_height() - self.hitbox_height / 2

 #   def give(self, player: Player, inventory: Inventory):
 #       '''
 #       дает объекты после взаимодействия
 #       '''
 #
 #       if ((abs(player.hitbox_x - self.hitbox_x) <= (player.hitbox_width + self.hitbox_width)/2 + self.inter_area) and
 #           (abs(player.hitbox_y - self.hitbox_y) <= (player.hitbox_height + self.hitbox_height)/2 + self.inter_area)) and
 #           self.required_item == invenory.contents[selected_slot] and player.immobile:
 #               
 #           inventory.add_item(self.given_item)
 #           inventory.remove_item(invenory.contents[selected_slot])








class Background:
    '''класс бэкграунда
    screen - экран, на котором расположен бэкграунд
    sprite - спрайт бэкграунда
    x, y - координаты левого верхнего угла бэкграунда (левый верхний угол экрана)
    objects - кортеж объектов на бэкграунде, отсортированный по их координате y
    interactable_objects - кортеж объектов на бэкграунде, с которыми можно взаимодействовать, отсортированный по их координате y
    all_objects - кортеж всех объектов на бэкграунде
    '''
    def __init__(self, screen, sprite, objects_list, interactable_objects_list=None, coord=[0,0]):
        self.screen = screen
        self.sprite = sprite
        self.x = coord[0]
        self.y = coord[1]
        self.objects = sorted(objects_list, key=lambda t: t.hitbox_y)
        if interactable_objects_list != None:
            self.interactable_objects = sorted(interactable_objects_list, key=lambda t: t.hitbox_y)
        self.all_objects = sorted((objects_list + interactable_objects_list), key=lambda t: t.hitbox_y)


    def draw(self):
        '''Отрисовка бэкграунда'''
        self.screen.blit(self.sprite, (self.x, self.y))


#    def check_collisions_for_objects(self, obj: ObjectInteractable, bg_manager):
#        if obj.hitbox_x - obj.hitbox_width / 2 < left_barrier:
#            obj.hitbox_x = left_barrier + obj.hitbox_width / 2
#        if obj.hitbox_x + obj.hitbox_width / 2 > right_barrier:
#            obj.hitbox_x = right_barrier - obj.hitbox_width / 2
#        if obj.hitbox_y - obj.hitbox_height / 2 < top_barrier:
#            obj.hitbox_y = top_barrier + obj.hitbox_height / 2
#        if obj.hitbox_y + obj.hitbox_height / 2 > bottom_barrier:
#            obj.hitbox_y = bottom_barrier - obj.hitbox_height / 2
#
#        for obj in bg_manager.current_bg.all_objects:
#            if (abs(obj.hitbox_x - obj.hitbox_x) < (obj.hitbox_width + obj.hitbox_width) / 2 and
#                    abs(obj.hitbox_y - obj.hitbox_y) < (obj.hitbox_height + obj.hitbox_height) / 2):
#                if ((obj.hitbox_width + obj.hitbox_width) / 2 - abs(obj.hitbox_x - obj.hitbox_x) <
#                        (obj.hitbox_height + obj.hitbox_height) / 2 - abs(obj.hitbox_y - obj.hitbox_y)):
#                    if obj.prev_hitbox_x > obj.hitbox_x:
#                        obj.hitbox_x = obj.hitbox_x + (obj.hitbox_width + obj.hitbox_width) / 2
#                    else:
#                        obj.hitbox_x = obj.hitbox_x - (obj.hitbox_width + obj.hitbox_width) / 2
#                elif ((obj.hitbox_width + obj.hitbox_width) / 2 - abs(obj.hitbox_x - obj.hitbox_x) >
#                      (obj.hitbox_height + obj.hitbox_height) / 2 - abs(obj.hitbox_y - obj.hitbox_y)):
#                    if obj.prev_hitbox_y > obj.hitbox_y:
#                        obj.hitbox_y = obj.hitbox_y + (obj.hitbox_height + obj.hitbox_height) / 2
#                    else:
#                        obj.hitbox_y = obj.hitbox_y - (obj.hitbox_height + obj.hitbox_height) / 2
#                else:
#                    if obj.prev_hitbox_x > obj.hitbox_x:
#                        obj.hitbox_x = obj.hitbox_x + (obj.hitbox_width + obj.hitbox_width) / 2
#                    else:
#                        obj.hitbox_x = obj.hitbox_x - (obj.hitbox_width + obj.hitbox_width) / 2
#                    if obj.prev_hitbox_y > obj.hitbox_y:
#                        obj.hitbox_y = obj.hitbox_y + (obj.hitbox_height + obj.hitbox_height) / 2
#                    else:
#                        obj.hitbox_y = obj.hitbox_y - (obj.hitbox_height + obj.hitbox_height) / 2


    def add_object(self, obj: ObjectInteractable, player: Player):
        '''
        функция добавляет объект из инвентаря на текущий бэкграунд рядом с игроком
        obj - объект типа ObjectInteractable, который мы хотим добавить на бэкграунд из инвентаря
        player - объект типа Player
        return - ничего
        '''
        obj.x = player.hitbox_x
        obj.y = player.hitbox_y + obj.hitbox_height
        obj.hitbox_x = obj.x + obj.sprite.get_width() / 2
        obj.hitbox_y = obj.y + obj.sprite.get_height() - obj.hitbox_height / 2
        #check_collisions_for_objects(obj, bg_manager)
        self.interactable_objects.append(obj)
        self.interactable_objects = sorted(self.interactable_objects, key=lambda t: t.hitbox_y)
        self.all_objects = sorted((self.objects + self.interactable_objects), key=lambda t: t.hitbox_y)
import pygame
from pygame import draw


class Inventory:
    '''класс инвентаря
    screen - экран, на котором расположен инвентарь
    active - true - пользователь взаимодействует с инвентарем, false - не взаимодействует
    sprite - спрайт инвентаря
    empty_sprite - спрайт пустого слота инвентаря
    height, width - размеры спрайта всего инвентаря
    border_width - ширина стороны окошка выбранного слота
    border_color - цвет окошка выбранного слота
    slots_amount - количество слотов в инвентаре
    slot_size - размер одного слота
    contents - кортеж с содержимым инвентаря
    x, y - координаты левого верхнего угла инвентаря
    selected_slot - текущий выбранный слот инвентаря
    '''
    def __init__(self, screen, coord, sprite, slots_amount, border_width, empty_sprite, border_color=0xFFFFFF):
        self.screen = screen
        self.active = False
        self.sprite = sprite
        self.empty_sprite = empty_sprite
        self.height = sprite.get_height()
        self.width = sprite.get_width()
        self.border_width = border_width
        self.border_color = border_color
        self.slots_amount = slots_amount
        self.slot_size = (self.height - border_width) / slots_amount - border_width
        self.contents = [None] * slots_amount
        self.x = coord[0]
        self.y = coord[1]
        self.selected_slot = 0

    def draw(self):
        '''Отрисовка инвентаря, его содержимого и рамочки выбранного слота'''
        self.screen.blit(self.sprite, (self.x, self.y))
        for i in range(self.slots_amount):
            if self.contents[i] == None:
                self.screen.blit(self.empty_sprite,
                                 (self.x + self.border_width,
                                  self.y + self.border_width + i * (self.slot_size + self.border_width)))
            else:
                self.screen.blit(self.contents[i].sprite,
                                 (self.x + self.border_width,
                                  self.y + self.border_width + i * (self.slot_size + self.border_width)))
        if self.active:
            self.draw_selected_slot()
        else:
            self.selected_slot = 0

    def draw_selected_slot(self):
        '''Отрисовка окошка выбранного слота'''
        draw.line(self.screen, self.border_color,
                  (self.x,
                   self.y + self.border_width / 2 + self.selected_slot * (self.slot_size + self.border_width)),
                  (self.x + self.slot_size + 2 * self.border_width,
                   self.y + self.border_width / 2 + self.selected_slot * (self.slot_size + self.border_width)),
                  self.border_width)
        draw.line(self.screen, self.border_color,
                  (self.x,
                   self.y + self.slot_size + 3 * self.border_width / 2 + self.selected_slot * (
                               self.slot_size + self.border_width)),
                  (self.x + self.slot_size + 2 * self.border_width,
                   self.y + self.slot_size + 3 * self.border_width / 2 + self.selected_slot * (
                               self.slot_size + self.border_width)),
                  self.border_width)
        draw.line(self.screen, self.border_color,
                  (self.x + self.border_width / 2,
                   self.y + self.selected_slot * (self.slot_size + self.border_width)),
                  (self.x + self.border_width / 2,
                   self.y + self.slot_size + 2 * self.border_width + self.selected_slot * (
                               self.slot_size + self.border_width)),
                  self.border_width)
        draw.line(self.screen, self.border_color,
                  (self.x + self.slot_size + 3 * self.border_width / 2,
                   self.y + self.selected_slot * (self.slot_size + self.border_width)),
                  (self.x + self.slot_size + 3 * self.border_width / 2,
                   self.y + self.slot_size + 2 * self.border_width + self.selected_slot * (
                               self.slot_size + self.border_width)),
                  self.border_width)

    def add_item(self, obj):
        '''Добавление объекта в инвентарь'''
        for i in range(len(self.contents)):
            if self.contents[i] == None:
                self.contents[i] = obj
                break

    def remove_item(self, obj):
        '''Удаление объекта из инвентаря'''
        for i in range(len(self.contents)):
            if self.contents[i] == obj:
                self.contents[i] = None
                break

    def selected_up(self):
        '''Движение окошка выбранного слота вверх (переход на нижнее, если достигли верха)'''
        self.selected_slot -= 1
        if self.selected_slot < 0:
            self.selected_slot = self.slots_amount - 1

    def selected_down(self):
        '''Движение окошка выбранного слота вниз (переход на верхнее, если достигли низа'''
        self.selected_slot += 1
        if self.selected_slot >= self.slots_amount:
            self.selected_slot = 0


class Menu(Inventory):
    def __init__(self, screen, coord, sprite, slots_amount, slot_width, border_width, empty_sprite):
        super().__init__(screen, coord, sprite, slots_amount, border_width, empty_sprite)
        self.slot_width = slot_width

    def draw_selected_slot(self):
        draw.line(self.screen, self.border_color,
                  (self.x,
                   self.y + self.border_width / 2 + self.selected_slot * (self.slot_size + self.border_width)),
                  (self.x + self.slot_width + 2 * self.border_width,
                   self.y + self.border_width / 2 + self.selected_slot * (self.slot_size + self.border_width)),
                  self.border_width)
        draw.line(self.screen, self.border_color,
                  (self.x,
                   self.y + self.slot_size + 3 * self.border_width / 2 + self.selected_slot * (
                           self.slot_size + self.border_width)),
                  (self.x + self.slot_width + 2 * self.border_width,
                   self.y + self.slot_size + 3 * self.border_width / 2 + self.selected_slot * (
                           self.slot_size + self.border_width)),
                  self.border_width)
        draw.line(self.screen, self.border_color,
                  (self.x + self.border_width / 2,
                   self.y + self.selected_slot * (self.slot_size + self.border_width)),
                  (self.x + self.border_width / 2,
                   self.y + self.slot_size + 2 * self.border_width + self.selected_slot * (
                           self.slot_size + self.border_width)),
                  self.border_width)
        draw.line(self.screen, self.border_color,
                  (self.x + self.slot_width + 3 * self.border_width / 2,
                   self.y + self.selected_slot * (self.slot_size + self.border_width)),
                  (self.x + self.slot_width + 3 * self.border_width / 2,
                   self.y + self.slot_size + 2 * self.border_width + self.selected_slot * (
                           self.slot_size + self.border_width)),
                  self.border_width)

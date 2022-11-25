import pygame
from pygame import draw


class Inventory:
    def __init__(self, screen, coord, sprite, slots_amount, border_width, empty_sprite, border_color=0xFFFFFF):
        self.screen = screen
        self.active = False
        self.sprite = sprite
        self.height = sprite.get_height()
        self.width = sprite.get_width()
        self.border_width = border_width
        self.border_color = border_color
        self.slots_amount = slots_amount
        self.slot_size = (self.height - border_width) / slots_amount - border_width
        self.empty_sprite = empty_sprite
        self.contents = [empty_sprite] * slots_amount
        self.x = coord[0]
        self.y = coord[1]
        self.selected_slot = 0
        self.empty_sprite = empty_sprite

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))
        for i in range(self.slots_amount):
            self.screen.blit(self.contents[i],
                             (self.x + self.border_width,
                              self.y + self.border_width + i * (self.slot_size + self.border_width)))
        if self.active:
            self.draw_selected_slot()
        else:
            self.selected_slot = 0

    def draw_selected_slot(self):
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

    def add_item(self, item_sprite):
        for i in range(len(self.contents)):
            if self.contents[i] == self.empty_sprite:
                self.contents[i] = item_sprite
                break

    def remove_item(self, item_sprite):
        for i in range(len(self.contents)):
            if self.contents[i] == item_sprite:
                self.contents[i] = self.empty_sprite
                break

    def selected_up(self):
        self.selected_slot -= 1
        if self.selected_slot < 0:
            self.selected_slot = self.slots_amount - 1

    def selected_down(self):
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

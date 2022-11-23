import pygame
from pygame import draw


class ObjectNotInteractable:
    def __init__(self, screen, sprite, coord, hitbox_size, hitbox_pos):
        self.screen = screen
        self.sprite = sprite
        self.x = coord[0]
        self.y = coord[1]
        self.hitbox_width = hitbox_size[0]
        self.hitbox_height = hitbox_size[1]
        self.hitbox_x = coord[0] + hitbox_pos[0]
        self.hitbox_y = coord[1] + hitbox_pos[1]

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))

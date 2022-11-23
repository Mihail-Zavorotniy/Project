import pygame
from pygame import draw


class Background:
    def __init__(self, screen, sprite, objects_list, coord=[0,0]):
        self.screen = screen
        self.sprite = sprite
        self.x = coord[0]
        self.y = coord[1]
        self.object_list = objects_list

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))

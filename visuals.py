import pygame


class ObjectNotChangable:
    def __init__(self, screen: pygame.Surface, sprites: list, coord: list, hitbox_size):
        self.screen = screen
        self.sprite = sprites[0]
        self.x = coord[0]
        self.y = coord[1]
        self.hitbox_width = hitbox_size[0]
        self.hitbox_height = hitbox_size[1]
        self.hitbox_x = self.x + self.hitbox_width/2
        self.hitbox_y = self.y + self.sprite.get_height() - self.hitbox_height / 2

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))


class Background:
    def __init__(self, screen, sprite, objects_list, coord=[0,0]):
        self.screen = screen
        self.sprite = sprite
        self.x = coord[0]
        self.y = coord[1]
        self.objects = sorted(objects_list, key=lambda t: t.hitbox_y)


    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))

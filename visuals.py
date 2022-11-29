import pygame


class Object:
    def __init__(self, screen: pygame.Surface, sprites: list, coord: list, hitbox_sizes, inventory_sprite=None):
        self.screen = screen
        self.current_state = 0
        self.sprites = sprites
        self.sprite = self.sprites[self.current_state]
        if inventory_sprite != None:
            self.inventory_sprite = inventory_sprite
        else:
            self.inventory_sprite = self.sprite
        self.x = coord[0]
        self.y = coord[1]
        self.hitbox_widthes = hitbox_sizes[0]
        self.hitbox_heights = hitbox_sizes[1]
        self.hitbox_width = self.hitbox_widthes[self.current_state]
        self.hitbox_height = self.hitbox_heights[self.current_state]
        self.hitbox_x = self.x+self.sprites[self.current_state].get_width()/2
        self.hitbox_y = self.y+self.sprites[self.current_state].get_height()-self.hitbox_heights[self.current_state]/2

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

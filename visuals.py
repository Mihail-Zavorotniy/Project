import pygame


class Object:
    def __init__(self, screen: pygame.Surface, sprites: list, coord: list, hitbox_sizes):
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
        self.screen.blit(self.sprite, (self.x, self.y))


class ObjectInteractable(Object):
    def __init__(self, screen: pygame.Surface, sprites: list, coord: list, hitbox_sizes, pickup: bool, interaction_area=4,
                 inventory_sprite=None, required_item=None):
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
        self.current_state = new_state
        self.sprite = self.sprites[self.current_state]
        self.hitbox_width = self.hitbox_sizes[self.current_state][0]
        self.hitbox_height = self.hitbox_sizes[self.current_state][1]
        self.hitbox_x = self.x + self.sprite.get_width() / 2
        self.hitbox_y = self.y + self.sprite.get_height() - self.hitbox_height / 2

class Background:
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
        self.screen.blit(self.sprite, (self.x, self.y))
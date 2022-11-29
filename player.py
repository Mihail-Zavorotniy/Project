import pygame


class Player:
    def __init__(self, screen: pygame.Surface, sprites: list, coord: list,
                  movement_speed, hitbox_size: list):
        self.screen = screen
        self.sprite = sprites[0]
        self.x = coord[0]
        self.y = coord[1]
        self.v = movement_speed
        self.moved = False
        self.immobile = False
        self.hitbox_width = hitbox_size[0]
        self.hitbox_height = hitbox_size[1]
        self.hitbox_x = self.x + self.hitbox_width / 2
        self.hitbox_y = self.y + self.sprite.get_height() - self.hitbox_height / 2
        self.prev_hitbox_x = self.hitbox_x
        self.prev_hitbox_y = self.hitbox_y
        
    def move(self, direcrion: str, norm=1):
        if not self.moved:
            self.prev_hitbox_x = self.hitbox_x
            self.prev_hitbox_y = self.hitbox_y
        self.moved = True
        if direcrion == 'r':
            self.hitbox_x += self.v / norm
        if direcrion == 'l':
            self.hitbox_x -= self.v / norm
        if direcrion == 'u':
            self.hitbox_y -= self.v / norm
        if direcrion == 'd':
            self.hitbox_y += self.v / norm

    def draw(self):
        self.screen.blit(self.sprite,
                        (self.hitbox_x - self.hitbox_width/2,
                         self.hitbox_y + self.hitbox_height/2 - self.sprite.get_height()))

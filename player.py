import pygame


class Player:

    '''
    класс игрока
    screen - экран, на котором расположен игрок
    sprite - текущий спрайт, который отображается на экране
    x, y - координаты левого верхнего угла игрока
    v - скорость движения
    moved - true если персонаж сейчас двигается, false - в противном случае
    immobile - true если пользователь взаимодействует в инвентарем и игрока нельзя двигать, false - в противном случае
    hitbox_width, hitbox_height - размеры хитбокса игрока
    hitbox_x, hitbox_y - координаты центра хитбокса
    prev_hitbox_x, prev_hitbox_y - позиция хитбокса на предыдущем фрейме
    '''
    def __init__(self, screen: pygame.Surface, sprites: dict, coord: list,
                  movement_speed, hitbox_size: list):
        '''Конструктор'''
        self.screen = screen
        self.sprites = sprites
        self.sprite = sprites['down1']
        self.x = coord[0]
        self.y = coord[1]
        self.v = movement_speed
        self.moved = False
        self.immobile = False
        self.hitbox_width = hitbox_size[0]
        self.hitbox_height = hitbox_size[1]
        self.hitbox_x = self.x + self.sprite.get_width() / 2
        self.hitbox_y = self.y + self.sprite.get_height() - self.hitbox_height / 2
        self.prev_hitbox_x = self.hitbox_x
        self.prev_hitbox_y = self.hitbox_y

    def move(self, direcrion: str, norm=1):
        '''Движение игрока'''
        if not self.moved:
            self.prev_hitbox_x = self.hitbox_x
            self.prev_hitbox_y = self.hitbox_y
        self.moved = True
        if direcrion == 'r':
            self.hitbox_x += self.v / norm
            self.sprite = self.sprites['right1']
        if direcrion == 'l':
            self.hitbox_x -= self.v / norm
            self.sprite = self.sprites['left1']
        if direcrion == 'u':
            self.hitbox_y -= self.v / norm
            self.sprite = self.sprites['up1']
        if direcrion == 'd':
            self.hitbox_y += self.v / norm
            self.sprite = self.sprites['down1']

    def draw(self):
        '''Отрисовка игрока'''
        self.screen.blit(self.sprite,
                        (self.hitbox_x - self.sprite.get_width() / 2,
                         self.hitbox_y + self.hitbox_height/2 - self.sprite.get_height()))

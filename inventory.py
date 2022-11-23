import pygame
from pygame import draw

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D

FPS = 30
WIDTH = 700
HEIGHT = 700
inventory_size = 6
all_sprites = {'inventory_bar': 0, 'empty_slot': 0, 'mushroom': 0}
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def fill_sprites():
    for key in all_sprites.keys():
        all_sprites[key] = pygame.image.load('C:\\Users\\Dell\\Desktop\\sprites\\' + key + '.png').convert()

fill_sprites()

def input_handler():
    global finished
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                inventory.active = True
            elif event.key == pygame.K_e:
                inventory.active = False
            if inventory.active:
                if event.key == pygame.K_w:
                    inventory.selected_up()
                elif event.key == pygame.K_s:
                    inventory.selected_down()


class Inventory:
    def __init__(self):
        self.screen = screen
        self.active = False
        self.sprite = all_sprites['inventory_bar']
        self.height = all_sprites['inventory_bar'].get_height()
        self.width = all_sprites['inventory_bar'].get_width()
        self.size = inventory_size
        self.slot_size = self.height/self.size
        self.contents = ['empty_slot']*self.size
        self.x = 0
        self.y = (HEIGHT - self.height)/2
        self.selection_x = self.x
        self.selection_y = self.y

    def draw(self):
        screen.blit(self.sprite, (self.x, self.y))
        for i in range(len(self.contents)):
            screen.blit(all_sprites[self.contents[i]], (8, self.y + self.slot_size * i + 6))
        if self.active:
            draw.line(screen, WHITE, (self.selection_x, self.selection_y),
                                     (self.selection_x + self.slot_size, self.selection_y), 3)
            draw.line(screen, WHITE, (self.selection_x, self.selection_y),
                                     (self.selection_x, self.selection_y + self.slot_size), 3)
            draw.line(screen, WHITE, (self.selection_x + self.slot_size, self.selection_y),
                                     (self.selection_x + self.slot_size, self.selection_y + self.slot_size), 3)
            draw.line(screen, WHITE, (self.selection_x, self.selection_y + self.slot_size),
                                     (self.selection_x + self.slot_size, self.selection_y + self.slot_size), 3)

    def add_item(self, item_name):
        for i in range(len(self.contents)):
            if self.contents[i] == 'empty_slot':
                self.contents[i] = item_name
                break

    def remove_item(self, item_name):
        for i in range(len(self.contents)):
            if self.contents[i] == item_name:
                self.contents[i] = 'empty_slot'
                break

    def selected_up(self):
        self.selection_y -= self.slot_size
        if self.selection_y <= self.y - 10:
            self.selection_y += self.slot_size * self.size

    def selected_down(self):
        self.selection_y += self.slot_size
        if self.selection_y >= self.y + self.slot_size * self.size:
            self.selection_y -= self.slot_size * self.size


finished = False
clock = pygame.time.Clock()
inventory = Inventory()

for j in range(10):
    inventory.add_item('mushroom')
for j in range(3):
    inventory.remove_item('mushroom')

while not finished:
    screen.fill(WHITE)
    inventory.draw()
    pygame.display.update()
    input_handler()
    print(inventory.active)
    clock.tick(FPS)

pygame.quit()
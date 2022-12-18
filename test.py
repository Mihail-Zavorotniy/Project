import os.path
from constants import *
from keyboard import *
from player import *
from visuals import *
from inventory_and_menu import *
from managers import *
from work_with_sprites import *


inventory = Inventory(screen, [0, 100], all_sprites['inventory_bar'], 9, 7, all_sprites['empty_slot'])
player = Player(screen, player_sprites, player_starting_coord, 8,
                [player_sprites['down'].get_width() / 2, player_sprites['down'].get_height() / 16])

bg_manager = BackgroundManager([bg1], 0)

while not finished:
    finished = input_handler(inventory, player, bg_manager)
    check_collisions(player, bg_manager)
    bg_manager.draw_scenery(player)
    inventory.draw()
    pygame.display.update()
    clock.tick(FPS)
    keyboard.update()

pygame.quit()

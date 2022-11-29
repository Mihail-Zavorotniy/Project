import pygame


FPS = 30
WIDTH = 900
HEIGHT = 700
left_barrier = 0
right_barrier = WIDTH
top_barrier = 200
bottom_barrier = HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
finished = False
player_starting_coord = [450, 350]

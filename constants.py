import pygame


FPS = 30
WIDTH = 900
HEIGHT = 700
left_barrier = 0
right_barrier = WIDTH
top_barrier = 0
bottom_barrier = HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(0xFFFFFF)
clock = pygame.time.Clock()
finished = False
player_starting_coord = [450, 350]

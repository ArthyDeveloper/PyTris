import pygame, math

def create_game_surface(screen_width, screen_height):
  surface_pos = (math.floor(screen_width*0.8), screen_height)
  return pygame.Surface(surface_pos)
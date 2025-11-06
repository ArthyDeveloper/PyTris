from settings import (
  grid_columns as cols,
  grid_rows as rows,
  grid_phantom_rows as phantom_rows
)
from game.logics import (
  checkTick,
  renderGrid
)
import pygame, settings, math

def create_game_surface(screen_width, screen_height):
  surface_pos = (math.floor(screen_width*0.8), screen_height)
  return pygame.Surface(surface_pos)

def scale_game_surface(surface, screen_width, screen_height):
  return pygame.transform.scale(surface, ((screen_width*0.8, screen_height)))

def get_dimensions(surface):
  return (surface.get_width(), surface.get_height())

def render_ui(panel, surface):
  surface_width, surface_height = get_dimensions(surface)
  mouse_pos = pygame.mouse.get_pos()
  match panel:
    case 'menu':
      font = pygame.font.Font(None, 30)
      text_color = 'white'
      text = font.render("Start", True, text_color)
      text_pos = text.get_rect(center=(surface_width * 0.5, surface_height * 0.7))
      if text_pos.collidepoint(mouse_pos):
        text_color = 'red'
        text = font.render("Start", True, text_color)
      else:
        text_color = 'white'
        text = font.render("Start", True, text_color)

      surface.blit(text, text_pos)

    case 'default':
      checkTick()
      renderGrid(surface, surface_width, surface_height)
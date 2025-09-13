from settings import (
  grid_columns as cols,
  grid_rows as rows,
  grid_phantom_rows as phantom_rows
)
from game.logics import (
  checkTick
)
import pygame, settings, math

def create_game_surface(screen_width, screen_height):
  surface_pos = (math.floor(screen_width*0.8), screen_height)
  return pygame.Surface(surface_pos)

def scale_game_surface(surface, screen_width, screen_height):
  return pygame.transform.scale(surface, ((screen_width*0.8, screen_height)))

def get_dimensions(surface):
  return (surface.get_width(), surface.get_height())

def render_ui(panel, surface, grid, block_size, border_size):
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

      # Game Grid
      for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
          x = surface_width * 0.5 - cols * block_size // 2 + col_idx * block_size + block_size
          y = surface_height * 0.5 - rows * block_size // 2 + row_idx * block_size
          pygame.draw.rect(surface, col[1], pygame.Rect(x, y, block_size, block_size))

      # Grid Barrier
      x = surface_width * 0.5 - (cols * block_size) // 2
      y = surface_height * 0.5 - rows * block_size // 2 + block_size * phantom_rows
      diff = block_size - border_size

      # Rect params: Pos x, Pos y , Width and Height
      pygame.draw.rect(surface, settings.grid_border_color, pygame.Rect(x + diff, y, border_size, block_size * rows)) # Left Barrier
      pygame.draw.rect(surface, settings.grid_border_color, pygame.Rect(x + ((cols+1) * block_size), y, border_size, block_size * rows)) # Right Barrier
      pygame.draw.rect(surface, settings.grid_border_color, pygame.Rect(x + diff, y + block_size * rows, (cols + 2) * block_size - (diff * 2), border_size)) # Bottom Barrier
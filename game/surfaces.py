from settings import (
  grid_columns as cols,
  grid_rows as rows,
  grid_phantom_rows as phantom_rows
)
import pygame, math

def create_game_surface(screen_width, screen_height):
  surface_pos = (math.floor(screen_width*0.8), screen_height)
  return pygame.Surface(surface_pos)

def scale_game_surface(surface, screen_width, screen_height):
  return pygame.transform.scale(surface, ((screen_width*0.8, screen_height)))

def get_dimensions(surface):
  return (surface.get_width(), surface.get_height())

def render_ui(panel, surface, grid, block_size, border_size):
  match panel:
    case 'default':
      surface_width, surface_height = get_dimensions(surface)
      # Game Grid
      for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
          x = int(surface_width * 0.5 - cols * block_size // 2 + col_idx * block_size + block_size)
          y = int(surface_height * 0.5 - rows * block_size // 2 + row_idx * block_size)
          pygame.draw.rect(surface, col[1], pygame.Rect(x, y, block_size, block_size))

      # Grid Barrier
      x = int(surface_width * 0.5 - cols * block_size // 2)
      y = int(surface_height * 0.5 - rows * block_size // 2 + border_size * phantom_rows)
      pygame.draw.rect(surface, 'white', pygame.Rect(x, y, border_size, border_size * rows)) # Left Barrier
      pygame.draw.rect(surface, 'white', pygame.Rect(x + ((cols+1) * border_size), y, border_size, border_size * rows)) # Right Barrier
      pygame.draw.rect(surface, 'white', pygame.Rect(x, y + border_size * rows, border_size * (cols + 2), border_size)) # Bottom Barrier
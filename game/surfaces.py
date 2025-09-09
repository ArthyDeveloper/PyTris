import pygame, math

def create_game_surface(screen_width, screen_height):
  surface_pos = (math.floor(screen_width*0.8), screen_height)
  return pygame.Surface(surface_pos)

def scale_game_surface(surface, screen_width, screen_height):
  return pygame.transform.scale(surface, ((screen_width*0.8, screen_height)))

def get_dimensions(surface):
  return (surface.get_width(), surface.get_height())

def render_ui(panel, surface, grid, cols, rows, phantom_rows, block_size):
  match panel:
    case 'default':
      surface_width, surface_height = get_dimensions(surface)
      # Game Grid
      for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
          x = int((surface_width * 0.25) + col_idx * block_size + block_size)
          y = int(surface_height * 0.3 - phantom_rows * block_size) + (row_idx * block_size)
          pygame.draw.rect(surface, col[1], pygame.Rect(x, y, block_size, block_size))

      # Grid Barrier
      for i in range(rows):
        x = int(surface_width * 0.25)
        y = int(surface_height * 0.3) + (i * block_size)

        pygame.draw.rect(surface, 'white', pygame.Rect(x, y, block_size, block_size))
        pygame.draw.rect(surface, 'white', pygame.Rect(x + ((cols+1) * block_size), y, block_size, block_size))
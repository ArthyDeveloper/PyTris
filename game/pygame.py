from settings import (
  start_screen_width,
  start_screen_height,
  game_clock,
  background_color
)
from game.logics import (
  scale,
  generateGrid,
  clear_console
)
from game.surfaces import (
  create_game_surface,
  scale_game_surface,
  get_dimensions,
  render_ui
)
from game.inputs import (
  events,
  controls
)
from datetime import datetime
import pygame, math

def start():
  pygame.init()
  pygame.display.set_caption("PyTris - A Tetris Clone")

  # Screen and surfaces set up
  screen = pygame.display.set_mode((start_screen_width, start_screen_height), pygame.RESIZABLE)

  screen_width = screen.get_width()
  screen_height = screen.get_height()

  game_surface = create_game_surface(screen_width, screen_height)
  game_surface_width, game_surface_height = get_dimensions(game_surface)

  # Grid - Standard = 10 Cols, 20 Rows
  block_size = scale(0.02, game_surface_width, game_surface_height)
  cols = 20
  rows = 30
  phantom_rows = 3
  grid = generateGrid(cols, rows, phantom_rows)

  clock = pygame.time.Clock()

  while True:
    # Debug
    start_loop = datetime.now()

    # Variables
    screen_width, screen_height = get_dimensions(screen)

    game_surface = create_game_surface(screen_width, screen_height)
    game_surface_width, game_surface_height = get_dimensions(game_surface)
    game_surface_center = (game_surface_width//2, game_surface_height//2)

    screen.fill(background_color)
    game_surface.fill((50, 50, 50))
    scale_game_surface(game_surface, screen_width, screen_height)

    render_ui('default', game_surface, grid, cols, rows, phantom_rows, block_size)

    screen.blit(game_surface, (math.floor(screen_width*0.1), 0))
    
    # Handling Events and Controls
    events(start_screen_width, start_screen_height)
    controls()

    clock.tick(game_clock)
    pygame.display.update()

    # Debug
    end_loop = datetime.now()
    clear_console()
    print(f'FPS: {clock.get_fps()}')
    print(f'Frametime: {(end_loop - start_loop).total_seconds():.3f}')

if __name__ == "__main__":
  start()
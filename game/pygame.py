from settings import (
  start_screen_width,
  start_screen_height,
  game_clock,
  background_color,
  block_size as bl_size,
  border_size as bo_size
)
from game.logics import (
  scale,
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
import pygame, settings, math

def start():
  pygame.init()
  pygame.display.set_caption("PyTris - A Tetris Clone")

  # Screen and surfaces set up
  screen = pygame.display.set_mode((start_screen_width, start_screen_height), pygame.RESIZABLE)
  screen_width, screen_height = get_dimensions(screen)

  game_surface = create_game_surface(screen_width, screen_height)
  game_surface_width, game_surface_height = get_dimensions(game_surface)

  # Grid - Standard = 10 Cols, 20 Rows
  block_size = scale(bl_size, game_surface_width, game_surface_height)
  border_size = scale(bo_size, game_surface_width, game_surface_height)

  settings.start_tick = datetime.now()
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

    render_ui('default', game_surface, settings.grid, block_size, border_size)

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
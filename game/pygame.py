from settings import (
  start_screen_width,
  start_screen_height,
  game_clock,
  background_color
)
from game.logics import (
  generateGrid
)
import pygame, math, sys

def start():
  pygame.init()
  pygame.display.set_caption("PyTris - A Tetris Clone")

  # Operations
  def scale(num):
    return int(min(game_surface_width, game_surface_height) * num)
  
  # Screen and surfaces set up
  screen = pygame.display.set_mode((start_screen_width, start_screen_height), pygame.RESIZABLE)
  screen_width = screen.get_width()
  screen_height = screen.get_height()
  game_surface_pos = [math.floor(screen_width*0.8), screen_height]
  game_surface = pygame.Surface(game_surface_pos)
  game_surface_width = game_surface.get_width()
  game_surface_height = game_surface.get_height()

  # Grid - Standard = 10 Cols, 20 Rows
  block_size = scale(0.02)
  cols = 20
  rows = 30
  phantom_rows = 3
  grid = generateGrid(cols, rows, phantom_rows)

  while True:
    # Variables
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    game_surface_pos = [math.floor(screen_width*0.8), screen_height]
    game_surface = pygame.Surface(game_surface_pos)
    game_surface_width = game_surface.get_width()
    game_surface_height = game_surface.get_height()
    game_surface_center = (game_surface_width//2, game_surface_height//2)

    screen.fill(background_color)
    game_surface.fill((50, 50, 50))
    game_surface = pygame.transform.scale(game_surface, (screen_width*0.8, screen_height))

    # Testing Grid
    for row_idx, row in enumerate(grid):
      for col_idx, col in enumerate(row):
        x = int((game_surface_width * 0.25) + col_idx * block_size + block_size)
        y = int(game_surface_height * 0.3 - phantom_rows * block_size) + (row_idx * block_size)
        pygame.draw.rect(game_surface, col[1], pygame.Rect(x, y, block_size, block_size))

    # Grid Barrier
    for i in range(rows):
      x = int(game_surface_width * 0.25)
      y = int(game_surface_height * 0.3) + (i * block_size)

      pygame.draw.rect(game_surface, 'white', pygame.Rect(x, y, block_size, block_size))
      pygame.draw.rect(game_surface, 'white', pygame.Rect(x + ((cols+1) * block_size), y, block_size, block_size))
    
    #pygame.draw.rect(game_surface, 'white', pygame.Rect(game_surface_center[0], game_surface_center[1], 5, 5))
    #pygame.draw.circle(game_surface, 'red', game_surface_center, scale(0.05))
    screen.blit(game_surface, (math.floor(screen_width*0.1), 0))
    
    # Handling Events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    
    # Handling Controls
    keys = pygame.key.get_pressed()
    # Up and Down
    if keys[pygame.K_UP]:
      circle_pos.y -= 5
    if keys[pygame.K_DOWN]:
      circle_pos.y += 5

    # Left and Right
    if keys[pygame.K_LEFT]:
      circle_pos.x -= 5
    if keys[pygame.K_RIGHT]:
      circle_pos.x += 5

    # Debugs
    #if keys[pygame.K_SPACE]:

    clock = pygame.time.Clock().tick(game_clock) / 1000
    pygame.display.flip()

if __name__ == "__main__":
  start()
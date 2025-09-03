from settings import (
  start_screen_width,
  start_screen_height,
  game_clock,
  background_color
)
import pygame, math, sys

def start():
  pygame.init()
  pygame.display.set_caption("PyTris - A Tetris Clone")

  # Operations
  def scale(num):
    return int(min(game_surface_width, game_surface_height) * num)
  
  def generateGrid(cols, rows):
    out = []
    for _ in range(rows):
      row = []
      for _ in range(cols):
        row.append([False, "white"])
      out.append(row)
    
    return out
  
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

    for i in range(20):
      x = int(game_surface_width * 0.25)
      y = int(game_surface_height * 0.3) + (i * block_size)

      pygame.draw.rect(game_surface, 'white', pygame.Rect(x, y, block_size, block_size))
      pygame.draw.rect(game_surface, 'white', pygame.Rect(x + (11 * block_size), y, block_size, block_size))
    
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
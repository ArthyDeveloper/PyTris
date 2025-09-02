from settings import (
  screen_width,
  screen_height,
  game_clock,
  background_color
)
import pygame, math, sys

def start():
  pygame.init()
  screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
  pygame.display.set_caption("PyTris - A Tetris Clone")
  circle_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

  while True:
    screen.fill(background_color)
    circle = pygame.draw.circle(screen, "red", circle_pos, int(screen.get_height() * 0.01))
    
    # Handling Events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
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
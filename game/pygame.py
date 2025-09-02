from settings import (
  screen_width,
  screen_height,
  game_clock,
  background_color
)
import pygame, sys

def start():
  pygame.init()
  pygame.time.Clock().tick(game_clock)
  screen = pygame.display.set_mode((screen_width, screen_height))
  pygame.display.set_caption("PyTris - A Tetris Clone")

  while True:
    screen.fill(background_color)
    
    # Handling Events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

if __name__ == "__main__":
  start()
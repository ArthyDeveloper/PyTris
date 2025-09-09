import pygame, sys

# Handling Events
def events(screen_width, screen_height):
    for event in pygame.event.get():
      if event.type == pygame.QUIT: # Quitting Game
        pygame.quit()
        sys.exit()
      elif event.type == pygame.VIDEORESIZE: # Setting Minimal Window Size
        new_width, new_height = event.size
        if new_width < screen_width:
          new_width = screen_width
        if new_height < screen_height:
          new_height = screen_height
        
        pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

# Handling Inputs / Controls
def controls():
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
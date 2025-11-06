from settings import (
  grid_columns,
  grid_rows,
  grid_phantom_rows,
  grid_color,
  block_size,
  border_size
)
from datetime import datetime
import pygame, random, settings, os

# Clear console
def clear_console():
  os.system('cls')

# Resolution Scale
def scale(num, width, height):
  return int(min(width, height) * num//100)

# Generate Grid
def generateGrid(cols: int = grid_columns, rows: int = grid_rows, phantom_rows: int = grid_phantom_rows):
  grid = []
  default_grid_block = [False, grid_color]
  phantom_grid_block = [False, grid_color]

  # Generating Phantom Rows
  for _ in range(phantom_rows):
    row = []
    for _ in range(cols):
      row.append(phantom_grid_block)
    grid.append(row)

  # Generating Normal Rows
  for _ in range(rows):
    row = []
    for _ in range(cols):
      row.append(default_grid_block)
    grid.append(row)
  
  return grid

settings.grid = generateGrid(grid_columns, grid_rows, grid_phantom_rows)

def renderGrid(surface, surface_width, surface_height, grid=settings.grid, cols=grid_columns, rows=grid_rows, block_size=block_size, border_size=border_size, phantom_rows=grid_phantom_rows):
  # Grid - Standard = 10 Cols, 20 Rows
  block_size = scale(block_size, surface_width, surface_height)
  border_size = scale(border_size, surface_width, surface_height)

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

# Check tick, make piece go down
def checkTick():
  # Tick (Make piece go down)
  settings.end_tick = datetime.now()
  if (settings.end_tick - settings.start_tick).total_seconds() > settings.difficulty_tick:
    # Gameplay (Checking if piece is at max bottom level) TO BE MADE
    if settings.piece_y <= len(settings.grid) - settings.piece_height:
      settings.current_piece = randomPiece()
      settings.piece_y = 0
    else:
      settings.piece_y += 1
    settings.start_tick = datetime.now()

# Piece Width and Height
def pieceWidthHeight(piece):
  height = len(piece)
  width = len(piece[0])
  return (width, height)

# Random Piece
def randomPiece():
  # I L J Z S O T
  pieces = (
    ( # Line (I)
      (
        (1, 1, 1, 1)
      ),
      (
        (0, 1),
        (0, 1),
        (0, 1),
        (0, 1)
      ),
      (
        (0, 0, 0, 0),
        (1, 1, 1, 1)
      ),
      (
        (1),
        (1),
        (1),
        (1)
      )
    ),
    ( # L
      (
        (0, 0, 1),
        (1, 1, 1)
      ),
      (
        (1, 0),
        (1, 0),
        (1, 1)
      ),
      (
        (1, 1, 1),
        (1, 0, 0)
      ),
      (
        (1, 1),
        (0, 1),
        (0, 1)
      )
    ),
    ( # J
      (
        (1, 1, 1),
        (0, 0, 1)
      ),
      (
        (0, 1),
        (0, 1),
        (1, 1)
      ),
      (
        (1, 0, 0),
        (1, 1, 1)
      ),
      (
        (1, 1),
        (1, 0),
        (1, 0)
      )
    ),
    ( # Z
      (
        (1, 1, 0),
        (0, 1, 1)
      ),
      (
        (0, 1),
        (1, 1),
        (1, 0)
      )
    ),
    ( # S
      (
        (0, 1, 1),
        (1, 1, 0)
      ),
      (
        (1, 0),
        (1, 1),
        (0, 1)
      )
    ),
    ( # T
      (
        (0, 1, 0),
        (1, 1, 1)
      ),
      (
        (1, 0),
        (1, 1),
        (1, 0)
      ),
      (
        (1, 1, 1),
        (0, 1, 0)
      ),
      (
        (0, 1),
        (1, 1),
        (0, 1)
      ),
    ),
    ( # O
      (
        (1, 1),
        (1, 1)
      )
    )
  )

  return random.choice(pieces)

settings.current_piece = randomPiece()
settings.piece_width, settings.piece_height = pieceWidthHeight(settings.current_piece)
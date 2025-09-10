from settings import(
  grid_color,
  grid_columns,
  grid_rows,
  grid_phantom_rows
)
import os
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
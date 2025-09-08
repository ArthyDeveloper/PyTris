# Resolution Scale
def scale(num, width, height):
  return int(min(width, height) * num)

# Generate Grid
def generateGrid(cols: int, rows: int, phantom_rows: int):
  grid = []
  default_grid_block = [False, "white"]
  phantom_grid_block = [False, "red"]

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
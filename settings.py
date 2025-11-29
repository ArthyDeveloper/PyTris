# Pygame Window
start_screen_width = 480
start_screen_height = 480
game_clock = 15
background_color = 0, 0, 0

# Game Grid
block_size = 2
border_size = 1
grid_columns = 10
grid_rows = 20
grid_phantom_rows = 3
grid_color = 'gray10'
grid_border_color = 'white'
grid = []

# Game Logic
start_tick, end_tick = 0, 0 # In Datetime
difficulty_tick = 1 # In seconds
current_piece = ()
next_piece = ()
stored_piece = ()
piece_width, piece_height = 0, 0
piece_x, piece_y = 0, 0
piece_rotation = 0
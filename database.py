# database.py
# ===============================================
# Stores data for global/common variables
# ===============================================

import static
import cell

#################################################
# STATES
# Generally stuff that will get updated mid-game
#################################################

dino_mode_enabled = False
is_maze_active = False
main_drone_last_position = 0,0
main_drone_cur_facing = North
num_drone_spawned = 0

#################################################
# INIT
# Generally stuff that is built and left alone (indexes/arrays of static stuff)
#################################################

# Create our index of cells
world_cells = []
cell_id = 0
for y in range(static.ws):
	for x in range(static.ws):
		# Make a new cell instance (dictionary copy of cell.py defaults)
		new_cell = {
			"id": cell_id,
			"position": (x, y),
			"ground_type": cell.ground_type,
			"entity_type": cell.entity_type,
			"fertilized": cell.fertilized
		}
		world_cells.append(new_cell)
		cell_id += 1

# ------------------------------------------------
# Walls: world perimeter, and internal inside a maze
# ------------------------------------------------

wall_index = {}

def clean_wall_index():
	for y in range(static.ws):
		for x in range(static.ws):
			# right / internal
			if x < static.ws - 1:
				a = (x, y)
				b = (x + 1, y)
				wall_index[(a,b)] = None
				wall_index[(b,a)] = None

			# up / internal
			if y < static.ws - 1:
				a = (x, y)
				b = (x, y + 1)
				wall_index[(a,b)] = None
				wall_index[(b,a)] = None

clean_wall_index() #called the first time db is loaded

# Mark the perimeter walls as being blocked
# The perimeter of the world is always a wall when inside a maze, might as well set them now.
def set_maze_perimeter_walls():
	for x in range(static.ws):
		# bottom
		a = (x, 0)
		b = (x, -1)
		wall_index[(a,b)] = True
		wall_index[(b,a)] = True

		# top
		a = (x, static.ws - 1)
		b = (x, static.ws)
		wall_index[(a,b)] = True
		wall_index[(b,a)] = True

	for y in range(static.ws):
		# left
		a = (0, y)
		b = (-1, y)
		wall_index[(a,b)] = True
		wall_index[(b,a)] = True

		# right
		a = (static.ws - 1, y)
		b = (static.ws, y)
		wall_index[(a,b)] = True
		wall_index[(b,a)] = True

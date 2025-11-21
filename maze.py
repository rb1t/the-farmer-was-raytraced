# maze.py
# ===============================================
# Maze setup and exploration
# Currently using right-hand rule (always turn right if possible)
# Tracks visited cells and dead ends using database.wall_index
# ===============================================

import database
import do
import static
import drone


# ------------------------------------------------
# Buld maze
# ------------------------------------------------

def build(size):
	if (size>0):
		maze_size = size
	else:
		maze_size=static.ws*2 #full map need *2 for some reason?

	if get_entity_type()==Entities.Grass:
		plant(Entities.Bush)
		substance = maze_size * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
	#print("Building maze of size: ", str(maze_size))

# ------------------------------------------------
# simple, 'go right and check'
# ------------------------------------------------

def check_treasure():
	return (get_entity_type() == Entities.Treasure)


def move_to_random_spot(map_size):
	x = random()*map_size//1
	y = random()*map_size//1
	pos=x,y
	do.move_linear(pos)

def find_treasure_simple():
	facing = drone.facing
	right_dir = static.right_of[facing]
	left_dir  = static.left_of[facing]
	back_dir  = static.right_of[static.right_of[facing]]  # 180°

	# 1. Check for treasure
	if get_entity_type() == Entities.Treasure:
		#quick_print("***** Treasure! *****")

		# occassionally harvest or make a harder maze
		if ((random()*100//1)>=99):
			harvest()
			# database.clean_wall_index() # remove the perimeter walls now that the maze is gone
		else:
			use_item(Items.Weird_Substance,(static.ws*2))

		return True   # signal that treasure was found

	# 2. Try right first
	if can_move(right_dir):
		move(right_dir)
		drone.facing = right_dir
		#quick_print("Turned right and moved ", str(right_dir))
		return False

	# 3. Try forward
	elif can_move(facing):
		move(facing)
		#quick_print("Moved forward ", str(facing))
		return False

	# 4. Try left
	elif can_move(left_dir):
		move(left_dir)
		drone.facing = left_dir
		#quick_print("Turned left and moved ", str(left_dir))
		return False

	# 5. All blocked turn around
	else:
		move(back_dir)
		drone.facing = back_dir

# ------------------------------------------------
# Count walls around a given cell
# ------------------------------------------------
def get_cell_wall_count(pos):
	x, y = pos
	count = 0
	dirs = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
	for n in dirs:
		if (pos, n) in database.wall_index and database.wall_index[(pos, n)] == True:
			count += 1
	return count

# ------------------------------------------------
# Update list of dead-end cells
# ------------------------------------------------
def update_dead_cells():
	database.dead_cells = []
	for cell in database.world_cells:
		pos = cell["position"]
		if get_cell_wall_count(pos) >= 3:
			database.dead_cells.append(pos)

# ------------------------------------------------
# Get neighbour positions in right-hand order relative to direction
# ------------------------------------------------
def get_neighbors_in_order(cur_dir, pos):
	x, y = pos
	# Directions: N,E,S,W
	dirs = [(0,1), (1,0), (0,-1), (-1,0)]

	# Map direction to index without using .index()
	if cur_dir[0] == 0 and cur_dir[1] == 1:
		dir_index = 0  # North
	elif cur_dir[0] == 1 and cur_dir[1] == 0:
		dir_index = 1  # East
	elif cur_dir[0] == 0 and cur_dir[1] == -1:
		dir_index = 2  # South
	elif cur_dir[0] == -1 and cur_dir[1] == 0:
		dir_index = 3  # West
	else:
		dir_index = 0  # default North if unknown

	# Right-hand order: right, forward, left, back
	right_hand_order = [
		dirs[(dir_index + 1) % 4],
		dirs[dir_index],
		dirs[(dir_index + 3) % 4],
		dirs[(dir_index + 2) % 4]
	]

	neighbors = []
	for d in right_hand_order:
		n = (x + d[0], y + d[1])
		neighbors.append(n)
	return neighbors

# ------------------------------------------------
# Explore maze using right-hand rule
# ------------------------------------------------
def maze_explore():
	cur_pos = do.get_pos()
	visited = []
	cur_dir = (0,1)  # start facing north by default

	while True:
		update_dead_cells()

		if cur_pos not in visited:
			visited.append(cur_pos)

		moved = False
		neighbors = get_neighbors_in_order(cur_dir, cur_pos)

		for n in neighbors:
			if not do.check_bounds(n[0], n[1]):
				continue
			if (cur_pos, n) in database.wall_index and database.wall_index[(cur_pos, n)] == True:
				continue
			if n in database.dead_cells:
				continue

			do.move_linear(n)
			new_pos = do.get_pos()

			# record wall if move failed
			if new_pos == cur_pos:
				database.wall_index[(cur_pos, n)] = True
				database.wall_index[(n, cur_pos)] = True
				continue
			else:
				cur_dir = (n[0]-cur_pos[0], n[1]-cur_pos[1])
				cur_pos = new_pos
				moved = True
				break

		if not moved:
			break

	do.quick_print("Exploration done. Visited:", len(visited), "Dead ends:", len(database.dead_cells))


# ------------------------------------------------
# Explore maze using experimental approaches
# ------------------------------------------------

def solve(size,drone_id):
	if (size>0):
		maze_size = size
	else:
		maze_size=static.ws*2 #full map need *2 for some reason?
	# Check if we're standing on treasure
	if get_entity_type() == Entities.Treasure:
		quick_print("--> Treasure ...")
		# occassionally harvest or make a harder maze
		if ((random()*100//1)>=93):
			harvest()
			quick_print("(... harvested the treasure!)")
			# database.clean_wall_index() # remove the perimeter walls now that the maze is gone
		else:
			quick_print("(... used weird substance on the treasure ...)")
			substance = maze_size * 2**(num_unlocked(Unlocks.Mazes) - 1)
			use_item(Items.Weird_Substance, substance)
		return True   # signal that treasure was found
	# I probably don't need to check the ground here .. @TODO cleanup
	if ((get_entity_type()!=Entities.Grass) and (get_entity_type()!=Entities.Bush)):
		# Randomly assign [this] drone to try and move directly at the treasure
		if ((random()*100//1)>=98): #periodically each drone can become a wizard (move direct) for a turn
			change_hat(Hats.Wizard_Hat)
			treasure_pos=measure()
			do.move_linear(treasure_pos)

		#@TODO 888 is just a placeholder to not assign wizards. chang to 8 for every 8th
		if ((drone_id+1)%888//1==0): #every 8th drone will be permanently a purple hat/wizard (3 drones at max/32)
			change_hat(Hats.Wizard_Hat)
			do.move_linear(measure())
			if ((random()*66//1)>=64):# Add some random movement once in a while to hope and get unstuck (even for purple hats)
				change_hat(Hats.Cactus_Hat)
				do.move_random_once()
		elif ((random()*133//1)>=131):# Add some random movement once in a while to hope and get unstuck
			change_hat(Hats.Cactus_Hat)
			move_to_random_spot(maze_size)
		else:
			change_hat(Hats.Gold_Hat) #Normies - these drones don't have a special task yet
			find_treasure_simple()

	return False #must not have found treasure




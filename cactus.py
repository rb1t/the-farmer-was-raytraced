import do
import static
import database
import drone

ws = static.ws #use number for specific or for max unlocked, ws = static.ws

# ------------------------------------------------
# Till and plant the ground full of cactus
# ------------------------------------------------
# pass in True for multiple drones
# pass in False for single drone
def plant_cacti(multiple_drones):
	if not multiple_drones:
		for y in range(ws):
			for x in range(ws):
				if (get_ground_type()!=Grounds.Soil):
					till()
				do.use_water()
				if (get_entity_type()!=Entities.Cactus):
					plant(Entities.Cactus)
				move(North)
			move(East)
	else: #multiple drones means don't chant columns/x
		for y in range(ws):
			if (get_ground_type()!=Grounds.Soil):
				till()
			do.use_water()
			if (get_entity_type()!=Entities.Cactus):
				plant(Entities.Cactus)
			move(North)


# ------------------------------------------------
# Measure and record each cactus
# ------------------------------------------------
# Really only needed for more complex sorting.
# May only work with one drone as well
def record_sizes():
	database.make_cells(ws) # creates and stores array of all world's cells in database.world_cells[]
	index=0#
	for y in range(ws):
		for x in range(ws):
			cactus_size = measure()
			database.world_cells[index]["cactus_size"] = cactus_size
			index+=1
			move(North)
		move(East)

	for cell in database.world_cells:
		pos = cell["position"]
		cactus_size = cell["cactus_size"]
		cell_id = cell["id"]
		quick_print("Cell Pos: ", pos, " Id:", cell_id, "Cactus Size: ", cactus_size)
		#do_a_flip()

# ------------------------------------------------
# Bubble sort for cacti, single drone
# ------------------------------------------------
def bubble_sort_single():
	swapped=False #keep track if a swap happened, True means another pass will be needed

	for y in range(ws):
		for x in range(ws):
			#We want to measure() each time so we can potentially swap multiple times per cell pass
			#Check West
			if (measure(West)>measure() and x>0):
				swap(West)
				swapped=True

			#Check East
			if (measure(East)<measure() and x<ws-1):
				swap(East)
				swapped=True

			#Check North
			if (measure(North)<measure() and y<ws-1):
				swap(North)
				swapped=True

			#Check South
			if (get_pos_y()>0 and measure(South)>measure()):
				swap(South)
				swapped=True

			#Move to next column (right/east)
			if (get_pos_x()==ws-1):
				move(North)

			move(East)

	return swapped

# ------------------------------------------------
# Reverse Bubble sort for cacti, single drone, for achievement
# ------------------------------------------------
def reverse_bubble_sort_single():
	swapped=False #keep track if a swap happened, True means another pass will be needed

	for y in range(ws):
		for x in range(ws):
			#We want to measure() each time so we can potentially swap multiple times per cell pass
			#Check West
			if (measure(West)<measure() and x>0):
				swap(West)
				swapped=True

			#Check East
			if (measure(East)>measure() and x<ws-1):
				swap(East)
				swapped=True

			#Check North
			if (measure(North)>measure() and y<ws-1):
				swap(North)
				swapped=True

			#Check South
			if (get_pos_y()>0 and measure(South)>measure()):
				swap(South)
				swapped=True

			#Move to next column (right/east)
			if (get_pos_x()==ws-1):
				move(North)

			move(East)

	return swapped

# ------------------------------------------------
# Bubble sort for cacti, multiple drones
# ------------------------------------------------
def bubble_sort_multi():
	swapped=False #keep track if a swap happened, True means another pass will be needed

	if get_entity_type()!=Entities.Cactus:
		return True #consider a situation where there's no cactus a swap, because something went wrong
	else:
		for i in range(ws):
			x = get_pos_x()
			y = get_pos_y()
			entity_here = get_entity_type()
			#We want to measure() each time so we can potentially swap multiple times per cell pass
			#Check West
			if (entity_here == Entities.Cactus and x>0 and (measure(West))>(measure())):
				swap(West)
				swapped=True

			#Check East
			if (entity_here == Entities.Cactus and x<ws-1 and measure(East)<measure()):
				swap(East)
				swapped=True

			#Check North
			if (entity_here == Entities.Cactus and y<ws-1 and measure(North)<measure()):
				swap(North)
				swapped=True

			#Check South
			if (entity_here == Entities.Cactus and y>0 and measure(South)>measure()):
				swap(South)
				swapped=True

			move(North)

	return swapped

# ------------------------------------------------
# verify things are sorted
# ------------------------------------------------
# (one drone does the full map, but can be multiple running)
def check_finished_sort(drone_id):
	swapped=False #keep track if a swap happened, True means another pass will be needed

	for y in range(ws):
		for x in range(ws):
			#We want to measure() each time so we can potentially swap multiple times per cell pass
			pos_x = get_pos_x()
			pos_y = get_pos_y()
			entity_here = get_entity_type()

			if (entity_here!= Entities.Cactus and pos_x != drone_id): #it must have been solved, move back to start
				return False

			#Check West
			if (pos_x > 0 and measure()!=None and measure(West)!=None and measure(West)>measure()):
				swap(West)
				swapped=True

			#Check East
			if (pos_x < ws-1 and measure()!=None and measure(East)!=None and measure(East)<measure()):
				swap(East)
				swapped=True

			#Check North
			if (pos_y < ws -1 and measure()!=None and measure(North)!=None and measure(North)<measure()):
				swap(North)
				swapped=True

			#Check South
			if (pos_y > 0 and measure()!=None and measure(South)!=None and measure(South)>measure()):
				swap(South)
				swapped=True

			#Move to next column (right/east)
			if (entity_here == Entities.Cactus and pos_x==ws-1):
				move(North)
			move(East)

	return swapped

#
def set_up_cacti(multiple_drones):
	if not multiple_drones:
		for y in range(ws):
			for x in range(ws):
				if (get_ground_type()!=Grounds.Soil):
					till()
				do.use_water()
				if (get_entity_type()!=Entities.Cactus):
					plant(Entities.Cactus)
				move(North)
			move(East)
	else: #multiple drones means don't chant columns/x
		for y in range(ws):
			if (get_ground_type()!=Grounds.Soil):
				till()
			do.use_water()
			if (get_entity_type()!=Entities.Cactus):
				plant(Entities.Cactus)
			move(North)

# ------------------------------------------------
# Solve the map; assumes cacti are already planted
# ------------------------------------------------
def solve(drone_id):
	if get_entity_type()!=Entities.Cactus:
		spread_position = drone_id,0
		do.move_linear(spread_position)
		plant_cacti(True)
		do_a_flip() #waiting for other drones before starting to sort
		do_a_flip()
		do_a_flip()
		return False
	elif bubble_sort_multi():
		return False
	elif not check_finished_sort(drone_id):
		print("Resetting!")
		return True
	return False

#################################################
# `SELF TEST`
#################################################

# Game must directly `Play` this file to access "__main__"
if __name__ == "__main__":
	set_world_size(ws)
	# Example harvester
	plant_cacti(False)
	while True:
		#while bubble_sort_single():
		while reverse_bubble_sort_single():
			pass
		harvest()
		plant_cacti(False)
	pass

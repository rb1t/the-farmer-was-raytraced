# do.py
# ===============================================
# Contains a lot of bassic, re-usable functions
# Movement, harvesting, scanning the area, etc.
# Needs regular cleaning and refactoring. And
# pairing down and modularizing .. :S
#
# Ideally I'm only using as few external modules
# as needed, for whatever I put in here.
# ===============================================

import static
import database
import drone

#################################################
# COMMON FUNCTIONS
#################################################

# Validate coordinates are in world bounds
def check_bounds(x, y):
	return not (x < 0 or y < 0 or x >= static.ws or y >= static.ws)

# Count up our resources and return in a dictionary
def count_items():
	item_counts = []
	for item in static.items:
		count = num_items(item)
		item_counts.append((item, count))
	return item_counts

# Return a random coordinate in the world
def gen_random_pos():
	x = random() * static.ws // 1
	y = random() * static.ws // 1
	return x, y

# print a random quantity right in game #CAN DELETE
def print_random_inventory():
	items=count_items()
	random_index = random() * len(items) // 1
	item = items[random_index][0]
	amount = items[random_index][1]
	print(str(item),": ", str(amount))

def print_hats():
	for hat in Hats:
		print(hat)
		do_a_flip()

# Return the Entity and Ground detected at current spot
def scan():
	return get_ground_type(), get_entity_type()

# Quick print the Entity and Ground detected at current spot
def scan_and_quick_print():
	quick_print("Entity: ", get_entity_type())
	quick_print("Ground: ", get_ground_type())

def get_pos():
	return get_pos_x(), get_pos_y()

def quick_print_costs():
	quick_print("Checking all items' cost ... ")
	for entity in database.entities:
		costs = get_cost(entity)

		#all ingredients
		quick_print("All items needed for '",entity,"': ", str(costs))

		#each ingredient
		i = 0
		for cost in (costs):
			i+=1
			quick_print(" - Ingredient [",i,"]: ",str(cost))

		#if num_items(item) < cost[item]:
		#    quick_print(" - ! Not enough ",item," to unlock ",items[item])

#################################################
# MOVEMENT FUNCTIONS
#################################################

# Simple movement, one axis at a time
def move_simple(x, y):
	if (check_bounds(x,y)==False):
		return

	# Align x
	while x != (get_pos_x()):
		if x > get_pos_x():
			move(East)
		else:
			move(West)

	# Align y
	while y != (get_pos_y()):
		if y > get_pos_y():
			move(North)
		else:
			move(South)

# Move a single tile, whatever is available, based on 'right hand rule'
# based on our find_treasure_simple() in maze.py
def navigate():
	facing = drone.facing
	right_dir = static.right_of[facing]
	left_dir  = static.left_of[facing]
	back_dir  = static.right_of[static.right_of[facing]]  # 180°

	# 1. Try right first
	if can_move(right_dir):
		move(right_dir)
		drone.facing = right_dir
		return False

	# 2. Try forward
	elif can_move(facing):
		move(facing)
		return False

	# 3. Try left
	elif can_move(left_dir):
		move(left_dir)
		drone.facing = left_dir
		return False

	# 4. All blocked turn around
	else:
		move(back_dir)
		drone.facing = back_dir

# Based on move_linear_simple, but here we want to move around the blocked area, AND catch move errors
def move_smart(position):
	if (position==None):
		return False
	else:
		x,y=position

	if(check_bounds(x,y)==False):
		# Align x and y, one at a time
		while x != get_pos_x() or y != get_pos_y():
			if x > get_pos_x():
				if(move(East)):
					pass
			elif x < get_pos_x():
				if(move(West)):
					pass
			if y > get_pos_y():
				if(move(North)):
					pass
			elif y < get_pos_y():
				if(move(South)):
					pass
	return True

# Simple, 'Linear-like' movement
def move_linear_simple(x, y):
	if (check_bounds(x,y)==False):
		return

	# Align x and y, one at a time
	while x != get_pos_x() or y != get_pos_y():
		if x > get_pos_x():
			move(East)
		elif x < get_pos_x():
			move(West)

		if y > get_pos_y():
			move(North)
		elif y < get_pos_y():
			move(South)

# Linear movement (true straight-line movement)
def move_linear(position):
	if (position):
		target_x, target_y = position
		cur_x = get_pos_x()
		cur_y = get_pos_y()

		if (check_bounds(target_x, target_y) == False):
			return

		# Calculate deltas
		dx = abs(target_x - cur_x)
		dy = abs(target_y - cur_y)
		if target_x > cur_x:
			step_x = 1
		else:
			step_x = -1

		if target_y > cur_y:
			step_y = 1
		else:
			step_y = -1

		# Error term (used to decide when to step vertically)
		err = dx - dy

		# Continue until we reach target
		while True:
			if cur_x == target_x and cur_y == target_y:
				break

			e2 = err * 2

			# Move horizontally if needed
			if e2 > -dy:
				err -= dy
				cur_x += step_x
				if step_x > 0:
					move(East)
				else:
					move(West)

			# Move vertically if needed
			if e2 < dx:
				err += dx
				cur_y += step_y
				if step_y > 0:
					move(North)
				else:
					move(South)


	if (position == get_pos()):
		return True
	else:
		return False

# Move to a random (x, y) position within world bounds
def move_random():
	x = random() * static.ws // 1
	y = random() * static.ws // 1
	#move_linear_simple(x, y)
	position = x,y
	move_linear(position)

#################################################
# HARVESTING FUNCTIONS
#################################################

# Polyfarming
def polyfarm():
	get_companion_precheck = get_companion()

	if (get_companion_precheck!=None):
		plant_companion, (x,y) = get_companion_precheck
		position = x,y
		move_linear(position)
		harvest()
		if (static.tilling_guide[plant_companion] != get_ground_type()):
			till()
		plant(plant_companion)
		return True
	else:
		return False


# Till
def till_spot(desired_ground,desired_plant):
	if (desired_ground!=get_ground_type()) and (desired_plant!=get_entity_type()):
		till()

#Check and use water if needed
def use_water():
	if get_water()<0.5:
		use_item(Items.Water)


# General forage / smart harvest:
def forage():

	# randomly select a plant/resource
	planting_guide = []
	for pair in static.planting_guide:
		planting_guide.append(pair)
	random_index = random() * len(planting_guide) // 1
	desired_plant = planting_guide[random_index]
	desired_ground = static.planting_guide[desired_plant]

	#Determine spacing based on entity being planted/farmed
	#if (desired_plant==Entities.Cactus or desired_plant==Entities.Tree):
	#	spacing=2 #skip a block
	#else:
	#	spacing=1 #every block
	spacing=1

	# Check and use if water is needed
	use_water()

	ground_at_this_spot = get_ground_type()
	entity_at_this_spot = get_entity_type()

	# Harvest
	#if (entity_at_this_spot==desired_plant):
	harvest()

	# Till and plant
	if (ground_at_this_spot!=desired_ground):
		till()
	plant(desired_plant)
	# Randomly polyfarm
	if (get_companion() and (random()*5//1>=4)):
		polyfarm()

	# make a bigger pumpkin area periodically. Does not account for world edge
	if (desired_plant == Entities.Pumpkin) and ((random()*4//1)>=3):
		move(West)
		harvest()
		if (desired_ground!=get_ground_type()) and (desired_plant!=get_entity_type()):
			till()
		plant(desired_plant)

		move(South)
		harvest()
		if (desired_ground!=get_ground_type()) and (desired_plant!=get_entity_type()):
			till()
		plant(desired_plant)

		move(East)
		harvest()
		if (desired_ground!=get_ground_type()) and (desired_plant!=get_entity_type()):
			till()
		plant(desired_plant)

		move(North) #back to where we started
		if (desired_ground!=get_ground_type()) and (desired_plant!=get_entity_type()):
			till()
		plant(desired_plant)

	use_item(Items.Fertilizer)

	# Determine where to move next ##

	if(desired_plant==Entities.Grass):
		move(North)
	else:
		# See if the next move north puts us over the world line, and go east
		if ((get_pos_y()+spacing)>=(static.ws)):
			for i in range(spacing):
				move(East) #columns

		for i in range(spacing):
			move(North) #rows



# Forage_for: [Desired Harvest/Plant], [Desired Ground], [Fertilize?]
def forage_for(desired_plant, desired_ground, use_fertilizer, flip_to_slow):

	#Determine spacing based on entity being planted/farmed
	if (desired_plant==Entities.Cactus or desired_plant==Entities.Tree):
		spacing=2 #skip a block
	else:
		spacing=1 #every block

	# Check and use if water is needed
	use_water()

	ground_at_this_spot = get_ground_type()
	entity_at_this_spot = get_entity_type()

	# Harvest and plant
	if (entity_at_this_spot==desired_plant):
		harvest()
		plant(desired_plant)

	# Till
	if (ground_at_this_spot!=desired_ground):
		till()

	if (ground_at_this_spot==desired_ground and entity_at_this_spot!=desired_plant):
		plant(desired_plant)
		# randomly polyfarm
		if((random()*2//1 == 2)):
			polyfarm(use_fertilizer)

	if (use_fertilizer):
		use_item(Items.Fertilizer)

	# Determine where to move next ##
	if (spacing>1 and (get_pos_x()%2==0) and get_pos_y()==0):
		move(North)
	elif(desired_plant==Entities.Grass):
		move(North)
	else:
		# See if the next move north puts us over the world line, and go east
		if ((get_pos_y()+spacing)>=(static.ws)):
			for i in range(spacing):
				#move(East) #columns
				if (flip_to_slow):
					do_a_flip()

		for i in range(spacing):
			move(North) #rows



#################################################
# `SELF TEST`
#################################################

# Game must directly `Play` this file to access "__main__"
if __name__ == "__main__":
	quick_print("[go_to] Running self-test...")
	quick_print("World size detected: ", static.ws)
	start_x = get_pos_x()
	start_y = get_pos_y()
	quick_print("Started at (",start_x,",",start_y,")")

	# Random move test
	quick_print("Moving to a random position...")
	move_random()

	# Arrival confirmation
	quick_print("Arrived at (",get_pos_x(),",",get_pos_y(),")")

	# Check the ground
	quick_print("Quick [print] scanning...")
	scan_and_quick_print()
	Ground, Entity = scan()
	quick_print("Scanned objects: ", Ground, ", ", Entity)

	# Back to the start
	quick_print("Moving to original postion using move_linear_simple()...")
	move_linear_simple(start_x,start_y)

	# Arrival confirmation
	quick_print("Arrived at (",get_pos_x(),",",get_pos_y(),")")

	# Random move test
	quick_print("Moving to a new random position...")
	move_random()

		# Arrival confirmation
	quick_print("Arrived at (",get_pos_x(),",",get_pos_y(),")")

	# Back to the start
	quick_print("Moving back to original postion using move_linear()...")
	position=start_x,start_y
	move_linear(position)

	# Arrival confirmation
	quick_print("Arrived at (",get_pos_x(),",",get_pos_y(),")")

	#@TODO harvest tests

# do.py
# ===============================================
# Contains a lot of bassic, re-usable functions
# Movement, harvesting, scanning the area, etc.
# Needs regular cleaning and refactoring. And
# pairing down and modularizing .. :S
# ===============================================

import static
import database

#################################################
# COMMON FUNCTIONS
#################################################

# Validate coordinates are in world bounds
def check_bounds(x, y):
	return not (x < 0 or y < 0 or x >= static.ws or y >= static.ws)

# Return a random coordinate in the world
def gen_random_pos():
	x = random() * static.ws // 1
	y = random() * static.ws // 1
	return x, y

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

# Dinosaur-mode toggle
def toggle_dino_mode():
	if database.dino_mode_enabled == False:
		change_hat(Hats.Dinosaur_Hat)
		database.dino_mode_enabled = True
	else:
		change_hat(Hats.Pumpkin_Hat)
		database.dino_mode_enabled = False

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

def till_spot(desired_ground,desired_plant):
	if (desired_ground!=get_ground_type()) and (desired_plant!=get_ground_type()):
		till()

def full_till():
	for i in range(static.ws):
		for i in range(static.ws):
			use_water()
			till()
			move(North)
		move(East)

def use_water():
	if get_water()<0.5:
		use_item(Items.Water)

# Full Plant: [Desired Plant], [Desired Ground], [Fertilize], [Spacing]
def full_plant(desired_plant, desired_ground, use_fertilizer, spacing):
	# Plant
	if (get_entity_type()!=desired_plant) and (get_entity_type()!=desired_ground):
		for i in range(static.ws/spacing):
			for i in range(static.ws/spacing):
				till_spot(desired_ground,desired_plant)
				plant(desired_plant)
				use_water()
				if use_fertilizer:
					use_item(Items.Fertilizer)

				for i in range(spacing):
					move(North)
			for i in range(spacing):
				move(East)

# Full Harvest: [Desired Harvest/Plant], [Desired Ground], [Fertilize], [Spacing]
def full_harvest(desired_plant, desired_ground, use_fertilizer, spacing):
	if (desired_plant==get_entity_type()) or (get_entity_type()==Entities.Dead_Pumpkin):
		for i in range(static.ws/spacing):
			for i in range(static.ws/spacing):
				till_spot(desired_ground,desired_plant)
				harvest()
				use_water()
				for i in range(spacing):
					move(North)
			for i in range(spacing):
				move(East)

# Full Plant and Harvest: [Desired Harvest/Plant], [Desired Ground], [Fertilize], [Spacing]
def full_plant_and_harvest(desired_plant, desired_ground, use_fertilizer, spacing, loops):
	for i in range(loops):
		full_plant(desired_plant, desired_ground, use_fertilizer, spacing)
		full_harvest(desired_plant, desired_ground, use_fertilizer, spacing)


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

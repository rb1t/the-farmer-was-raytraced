# drone.py
# ===============================================
# 4 drones acting concurrently (time-sliced)
# ===============================================

import do
import database
import static
import maze
global id
drone_id = 0

def and_clone():
	if num_drones() <= static.max_available_drones:
		print("Spawned Drone: ", str(drone_id))
		run(drone_id)

def run(drone_id):
	id=drone_id+1
	while id < static.max_available_drones:
		if spawn_drone(and_clone):
			return True
		else:
			# Let's have some face different directions to speed up exploration
			# Each drone will do this when no more drones can be spawned
			if maze.find_treasure_simple():
				clear()
				if Items.Power <= 200:
					if drone_id == 1:
						move(North)
					do.full_plant_and_harvest(Entities.Sunflower, Grounds.Soil, True, 2, 4)
				else:
					maze.build(0)
					run()
			return False

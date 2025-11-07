# drone.py
# ===============================================
# 4 drones acting concurrently (time-sliced)
# ===============================================
import do
import database
import static
import maze

last_position = 0,0 #not using atm...
facing = North #set initial direction

def determine_priority():

	# Check sufficient resources
	# ...
	#always do for now / simulate condition is met for cactus

	do.smart_harvest(Entities.Grass, Grounds.Grassland, False)
	#do.smart_harvest(Entities.Tree, Grounds.Grassland, False)
	#do.smart_harvest(Entities.Carrot, Grounds.Soil, False)
	#do.smart_harvest(Entities.Pumpkin, Grounds.Soil, False)
	#do.smart_harvest(Entities.Cactus, Grounds.Soil, False)

	# Check for specific objective # database.mode = ["Farm","Maze","Dino"]
	# ...

	# Other
	# ...

	# Test stuff --------------
	#do.move_random()
	#harvest()

	#maze.build(0)
	#while not maze.find_treasure_simple():
	#	pass

	# quick print our inventory
	#items = do.count_items()
	#for (item, amount) in items:
	#	quick_print(str(item),", Qty.:", str(amount))
	#	pass

	#print random item in game
	#do.print_random_inventory()

def spawn_and_work():
	# just putting drones into a self-goverened loop for now
	while True:
		# getting all drones out, later we can have logic to spawn only as needed
		while num_drones() < static.max_available_drones:
			spawn_drone(spawn_and_work)
		determine_priority()
		#run each loop, for each drone
	pass

def retire():
	pass

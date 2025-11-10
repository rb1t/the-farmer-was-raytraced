# drone.py
# ===============================================
# 4 drones acting concurrently (time-sliced)
# ===============================================
import do
import database
import static
import maze
import dino

last_position = 0,0 #not using atm...
facing = North #set initial direction

def determine_priority(id): #looped in spawn_and_work():

	my_id = id

	# ------------------------------------------------
	# Mazes: build and search
	# ------------------------------------------------

	#maze.solve()

	# ------------------------------------------------
	# Dino mode
	# ------------------------------------------------

	dino.grow_tail()

	# ------------------------------------------------
	# Harvesting
	# ------------------------------------------------

	#do.forage()

	#harvest everything contained in our static list
	# target = 10000000
	# for plant in static.planting_guide:
	# 	ground = static.planting_guide[plant]
	# 	item = static.harvesting_guide[plant]
	# 	while num_items(item) < target:
	# 		do.forage_for(plant, ground, False)


	#do.forage_for(Entities.Grass, Grounds.Grassland, False)
	#do.forage_for(Entities.Tree, Grounds.Grassland, True)
	#do.forage_for(Entities.Carrot, Grounds.Soil, False)
	#do.forage_for(Entities.Pumpkin, Grounds.Soil, False)
	#do.forage_for(Entities.Cactus, Grounds.Soil, False)
	#do.move_random()
	#harvest()

	# ------------------------------------------------
	# Other
	# ------------------------------------------------

	# quick print our inventory
	#items = do.count_items()
	#for (item, amount) in items:
	#	quick_print(str(item),", Qty.:", str(amount))
	#	pass

	#print random item in game
	#do.print_random_inventory()

def spawn_and_work():

	#-------
	# Next few lines are basically each individual drone's initilization
	calibrate_num_drones = num_drones()
	id = (calibrate_num_drones-1)*1 #multiply by spacing
	spread_position = id,0
	do.move_linear(spread_position) # Spread out the drones based around the origin, x-axis only
	do_a_flip()
	#quick_print("My id:", str(id))

	# just putting drones into a self-goverened loop for now
	while True:
		# getting all drones out, later we can have logic to spawn only as needed
		while num_drones() < (static.max_available_drones): #### can lower drone count artificially
			spawn_drone(spawn_and_work)
		determine_priority(id)#run each loop, for each drone
	pass

def retire():
	pass

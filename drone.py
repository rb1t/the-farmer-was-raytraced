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

def determine_priority(): #looped in spawn_and_work():

	#maze.build(0)
	#while not maze.find_treasure_simple():
	#	pass

	#harvest everything contained in our static list
	# target = 10000000
	# for plant in static.planting_guide:
	# 	ground = static.planting_guide[plant]
	# 	item = static.harvesting_guide[plant]
	# 	while num_items(item) < target:
	# 		do.forage_for(plant, ground, False)

	do.forage()

	#do.forage(Entities.Grass, Grounds.Grassland, False)
	do.forage_for(Entities.Tree, Grounds.Grassland, False)
	#do.forage(Entities.Carrot, Grounds.Soil, False)
	#do.forage(Entities.Pumpkin, Grounds.Soil, False)
	#do.forage(Entities.Cactus, Grounds.Soil, False)


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
			#do.move_random() #spread out randomly
			spawn_drone(spawn_and_work)
		determine_priority()
		#run each loop, for each drone
	pass

def retire():
	pass

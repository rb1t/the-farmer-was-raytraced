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

def determine_priority(id): #looped in spawn_and_work():

	my_id = id
	#Maze builder: Try finding treasure, and if it fails, build maze.
	if not maze.find_treasure_simple() and (get_entity_type()!=Entities.Grass) and (get_entity_type()!=Entities.Bush):

		#move randomly to cover the maze
		#if (random()*num_drones()//1 >= (num_drones()-2)):
		#	move(East)
		#	move(East)
		#	move(North)
		#	move(North)

		# Add some randomness to even numbered drones drones moving in unusual directions (not all drones)
		if ((my_id)%2==0 and ((random()*5//1)>=4)):
			change_hat(Hats.Brown_Hat)
			move(North)
			if(maze.check_treasure()):
				use_item(Items.Weird_Substance,(static.ws*2))
			move(North)
			if(maze.check_treasure()):
				use_item(Items.Weird_Substance,(static.ws*2))
			move(North)
			if(maze.check_treasure()):
				use_item(Items.Weird_Substance,(static.ws*2))
			move(East)
			if(maze.check_treasure()):
				use_item(Items.Weird_Substance,(static.ws*2))
			move(East)
			if(maze.check_treasure()):
				use_item(Items.Weird_Substance,(static.ws*2))

		# Every nth drone (or random num) will try to move directly to the treasure
		elif ((my_id)%9==0 or ((random()*33//1)>=32)):
			# Add some random movement once in a while to hope and get unstuck
			if ((random()*7//1)>=6):
				do.move_random()
			change_hat(Hats.Wizard_Hat)
			treasure_pos=measure()
			do.move_linear(treasure_pos)

		# Every nth drone moves weirdly
		elif ((my_id)%6==0 and ((random()*5//1)>=4)):
			change_hat(Hats.Brown_Hat)
			move(West)
			if(maze.check_treasure()):
				use_item(Items.Weird_Substance,(static.ws*2))
			move(West)
			if(maze.check_treasure()):
				use_item(Items.Weird_Substance,(static.ws*2))
			move(South)
			if(maze.check_treasure()):
				use_item(Items.Weird_Substance,(static.ws*2))
			move(South)
			if(maze.check_treasure()):
				use_item(Items.Weird_Substance,(static.ws*2))

		# Add some random movement once in a while to hope and get unstuck
		elif ((random()*66//1)>=65):
			change_hat(Hats.Cactus_Hat)
			do.move_random()

		else:
			change_hat(Hats.Gold_Hat) #Normies - these drones don't have a special task yet
		#	maze.find_treasure_simple()

		maze.find_treasure_simple()
	else:
		maze.build(0)

	#harvest everything contained in our static list
	# target = 10000000
	# for plant in static.planting_guide:
	# 	ground = static.planting_guide[plant]
	# 	item = static.harvesting_guide[plant]
	# 	while num_items(item) < target:
	# 		do.forage_for(plant, ground, False)

	#do.forage()

	#do.forage_for(Entities.Grass, Grounds.Grassland, False)
	#do.forage_for(Entities.Tree, Grounds.Grassland, True)
	#do.forage_for(Entities.Carrot, Grounds.Soil, False)
	#do.forage_for(Entities.Pumpkin, Grounds.Soil, False)
	#do.forage_for(Entities.Cactus, Grounds.Soil, False)
	#do.move_random()
	#harvest()

	# quick print our inventory
	#items = do.count_items()
	#for (item, amount) in items:
	#	quick_print(str(item),", Qty.:", str(amount))
	#	pass

	#print random item in game
	#do.print_random_inventory()

def spawn_and_work():

	#Spread out the drones based around the origin, x-axis only
	calibrate_num_drones = num_drones()
	id = (calibrate_num_drones-1)*1 #multiply by spacing
	spread_position = id,0
	do.move_linear(spread_position)
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

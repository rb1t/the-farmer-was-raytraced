# drone.py
# ===============================================
# 4 drones acting concurrently (time-sliced)
# ===============================================
import do
import database
import static
import maze
import dino
import cactus

last_position = 0,0 #not using atm...
facing = North #set initial direction
id = 0

def determine_priority(my_id): #looped in spawn_and_work():

	id = my_id

	if id >= num_drones():
		print("id overflow :", str(id))
		do_a_flip()
		print("id overflow :", str(id))
		do_a_flip()

	# ------------------------------------------------
	# Mazes: build and search
	# ------------------------------------------------
	# current_entity = get_entity_type()
	# if id==0 and current_entity!=Entities.Hedge and current_entity!=Entities.Treasure: #only need one builder
	# 	maze.build(0)
 #
	# # #experimental maze hunting
	# if(maze.solve(0)):
	# 	print("Drone ",id," here, maze runner!")

	# ---

	#straightforward maze hunting
	#maze.find_treasure_simple()

	# ------------------------------------------------
	# Dino mode (only one dino hat)
	# ------------------------------------------------
	#if (my_id == 0):
	#	dino.grow_tail_zigzag()

	# ------------------------------------------------
	# Harvesting
	# ------------------------------------------------

	#do.forage() #General, does all plants

	# Desired Plant, Desired ground type, Fertilize?, Flip at end to slow?
	#do.forage_for(Entities.Grass, Grounds.Grassland, False, False)
	#do.forage_for(Entities.Tree, Grounds.Grassland, True, True)
	#do.forage_for(Entities.Carrot, Grounds.Soil, True, False)
	#do.forage_for(Entities.Pumpkin, Grounds.Soil, False, False)
	do.forage_for(Entities.Sunflower, Grounds.Soil, True, True)
	#do.forage_for(Entities.Cactus, Grounds.Soil, True, False)

	# ------------------------------------------------
	# Cactus sorting and farminfox newsg
	# ------------------------------------------------

	#if(cactus.solve(id)): #Pass in this drone's id to solve (uses multi drones)
	#	harvest()
	#	print("Drone ", id ," verified the cactus sorting!")
	#	do.move_linear_simple(id,0)

	# ------------------------------------------------
	# Other
	# ------------------------------------------------
	# 32x32 pumpking
	#do.big_pumpkin()

	# Periodically print a drone's "id"
	#if(random()*10000//1>=9950):
	# 	print ("I am drone #", str(my_id))

	# Wear a hat based on id
	if id == 0: #first drone
		change_hat(Hats.The_Farmers_Remains)
	elif id == (num_drones()-1): #last drone
		change_hat(Hats.Top_Hat)
	elif id > (num_drones()-1): #shouldn't be a drone this high!
		change_hat(Hats.Brown_Hat)

def spawn_and_work():
	#-------
	# Next few lines are basically each individual drone's initilization (only done once per drone)
	calibrate_num_drones = num_drones()
	my_id = (calibrate_num_drones-1)*1 #multiply by spacing
	#quick_print("My id:", str(id))
	do_a_flip() #a flip seems to help let the drones all deploy properly

	spread=True #If we want them to spread out or stay put (latter mainly for maze)
	if spread==True:
		spread_position = my_id,0
		do_a_flip() #a second flip seems to get them to the correct x (for their id) position every time
		do.move_linear(spread_position) # Spread out the drones on the first row, (y=0)

	# just putting drones into a self-goverened loop for now
	while True:
		# getting all drones out, later we can have logic to spawn only as needed
		while num_drones() < (static.max_available_drones): ### can lower max drone count artificially
			spawn_drone(spawn_and_work)
		determine_priority(my_id)#run each loop, for each drone
	pass

def retire():
	pass

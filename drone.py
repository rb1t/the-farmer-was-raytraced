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

maze_size=32
set_world_size(maze_size)

def determine_priority(my_id): #looped in spawn_and_work():

	id = my_id

	#There should never be a drone id larger than the allowed number of drones (starting at 0)
	# if id >= num_drones():
	# 	print("id overflow :", str(id))
	# 	do_a_flip()
	# 	print("id overflow :", str(id))
	# 	do_a_flip()

	# ------------------------------------------------
	# Mazes: build and search
	# ------------------------------------------------
	# treasure_opened = False
	# open_rate=66.22 # out of 100, floating (higher number = higher chance)
	# current_entity = get_entity_type()
	# if current_entity!=Entities.Hedge and current_entity!=Entities.Treasure:
	# 	database.gold_at_start = num_items(Items.Gold) # reset our gold counter
	# 	treasure_opened = False
	# 	if get_pos_x()>=maze_size or get_pos_y()>=maze_size:
	# 		do.move_linear_simple((maze_size-1),(maze_size-1)) #Make
	# 	elif id==0: #only need one builder
	# 		start = 0,0
	# 		#do.move_linear(start)
	# 		maze.build(maze_size)
	# elif(maze.solve(maze_size,open_rate,id)):
	# 	treasure_opened = True
	# 	#print("Drone ",id," found the treasure!")
 #
	# #if the drone 0 found treasure, or is not in the maze, it's time to calculate earned gold
	# if (treasure_opened == True):
	# 	gold_earned = num_items(Items.Gold) - database.gold_at_start
	# 	quick_print("Gold farmed: ", gold_earned)
	# 	treasure_opened = False

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
	#do.forage_for(Entities.Sunflower, Grounds.Soil, True, True)
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
	do.big_pumpkin(id)

	# Periodically print a drone's "id"
	#if(random()*10000//1>=9950):
	# 	print ("I am drone #", str(my_id))

	# Wear a hat based on id
	#if id == 0: #first drone
	#	change_hat(Hats.Wizard_Hat)
	#elif id == (num_drones()-1): #last drone
	#	change_hat(Hats.Top_Hat)
	if id > (num_drones()-1): #shouldn't be a drone this high!
		change_hat(Hats.The_Farmers_Remains)

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
			spawn_drone(spawn_and_work) #pass in itself so each drone can spawn the next, if possible
		determine_priority(my_id)#run each loop, for each drone
	pass

def retire():
	pass

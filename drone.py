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

	#maze.build(0)
	#maze.solve()

	# ------------------------------------------------
	# Dino mode (only one dino hat)
	# ------------------------------------------------
	#if (my_id == 0):
	#	dino.grow_tail_zigzag()

	# ------------------------------------------------
	# Harvesting
	# ------------------------------------------------

	do.forage() #General, does all plants

	# Desired Plant, Desired ground type, Fertilize?, Flip at end to slow?
	#do.forage_for(Entities.Grass, Grounds.Grassland, False, False)
	#do.forage_for(Entities.Tree, Grounds.Grassland, True, True)
	#do.forage_for(Entities.Carrot, Grounds.Soil, True, False)
	#do.forage_for(Entities.Pumpkin, Grounds.Soil, False, False)
	#do.forage_for(Entities.Sunflower, Grounds.Soil, True, True)
	#do.forage_for(Entities.Cactus, Grounds.Soil, True, False)

	# ------------------------------------------------
	# Other
	# ------------------------------------------------
	#Periodically print a drone's "id"
	#if(random()*10000//1>=9950):
	#	do_a_flip()
	#	print ("I am drone #", str(my_id))

def spawn_and_work():

	#-------
	# Next few lines are basically each individual drone's initilization (only done once per drone)
	calibrate_num_drones = num_drones()
	id = (calibrate_num_drones-1)*1 #multiply by spacing
	spread_position = id,0
	do.move_linear(spread_position) # Spread out the drones based around the origin, x-axis only
	do_a_flip()
	do_a_flip() #a second flip seems to get them to calibrate better
	#quick_print("My id:", str(id))

	# just putting drones into a self-goverened loop for now
	while True:
		# getting all drones out, later we can have logic to spawn only as needed
		while num_drones() < (static.max_available_drones): ### can lower max drone count artificially
			spawn_drone(spawn_and_work)
		determine_priority(id)#run each loop, for each drone
	pass

def retire():
	pass

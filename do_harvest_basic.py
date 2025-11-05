clear()
## farm_list=[Pumpkin,Cactus,...]

def till_pass():
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			use_water()
			till()
			move(North)
		move(East)

def use_water():
	if get_water()<0.5:
		use_item(Items.Water)
		#print("WATER USED: ", get_water())
		
		
def do_harvest(spacing, desired_ground,desired_harvest,desired_plant):
	# Harvest
	if (desired_harvest==get_entity_type()) or (get_entity_type()==Entities.Dead_Pumpkin):
		for i in range(get_world_size()):
			for i in range(get_world_size()/spacing):
				use_water()
				harvest()
				for i in range(spacing):
					move(North)
			move(East)
	# Till
	if (desired_ground!=get_ground_type()) and (desired_harvest!=get_ground_type()):		 
		while(desired_ground!=get_ground_type()):
			till_pass()

	# Plant
	if (desired_plant!=None and get_entity_type()!=desired_plant) and (get_entity_type()!=desired_ground):
		for i in range(get_world_size()):			
			for i in range(get_world_size()/spacing):
				use_water()
				plant(desired_plant)
				for i in range(spacing):
					move(North)
			move(East)
	

for i in range(1000):
	do_a_flip()
	
	# Hay/Grass
	do_harvest(1, Grounds.Grassland, Entities.Grass, None)
	do_harvest(1, Grounds.Grassland, Entities.Grass, None)
	
	# Trees
	do_harvest(3, Grounds.Soil, Entities.Tree, Entities.Tree)
	do_harvest(3, Grounds.Soil, Entities.Tree, Entities.Tree)
	do_harvest(3, Grounds.Soil, Entities.Tree, Entities.Tree)
	do_harvest(3, Grounds.Soil, Entities.Tree, Entities.Tree)
	
	# Sunflowers
	do_harvest(1, Grounds.Soil, Entities.Sunflower, Entities.Sunflower)
	do_harvest(1, Grounds.Soil, Entities.Sunflower, Entities.Sunflower)
	
	# Cacti
	do_harvest(1, Grounds.Soil, Entities.Cactus, Entities.Cactus)
	do_harvest(1, Grounds.Soil, Entities.Cactus, Entities.Cactus)

	# Pumpkins
	do_harvest(1, Grounds.Soil, Entities.Pumpkin, Entities.Pumpkin)
	do_harvest(1, Grounds.Soil, Entities.Pumpkin, Entities.Pumpkin)

	

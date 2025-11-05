# main.py
# ===============================================
# Main game loop
# ===============================================

import database
import static
import do
import maze

## START FRESH
#clear()

## INIT STUFF
#do.maze_scan_impasses()
change_hat(Hats.Wizard_Hat)
		
## MAIN LOOP
def main():
	total_passes = -1 #set to -1 for infinite loop, 0 or greater for static repitions
	while total_passes == -1 or total_passes > 0:
		# Maze routine
		if(num_items(Items.Power)<= 50):
			do.full_plant_and_harvest(Entities.Sunflower, Grounds.Soil, True, 2, 1)
		maze.build(0)
		while not maze.find_treasure_simple():
			pass

		# Move to every cell in our global cell array, 1 by 1
		#for cell in database.world_cells:
		#	do.move_linear(cell["position"])

		# Planing functions
		#do.full_plant(Entities.Grass, Grounds.Grassland, False, 1)
		#do.full_harvest(Entities.Grass, Grounds.Grassland, False, 1)
		#do.full_plant_and_harvest(Entities.Carrot, Grounds.Soil, False, 1, 1)
		#do.full_plant_and_harvest(Entities.Grass, Grounds.Grassland, False, 1, 1)
		#do.full_plant_and_harvest(Entities.Bush, Grounds.Grassland, True, 1, 1)
		#do.full_plant_and_harvest(Entities.Tree, Grounds.Soil, True, 1, 1)
		#do.full_plant_and_harvest(Entities.Sunflower, Grounds.Soil, True, 2, 1)
		#do.full_plant_and_harvest(Entities.Cactus, Grounds.Soil, False, 2, 1)
		#do.full_plant_and_harvest(Entities.Pumpkin, Grounds.Soil, False, 1, 1)

		if total_passes > 0:
			total_passes -= 1

main()

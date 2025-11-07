# main.py
# ===============================================
# Main game loop
# ===============================================

import database
import static
import do
import maze

## START FRESH
clear()

## INIT STUFF
change_hat(Hats.Wizard_Hat)

## MAIN LOOP
def main():
	total_passes = -1 #set to -1 for infinite loop, 0 or greater for static repitions
	while total_passes == -1 or total_passes > 0:

		# Move to every cell in our global cell array, 1 by 1
		#for cell in database.world_cells:
		#	do.move_linear(cell["position"])

		if total_passes > 0:
			total_passes -= 1

main()

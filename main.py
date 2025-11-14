# main.py
# ===============================================
# Main game loop
# ===============================================

# IMPORTS
import drone

## START FRESH?
#clear()

## INIT STUFF
#change_hat(Hats.Wizard_Hat)

## MAIN LOOP
def main():
	total_passes = -1 #set to -1 for infinite loop, 0 or greater for static repitions
	while total_passes == -1 or total_passes > 0:

		drone.spawn_and_work()

		if total_passes > 0:
			total_passes -= 1

main()

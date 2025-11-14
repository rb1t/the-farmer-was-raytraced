# drone.py
# ===============================================
# Stuff related to the snake-like Dinosaur minigame
# ===============================================

import static
import do

# Temporary, local worldsize just for testing
ws=32 # for testing. reminder: should be 1 less than actual worldsize (when starting from 0).


def grow_tail():
	#@TODO This is only a placeholder, need to build out
	change_hat(Hats.Dinosaur_Hat)
	while True:
		apple_pos=measure()
		#quick_print(apple_pos)
		if(do.move_linear(apple_pos)):
			pass
		else:
			change_hat(Hats.Gold_Hat)
			change_hat(Hats.Dinosaur_Hat)

# @TODO even for simple zigzag, this needs some cleanup
#  Requires even number to solve currently.
def grow_tail_zigzag():

	#@TODO cleanup and move some of this into do/static/etc. if I end up using
	x_directions = {"Left":West, "Right":East}
	cur_heading = x_directions["Right"]

	change_hat(Hats.Dinosaur_Hat)
	tail_size = 0 # used to move the snake as the tail grows
	#starting_pos = do.get_pos() #track where we started before moving
	steps = 0 # how many tiles we walked across while solving
	facing=East # to know if i just switched to a new row or not

	while True:
		#pos = do.get_pos() #track where we started before moving
		pos_x = get_pos_x()
		pos_y = get_pos_y()

		if (get_entity_type()==Entities.Apple):
			tail_size+=1 # i.e., apples eaten

		# zigzag round, start with heading east
		# we're adding +1 to have the first row (e.g., a point like 0,0) be "row 1"

		# East & North - on odd  at the start, move east but leave one space for tail
		if facing==East:
			if (move(East)):
				pass
			elif(move(North)):
				facing = West
			elif facing == East: #must be at the end, time to make steps towards starting the loop over
				facing = South
				quick_print("Couldn't move East (or North)")
		#West & North
		elif facing==West:
			if(((pos_x > 1) or (pos_y==ws-1 and pos_x>0)) and move(West)):
				pass
			elif(move(North)):
				facing = East
			elif facing == West: #must be at the end, time to make steps towards starting the loop over
				facing = South
			else:
				quick_print("Couldn't move West (or North)")
		# Move south, on the east column, to reset
		elif facing == South:
			if (move(South)):
				pass
			elif(move(East)):
				facing = East
			elif(move(West)):
				facing = West
			elif not move(South) and not move(North): #Can't move anywhere? Start over
				change_hat(Hats.Gold_Hat)
				do.move_linear_simple(0,0)
				change_hat(Hats.Dinosaur_Hat)
			else:
				quick_print("Couldn't move South (Anywhere really)")

		# if pos_x == 0 and pos_y == 0 or (pos_x==0 and pos_y==ws-1):
		# 	print("Facing: ", str(facing))
		steps+=1
	print(str(do.get_pos()), " - Apples: ", str(apples_eaten), " - Steps: ",str(steps))

#################################################
# `SELF TEST`
#################################################

# Game must directly `Play` this file to access "__main__"
if __name__ == "__main__":
	clear()
	set_world_size(ws)
	grow_tail_zigzag()

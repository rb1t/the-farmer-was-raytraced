import static
import do


#
def grow_tail():
	change_hat(Hats.Dinosaur_Hat)


	while True:
		apple_pos=measure()
		quick_print(apple_pos)
		if(do.move_linear(apple_pos)):
			pass
		else:
			change_hat(Hats.Gold_Hat)
			change_hat(Hats.Dinosaur_Hat)


	# while True:
	# 	if (do.move_linear(apple_pos)):
	# 		print ("True")
	# 	elif (random()*100//1>=33):
	# 		do.move_random()

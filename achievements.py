# achievements.py
# ===============================================
# I thought it'd be fun to have a single file
# that can unlock all Steam Achievements. I also
# thought it could be a good learning tool.
# THIS NEEDS A LOT OF WORK :)
# ===============================================

# "Higher-Order Programming - Pass a function as an argument to a function"
def square(x):
	return x * x

def cube(x):
	return x * x * x

def my_map(func, data):
	result = []
	for item in data:
		result.append(func(item))
	return result

def higher_order_programming():
	numbers = [1, 2, 3, 4, 5]
	print(my_map(square, numbers)) # -> [1, 4, 9, 16, 25]

	cubed_numbers = my_map(cube, numbers)
	for i in range(len(cubed_numbers)):
		quick_print(numbers[i], " cubed is ", cubed_numbers[i])



#################################################
#
# EXAMPLES
# Uncomment each line to unlock that achievement.
#################################################

# higher_order_programming() # Higher-Order Programming

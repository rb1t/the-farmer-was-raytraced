# cell.py
# ===============================================
# Defines a single "cell" in the world grid.
# Each cell tracks information about itself.
# ===============================================

id = 0                            # unique integer ID
position = 0,0                    # (x, y)
ground_type = Grounds.Grassland   # e.g. Ground.Soil, Ground.Rock, etc.
entity_type = Entities.Grass      # e.g. Entities.Pumpkin, Entities.Tree
fertilized = False                # boolean
plant_timer = 0


def set_plant__timer():
	#plant_timer = get_time()
	pass

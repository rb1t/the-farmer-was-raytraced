# static.py
# ===============================================
# Vars that should not change, at least once init
# ===============================================
ws=get_world_size()
right_of = {North: East, East: South, South: West, West: North}
left_of  = {North: West, West: South, South: East, East: North}
max_available_drones = max_drones()
items = {
		Items.Hay,
		Items.Wood,
		Items.Carrot,
		Items.Pumpkin,
		Items.Cactus,
		Items.Bone,
		Items.Weird_Substance,
		Items.Water,
		Items.Fertilizer,
		Items.Power
		}
entities = {
		Entities.Apple,
		Entities.Bush,
		Entities.Cactus,
		Entities.Carrot,
		Entities.Dead_Pumpkin,
		Entities.Dinosaur,
		Entities.Grass,
		Entities.Pumpkin,
		Entities.Sunflower,
		Entities.Tree,
}

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
		Items.Power,
		Items.Bone,
		Items.Weird_Substance,
		Items.Water,
		Items.Fertilizer,
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
tilling_guide = {
		Entities.Grass: Grounds.Grassland,
		Entities.Bush: Grounds.Grassland,
		Entities.Tree: Grounds.Grassland,
		Entities.Carrot: Grounds.Soil,
		Entities.Pumpkin: Grounds.Soil,
		Entities.Cactus: Grounds.Soil,
		Entities.Sunflower: Grounds.Soil
}
planting_guide = {
		Entities.Grass: Grounds.Grassland,
		Entities.Tree: Grounds.Grassland,
		Entities.Carrot: Grounds.Soil,
		Entities.Pumpkin: Grounds.Soil,
		Entities.Cactus: Grounds.Soil,
		Entities.Sunflower: Grounds.Soil
}
harvesting_guide = {
		Entities.Grass: Items.Hay,
		Entities.Tree: Items.Wood,
		Entities.Carrot: Items.Carrot,
		Entities.Pumpkin: Items.Pumpkin,
		Entities.Cactus: Items.Cactus,
		Entities.Sunflower: Items.Power
}

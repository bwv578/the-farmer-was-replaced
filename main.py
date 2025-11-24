import preset
import auto

plan_1 = [
	[Entities.Bush, [0, 0], [2, 2]],
	[Entities.Carrot, [2, 3], [0, 5]],
	[Entities.Pumpkin, [3, 5], [5, 0]],
]

plan_2 = [
	[Entities.Bush, [5, 0], [4, 1]],
	[Entities.Carrot, [4, 2], [5, 5]],
	[Entities.Bush, [3, 5], [0, 2]],
	[Entities.Grass, [0, 1], [3, 0]]
]

plan_carrot = [
	[Entities.Carrot, [0,0], [5, 5]]
]

while not can_harvest():
	entity = get_entity_type()
	if(entity==None or entity==Entities.Dead_Pumpkin):
		plant(Entities.Grass)
	print('빨리좀 자라라')

#preset.all_pumpkin()
	
#while True:
	#auto.plant_blueprint(plan_1)
	#auto.plant_blueprint(plan_2)
	#auto.plant_blueprint(plan_carrot)
	#auto.plant_trees(Entities.Carrot)

clear()
preset.carrot_and_tree()
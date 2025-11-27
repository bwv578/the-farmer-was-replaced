import auto


def pray():
	while not can_harvest():
		entity = get_entity_type()
		if(entity==None or entity==Entities.Dead_Pumpkin):
			plant(Entities.Grass)
			print('빨리좀 자라라')
	
	
def all_pumpkin():
	blueprint = [
		[Entities.Pumpkin, [0, 0], [15, 15]]
	]
	
	while True:
		auto.plant_blueprint(blueprint)


def all_carrot():
	lueprint = [
		[Entities.Carrot, [0, 0], [15, 15]]
	]
	
	while True:
		auto.plant_blueprint(blueprint)


def carrot_and_tree():
	while True:
		auto.plant_trees(Entities.Carrot)
	
	
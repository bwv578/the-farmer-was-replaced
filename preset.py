import auto


def all_pumpkin():
	blueprint = [
		[Entities.Pumpkin, [0, 0], [15, 15]]
	]
	
	while True:
		auto.plant_blueprint(blueprint)
		move(North)
		move(East)


def all_carrot():
	lueprint = [
		[Entities.Carrot, [0, 0], [15, 15]]
	]
	
	while True:
		auto.plant_blueprint(blueprint)
		move(North)
		move(East)
		
def carrot_and_tree():
	while True:
		auto.plant_trees(Entities.Carrot)
	
	
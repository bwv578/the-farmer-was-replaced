import auto

clear()
while not can_harvest():
	print('ㅗ^^ㅗ')

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

auto.plant_blueprint(plan_1)

clear()
while not can_harvest():
	print('ㅗ^^')

auto.plant_blueprint(plan_2)
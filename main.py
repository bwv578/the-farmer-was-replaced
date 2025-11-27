import preset
import auto

complex_16x16 = [
	{
		'entity': Entities.Bush,
		'start': [0, 0],
		'end': [2, 2]
	},
	{
		'entity': Entities.Pumpkin,
		'start': [0, 15],
		'end': [7, 7]
	},
	{
		'entity': Entities.Carrot,
		'start': [15, 15],
		'end': [9, 3]
	},
	{
		'entity': Entities.Cactus,
		'start': [15, 0],
		'end': [3, 2]
	},
	{
		'entity': Entities.Cactus,
		'start': [8, 15],
		'end': [8, 3]
	},
	{
		'entity': Entities.Sunflower,
		'start': [0, 6],
		'end': [7, 3]
	}
]

preset.pray()
while True:
	auto.plant_blueprint(complex_16x16)
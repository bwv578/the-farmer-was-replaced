import preset
import harv
import maze

import advanced


#auto.pray()
#while True:
	#harv.plant_blueprint(preset.complex_16x16)
	#harv.plant_blueprint(preset.complex_22x22)
	#harv.plant_blueprint(preset.all_carrot)
	#harv.plant_blueprint(preset.all_pumpkin)
	
	#maze.open()
	#maze.solve()

maze.open()
maze_map = maze.explore()
print(maze_map)


import preset
import harv
import maze
import glob

import advanced


#auto.pray()
#while True:
	#harv.plant_blueprint(preset.complex_16x16)
	#harv.plant_blueprint(preset.complex_22x22)
	#harv.plant_blueprint(preset.all_carrot)
	#harv.plant_blueprint(preset.all_pumpkin)
	
	#maze.open()
	#maze.solve()

#maze.open()
	
for i in range(50):
	maze.open()
	maze_map = maze.explore()
	maze.solve_node(maze_map)
	if((get_pos_x(), get_pos_y())==measure()):
		quick_print('성공')
	else:
		quick_print('실패')
	harvest()
	
#maze_map = maze.explore()
#maze.solve_node(maze_map)
#harvest()
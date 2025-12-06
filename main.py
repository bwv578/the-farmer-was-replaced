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
	
	
# test - 랜덤위치에서 시작 x50회
for i in range(50):
	maze.open()
	maze_map = maze.explore()
	
	maze.go_random_loc()
	print('여기서 시작')
	
	maze.solve_node(maze_map)
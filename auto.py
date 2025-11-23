import util
import advanced
import movement


def get_dir(x, y):
	directions = []
	
	if(util.is_negative(get_pos_x()-x)):
		directions.append(East)
	else:
		directions.append(West)
	
	if(util.is_negative(get_pos_y()-y)):
		directions.append(North)
	else:
		directions.append(South)
	
	return directions


def plant_row(item, len, dir) : 	
	for i in range(len):
		advanced.a_harvest(item)
				
		if(not i==(len-1)):
			move(dir)
		

def plant_area(items, start, end) :
	
	movement.go_point(start[0], start[1])
	
	start_dirs = get_dir(end[0], end[1])
	dir_row = start_dirs[0]
	dir_col = start_dirs[1]
	
	width = util.abs(start[0] - end[0]) + 1
	height = util.abs(start[1] - end[1]) + 1
	
	for r in range(height):
		item = items[r%len(items)]
		plant_row(item, width, dir_row)
		
		dir_row = util.flip_dir(dir_row)
		move(dir_col)
		

def plant_blueprint(blueprint):
	
	for i in range(len(blueprint)):
		plan = blueprint[i]
		
		entity = plan[0]
		start = plan[1]
		end = plan[2]
		plant_area([entity], start, end)
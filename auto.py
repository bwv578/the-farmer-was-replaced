import util
import advanced
import movement


def plant_row(item, len, dir) : 	
	for i in range(len):
		advanced.a_harvest(item)
				
		if(not i==len-1):
			move(dir)

			
def plant_row_with_trees(item, len, dir) :
	for i in range(len):
		if(util.is_pos_odd()):
			advanced.a_harvest(Entities.Tree)
		else:
			advanced.a_harvest(item)
				
		if(not i==len-1):
			move(dir)


def plant_area(items, start, end) :
	movement.go_point(start[0], start[1])
	
	start_dirs = movement.get_dir(end[0], end[1])
	dir_row = start_dirs[0]
	dir_col = start_dirs[1]
	
	width = util.abs(start[0] - end[0]) + 1
	height = util.abs(start[1] - end[1]) + 1
	
	for r in range(height):
		item = items[r%len(items)]
		plant_row(item, width, dir_row)
		
		dir_row = util.flip_dir(dir_row)
		if(not r==height-1):
			move(dir_col)
		

def plant_blueprint(blueprint):
	
	for i in range(len(blueprint)):
		plan = blueprint[i]	
		entity = plan[0]
		start = plan[1]
		end = plan[2]
		plant_area([entity], start, end)
		

def plant_trees(entity):
	for col in range(get_world_size()):
		plant_row_with_trees(entity, get_world_size(), East)
		move(North)
			 
		
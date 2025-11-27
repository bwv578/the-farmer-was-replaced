import util
import advanced
import movement


def harvest_all():
	ws = get_world_size()
	for row in range(ws):
		for col in range(ws):
			harvest()
			move(East)
		move(North)


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


def plant_area(item, start, end) :
	pos_x = get_pos_x()
	pos_y = get_pos_y()
	
	routes_start = [
		movement.get_route(East, start[0]-pos_x),
		movement.get_route(North, start[1]-pos_y)
	]
	routes_end = [
		movement.get_route(East, end[0]-pos_x),
		movement.get_route(North, end[1]-pos_y)
	]
	
	manhattan_start = routes_start[0][1] + routes_start[1][1]
	manhattan_end = routes_end[0][1] + routes_end[1][1]
	
	if(manhattan_start > manhattan_end):
		routes_start, routes_end = routes_end, routes_start
		start, end = end, start
	
	movement.go_routes(routes_start)
	
	dirs = movement.get_dir(end[0], end[1])
	width = util.abs(start[0] - end[0]) + 1
	height = util.abs(start[1] - end[1]) + 1
	
	for r in range(height):
		plant_row(item, width, dirs[0])
		
		dirs[0] = util.flip[dirs[0]]
		if(not r==height-1):
			move(dirs[1])
		

def plant_blueprint(blueprint):	
	for i in range(len(blueprint)):
		plan = blueprint[i]	
		plant_area(plan['entity'], plan['start'], plan['end'])


def plant_trees(entity):
	for col in range(get_world_size()):
		plant_row_with_trees(entity, get_world_size(), East)
		move(North)
			 
		
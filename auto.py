import util
import advanced
import movement


def pray():
	while not can_harvest():
		entity = get_entity_type()
		if(entity==None or entity==Entities.Dead_Pumpkin):
			plant(Entities.Grass)
			print('빨리좀 자라라')


def harvest_all():
	ws = get_world_size()
	for row in range(ws):
		for col in range(ws):
			harvest()
			move(East)
		move(North)


def plant_row(item, len, dir) :  	
	for i in range(len-1):
		advanced.a_harvest(item)
		move(dir)
	advanced.a_harvest(item)

			
def plant_row_trees(len, dir) :
	for i in range(len-1):
		if(util.is_pos_odd()):
			advanced.a_harvest(Entities.Tree)
		else:
			advanced.a_harvest(Entities.Bush)
		move(dir)
	if(util.is_pos_odd()):
		advanced.a_harvest(Entities.Tree)
	else:
		advanced.a_harvest(Entities.Bush)


def plant_area(item, start, end) :
	pos_x = get_pos_x()
	pos_y = get_pos_y()
	
	start_op = [start[0], end[1]]
	end_op = [end[0], start[1]]
	
	routes_start = [
		movement.get_route(East, start[0]-pos_x),
		movement.get_route(North, start[1]-pos_y)
	]
	routes_end = [
		movement.get_route(East, end[0]-pos_x),
		movement.get_route(North, end[1]-pos_y)
	]
	routes_start_op = [
		movement.get_route(East, start[0]-pos_x),
		movement.get_route(North, end[1]-pos_y)
	]
	routes_end_op = [
		movement.get_route(East, end[0]-pos_x),
		movement.get_route(North, start[1]-pos_y)
	]
	
	corner_points = [start, start_op, end_op, end]
	corner_routes = [routes_start, routes_start_op, routes_end_op, routes_end] 
	
	shortest_dist = routes_start[0][1] + routes_start[1][1]
	shortest_idx = 0
	
	for i in range(3):
		route = corner_routes[i+1]
		dist = route[0][1]+route[1][1]
		if(dist < shortest_dist):
			shortest_dist = dist
			shortest_idx = i+1
	
	routes_start = corner_routes[shortest_idx]
	start = corner_points[shortest_idx]
	end = corner_points[3-shortest_idx]
	
	movement.go_routes(routes_start)
	
	dirs = movement.get_dir(end[0], end[1])
	width = util.abs(start[0] - end[0]) + 1
	height = util.abs(start[1] - end[1]) + 1
	
	for r in range(height-1):
		if(item==Entities.Tree):
			plant_row_trees(width, dirs[0])
		else:
			plant_row(item, width, dirs[0])
		dirs[0] = util.flip[dirs[0]]
		move(dirs[1])
	if(item==Entities.Tree):
		plant_row_trees(width, dirs[0])
	else:
		plant_row(item, width, dirs[0])	
	dirs[0] = util.flip[dirs[0]]
		

def plant_blueprint(blueprint):	
	for i in range(len(blueprint)):
		plan = blueprint[i]	
		plant_area(plan['entity'], plan['start'], plan['end'])
import util
	

def get_dir(x, y):
	directions = []
	
	if(get_pos_x() < x):
		directions.append(East)
	else:
		directions.append(West)
	
	if(get_pos_y() < y):
		directions.append(North)
	else:
		directions.append(South)
	
	return directions	

	
def get_route(forward_dir, diff):
	dist = util.abs(diff)
	reverse = util.is_negative(diff)
	has_short_cut = dist > get_world_size()/2
	
	if(has_short_cut):
		reverse = not reverse
		dist = get_world_size() - dist		
	
	if(reverse):
		return [util.flip[forward_dir], dist]
	else:
		return [forward_dir, dist]


def go_routes(routes):
	for i in range(len(routes)):
		route = routes[i]
		for j in range(route[1]):
			move(route[0])
	
def go_x(x):
	route = get_route(East, x-get_pos_x())
	for i in range(route[1]):
		move(route[0])	


def go_y(y):
	route = get_route(North, y-get_pos_y())
	for i in range(route[1]):
		move(route[0])
		

def go_point(x, y):
	go_x(x)
	go_y(y)
	
	
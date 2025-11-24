import util
	
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
	
def go_x(x):
	diff = x-get_pos_x()
	reverse = util.is_negative(diff)
	
	if(reverse):
		for d in range(diff * -1):
			move(West)
	else:
		for d in range(diff):
			move(East)

def go_y(y):
	diff = y - get_pos_y()
	reverse = util.is_negative(diff)
	
	if(reverse):
		for d in range(diff*-1):
			move(South)
	else:
		for d in range(diff):
			move(North)	
		
def go_point(x, y):
	go_x(x)
	go_y(y)
	
	
	
	
def is_odd(number):
	if(number%2 == 1):
		return True
	return False
	
def is_even(number):
	return not is_odd(number)
	
def get_pos_sum():
	return get_pos_x() + get_pos_y()
	
def is_pos_odd():
	return is_odd(get_pos_sum())	
	
def is_pos_even():
	return is_even(get_pos_sum())

def is_negative(number):
	if(number<0):
		return True
	return False

def abs(number):
	if(number < 0):
		return number * -1
	else:
		return number
		
def flip_dir(dir):
	if(dir == East):
		return West
	elif(dir == West):
		return East
	elif(dir == North):
		return South
	else:
		return North
	
def needs_till(item) :
	if(item==Entities.Carrot or item==Entities.Pumpkin):
		if(not get_ground_type()==Grounds.Soil):
			return True
	return False

	
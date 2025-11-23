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
	
def needs_till(item) :
	if(item==Entities.Carrot or item==Entities.Pumpkin):
		if(not get_ground_type()==Grounds.Soil):
			return True
	return False
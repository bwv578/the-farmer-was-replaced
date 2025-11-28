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

flip = {
	East:West,
	West:East, 
	North:South, 
	South:North
}


turn = {
	'cw': {
		East: South,
		South: West,
		West: North,
		North: East
	},
	'ccw': {
		East: North,
		North: West,
		West: South,
		South: East
	}
}


needs_till = {
	Entities.Carrot: Grounds.Grassland,
	Entities.Pumpkin: Grounds.Grassland,
	Entities.Grass: Grounds.Soil,
	Entities.Bush: None,
	Entities.Dead_Pumpkin: None,
	Entities.Cactus: Grounds.Grassland,
	Entities.Tree: None,
	Entities.Sunflower: Grounds.Grassland
}

	
	
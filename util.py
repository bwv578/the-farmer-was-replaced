def isOdd(number):
	if(number%2 == 1):
		return True
	return False
	
def isEven(number):
	return not isOdd(number)
	
def getPosSum():
	return get_pos_x() + get_pos_y()
	
def isPosOdd():
	return isOdd(getPosSum())	
	
def isPosEven():
	return isEven(getPosSum())
	
def needTill(item) :
	if(item==Entities.Carrot or item==Entities.Pumpkin):
		groundType = get_ground_type()
		if(not groundType==Grounds.Soil):
			return True
	return False
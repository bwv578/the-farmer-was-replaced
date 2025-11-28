import util

def a_plant(item):
	if(util.needs_till[item]==get_ground_type()):
		till()
	plant(item)
	use_item(Items.Fertilizer)


def a_harvest(item):
	if(can_harvest()):
		harvest()
		a_plant(item)
	
	elif(get_entity_type()==None 
			or get_entity_type()==Entities.Dead_Pumpkin):
		a_plant(item)
		
	elif(get_entity_type()==Entities.Grass):
		if(not item==Entities.Grass):
			a_plant(item)
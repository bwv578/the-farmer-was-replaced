import util

def a_plant(item):
	if(util.needs_till(item)):
		till()		
	plant(item)
	

# @return job_done(boolean) 
def a_harvest(item):
	if(can_harvest()):
		harvest()
		a_plant(item)
		return True
		
	elif(get_entity_type()==Entities.Dead_Pumpkin):
		a_plant(item)
		return True
	
	return False

				
		
		
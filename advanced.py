import util

def aPlant(item):
	if(util.needTill(item)):
		till()		
	plant(item)
	
	
def aHarvest(item):
	if(can_harvest()):
		harvest()
		aPlant(item)

	elif(get_entity_type()==Entities.Dead_Pumpkin):
		aPlant(item)
		

				
		
		
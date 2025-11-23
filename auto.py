import util
import advanced

def plantRow(item) : 
	for i in range(get_world_size()):
		advanced.aHarvest(item)
		move(North)


def plantRowWithTrees(item) :
	for i in range(get_world_size()):
		target = item		
		
		if(util.isPosOdd()):
			target = Entities.Tree
					
		advanced.aHarvest(target)
		move(North)
		
		
def plantArea(items, withTrees=False) :
	worldSize = get_world_size()
	rows = range(worldSize)
	
	for r in rows:
		if(withTrees):
			plantRowWithTrees(items[r%len(items)])
		else:
			plantRow(items[r%len(items)])
		
		move(East)
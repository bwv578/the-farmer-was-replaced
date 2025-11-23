import util
import advanced

def plant_row(item) : 
	for i in range(get_world_size()):
		advanced.a_harvest(item)
		move(North)


def plant_row_with_trees(item) :
	for i in range(get_world_size()):
		target = item		
		
		if(util.is_pos_odd()):
			target = Entities.Tree
					
		advanced.a_harvest(target)
		move(North)
		
		
def plant_area(items, mix_trees=False) :
	world_size = get_world_size()
	rows = range(world_size)
	
	for r in rows:
		if(mix_trees):
			plant_row_with_trees(items[r%len(items)])
		else:
			plant_row(items[r%len(items)])
		
		move(East)
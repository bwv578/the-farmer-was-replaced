import advanced
import movement
import util


def open():
	advanced.a_harvest(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

	
def is_pos_treasure():
	if((get_pos_x(), get_pos_y()) == measure()):
		return True
	return False
	

def is_wall_left(forward):
	return not can_move(util.turn['ccw'][forward])

	
def solve():
	forward = North
	
	while not is_wall_left(forward):
		move(util.turn['ccw'][forward])
		
	while not is_pos_treasure():
		if(not is_wall_left(forward)):
			forward = util.turn['ccw'][forward]
		elif(not can_move(forward)):
			forward = util.turn['cw'][forward]
		move(forward)
	harvest()

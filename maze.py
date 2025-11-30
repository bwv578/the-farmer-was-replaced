import util
import advanced
import glob


def open():
	advanced.a_harvest(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 3)
	use_item(Items.Weird_Substance, substance)

	
def is_pos_treasure():
	if((get_pos_x(), get_pos_y()) == measure()):
		return True
	return False
	

def is_wall_beside(forward, hand):
	return not can_move(util.turn[hand][forward])

	
def solve(hand):
	forward = North
	
	while not is_wall_beside(forward, hand):
		move(util.turn[hand][forward])
		
	while not is_pos_treasure():
		if(not is_wall_beside(forward, hand)):
			forward = util.turn[hand][forward]
		elif(not can_move(forward)):
			forward = util.turn[util.flip[hand]][forward]
		move(forward)
	harvest()
	
	
def scan(forward=None):
	ways = []
	for dir in [East, West, South, North]:
		if(can_move(dir) and dir!=util.flip[forward]):
			ways.append(dir)
	return ways

	
def is_node():
	if(len(scan()) > 2):
		return True
	return False


def set_root():
	forward = North
	while not is_wall_beside(forward, 'left'):
		move(West)
	while not is_node():
		if(not is_wall_beside(forward, 'left')):
			forward = util.turn['left'][forward]
		elif(not can_move(forward)):
			forward = util.turn[util.flip['left']][forward]
		move(forward)

	return {'pos':(get_pos_x(), get_pos_y()), 'fwd':forward}
	

def back_to_parent(forward):
	back_fwd = util.flip[forward]
	while not is_node():
		back_fwd = scan(back_fwd)[0]
		move(back_fwd)
			


def explore(parent=None, forward=None, node_table=None):
	
	subtask_addr = (get_pos_x(), get_pos_y())
	is_subtask = subtask_addr in glob.tasks
	if(is_subtask):
		task = glob.tasks[subtask_addr]
		parent = task['parent']
		forward = task['fwd']
	
	is_root = parent==None
	if(is_root):
		set_root()
		
	cur_fwd = forward
	child_drones = []
	if(node_table==None):
		node_table = {}
		
	while True:
		dirs = scan(cur_fwd)
		
		if(len(dirs) > 2 or (len(dirs)==2 and not is_root)):
			cur_pos = (get_pos_x(), get_pos_y())
			node_table[cur_pos] = parent
			
			for dir in dirs:
				move(dir)
				if(num_drones() < max_drones()):
					new_task_addr = (get_pos_x(), get_pos_y())
					glob.tasks[new_task_addr] = {'parent': cur_pos, 'fwd': dir}
					child_drones.append(spawn_drone(explore))
					move(util.flip[dir])
				else:
					explore(cur_pos, dir, node_table)
				
			if(not is_root):
				move(util.flip[cur_fwd])
				back_to_parent(cur_fwd)
				
			break
				
		elif(len(dirs) == 0):
			end_node = (get_pos_x(), get_pos_y())
			back_to_parent(cur_fwd)
			node_table[end_node] = parent
			
			break
			
		else:
			cur_fwd = dirs[0]
			move(cur_fwd)
	
	for drone in child_drones:
		sub_nodes = wait_for(drone)
		for c in sub_nodes:
			node_table[c] = sub_nodes[c]
	
	if(is_subtask):
		glob.tasks.pop(subtask_addr)
	
	return node_table
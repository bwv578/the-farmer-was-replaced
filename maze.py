import util
import advanced
import glob


def open():
	advanced.a_harvest(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 2)
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


def back_to_parent(forward):
	back_fwd = util.flip[forward]
	while not is_node():
		back_fwd = scan(back_fwd)[0]
		move(back_fwd)
			

def explore(parent=None, forward=None, node_table={}):
	
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
		
	while True:
		dirs = scan(cur_fwd)
		
		if(len(dirs) > 2 or (len(dirs)==2 and not is_root)):
			cur_pos = (get_pos_x(), get_pos_y())
			node_table[cur_pos] = (parent, forward, util.flip[cur_fwd])
			
			for dir in dirs:
				move(dir)
				new_task_addr = (get_pos_x(), get_pos_y())
				glob.tasks[new_task_addr] = {'parent': cur_pos, 'fwd': dir}
				spawn_attempt = spawn_drone(explore)
				
				if(spawn_attempt==None):
					glob.tasks.pop(new_task_addr)
					explore(cur_pos, dir, node_table)
				else:
					child_drones.append(spawn_attempt)
					move(util.flip[dir])
				
			if(not is_root):
				move(util.flip[cur_fwd])
				if not is_subtask:
					back_to_parent(cur_fwd)
			
			for drone in child_drones:
				sub_nodes = wait_for(drone)
				for node in sub_nodes:
					node_table[node] = sub_nodes[node]
			break
				
		elif(len(dirs) == 0):
			end_node = (get_pos_x(), get_pos_y())
			if not is_subtask:
				back_to_parent(cur_fwd)
			node_table[end_node] = (parent, forward, util.flip[cur_fwd])
			break
			
		else:
			cur_fwd = dirs[0]
			move(cur_fwd)
	
	if(is_root):
		glob.tasks = {}
	
	return node_table
	
	
def run_paths(paths, target):
	cur_pos = (get_pos_x(), get_pos_y())
	while cur_pos != target:
		dir = paths[cur_pos]
		if(dir==None):
			break		
		move(dir)
		while not is_node():
			scans = scan(dir)
			if(len(scans)==0):
				break
			dir = scans[0]
			move(dir)
		cur_pos = (get_pos_x(), get_pos_y())
		
	
def solve_node(node_table):
	set_root()

	cur_super = [(get_pos_x(), get_pos_y())]
	trs_super = [measure()]

	cur_to_fork = {}
	fork_to_trs = {}
	fork = None
	
	while True :
		if cur_super[0] in fork_to_trs:
			fork = cur_super[0]
			addr = cur_super[0]
			cur_super = node_table[cur_super[0]]
			cur_to_fork[addr] = cur_super[2]
			break
		if trs_super[0] in cur_to_fork:
			fork = trs_super[0]
			trs_super = node_table[trs_super[0]]
			fork_to_trs[trs_super[0]] = trs_super[1]
			break
			
		if cur_super[0] != None:
			addr = cur_super[0]
			cur_super = node_table[cur_super[0]]
			cur_to_fork[addr] = cur_super[2]
		if trs_super[0] != None:
			trs_super = node_table[trs_super[0]]
			fork_to_trs[trs_super[0]] = trs_super[1]
			
	run_paths(cur_to_fork, fork)
	run_paths(fork_to_trs, measure())
	print('보물 여깄다')
	

def go_random_loc():
	hand = 'left'
	forward = North
	
	while not is_wall_beside(forward, hand):
		move(util.turn[hand][forward])
		
	for i in range(50):
		if(not is_wall_beside(forward, hand)):
			forward = util.turn[hand][forward]
		elif(not can_move(forward)):
			forward = util.turn[util.flip[hand]][forward]
		move(forward)

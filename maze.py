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
			node_table[cur_pos] = (parent, forward)
			
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
			back_to_parent(cur_fwd)
			node_table[end_node] = (parent, forward)
			break
			
		else:
			cur_fwd = dirs[0]
			move(cur_fwd)
	
	if(is_root):
		glob.tasks = {}
	
	return node_table
	
	
def run_paths(paths):
	for path in paths:
		if(path == None):
			break
		move(path)
		while not is_node():
			scans = scan(path)
			if(len(scans)==0):
				break
			path = scans[0]
			move(path)
	
	
def solve_node(node_table):
	test()
	set_root()

	cur_super = [(get_pos_x(), get_pos_y())]
	trs_super = [measure()]
	quick_print('solve start..  cur_pos:', cur_super[0], '  isNodeHead?:',node_table[cur_super[0]]==(None,None))
	
	cur_to_fork = []
	trs_to_fork = []
	
	# 여태 그냥 루트에서 시작해서 오류 안난듯	다른위치면 포크 잘못잡아서 오류날거임
	while cur_super != trs_super:
		if(cur_super[0] != None):
			cur_super = node_table[cur_super[0]]
			cur_to_fork.append(util.flip[cur_super[1]])
		if(trs_super[0] != None):
			trs_super = node_table[trs_super[0]]
			trs_to_fork.append(trs_super[1])
	
	fork_to_trs = util.mirror(trs_to_fork)
	fork_to_trs.remove(fork_to_trs[0])
	
	run_paths(cur_to_fork)
	run_paths(fork_to_trs)
	quick_print('cur_to_fork:', cur_to_fork)
	quick_print('fork_to_trs:', fork_to_trs)
	
	#print('보물 여깄다')
	#do_a_flip()	

	
	
def test(hand='left'):
	forward = North
	
	while not is_wall_beside(forward, hand):
		move(util.turn[hand][forward])
		
	for i in range(50):
		if(not is_wall_beside(forward, hand)):
			forward = util.turn[hand][forward]
		elif(not can_move(forward)):
			forward = util.turn[util.flip[hand]][forward]
		move(forward)

from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

trav_graph = {}
# print(world.rooms[0].e_to)
for room in world.rooms:
	trav_graph[room] = {
		'n': world.rooms[room].n_to.id if world.rooms[room].n_to else None,
		's': world.rooms[room].s_to.id if world.rooms[room].s_to else None,
		'w': world.rooms[room].w_to.id if world.rooms[room].w_to else None,
		'e': world.rooms[room].e_to.id if world.rooms[room].e_to else None
	}
print(trav_graph)
# ---
q = []
# q.append([world.starting_room])
q.append([(world.starting_room.id, 'start')])
shortest_paths = {}
while len(q) > 0:
	p = q.pop(0)
	room = p[-1][0]
	if (room == None):
		continue
	if room not in shortest_paths:
		shortest_paths[room] = p
		for next_room in trav_graph[room]:
			if next_room not in shortest_paths:
				copy = p[:]
				copy.append((trav_graph[room][next_room], next_room))
				q.append(copy)
print(shortest_paths)

# x = [{1: 't'}, {2: 'bingus'}, {}]
# print(x[-1].items())

# visited = {}
# q = Queue()
# q.enqueue([user_id])
# while q.size() > 0:
# 	path = q.dequeue()
# 	newuser_id = path[-1]
# 	if newuser_id not in visited:
# 		visited[newuser_id] = path
# 		for friend_id in self.friendships[newuser_id]:
# 			if friend_id not in visited:
# 				new_path = list(path)
# 				new_path.append(friend_id)
# 				q.enqueue(new_path)
# ---
opp = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
direction_paths = {}
for key in shortest_paths:
	direction_paths[key] = [x[1] for x in shortest_paths[key]]
print(direction_paths)

for value in direction_paths.values():
	path_back = []
	for direction in value:
		if direction != 'start':
			traversal_path.append(direction)
			path_back.insert(0, opp[direction])
	traversal_path.extend(path_back)

s = []
s.append([0])
dfs_paths = {}
while len(s) > 0:
	path = s.pop()
	room_num = path[-1]
	if room_num not in dfs_paths:
		if (room_num == None):
			continue
		dfs_paths[room_num] = path
		# print(room_num)
		for next_room in trav_graph[room_num]:
			copy = path[:]
			copy.append(trav_graph[room_num][next_room])
			s.append(copy)
print(dfs_paths)

# s = [n for n in shortest_paths[0]]
# # s.append(shortest_paths[0])
# # directions = ['n', 's', 'w', 'e']
# current_room = player.current_room
# direction_paths = {}
# while len(s) > 0:
# 	room_num = s.pop()
# 	direction_path = []
# 	# room_num = path[-1]
# 	# if room_num == 0:
# 		# s.append(shortest_paths[room_num + 1])
# 		# s = [n for n in shortest_paths]
# 		# continue
# 	if room_num not in direction_paths:
# 		for x in current_room.get_exits():
# 			if x == 'n':
# 				if room.n_to.id == room_num:
# 					current_room = current_room.n_to
# 					# s.append(room.n_to)
# 					# x.append(next_room)
# 			elif x == 's':
# 				if room.s_to.id == room_num:
# 					current_room = current_room.s_to
# 					# s.append(room.s_to)
# 					# x.append(next_room)
# 			elif x == 'w':
# 				if room.w_to.id == room_num:
# 					current_room = current_room.w_to
# 					# s.append(room.w_to)
# 					# x.append(next_room)
# 			elif x == 'e':
# 				if room.e_to.id == room_num:
# 					current_room = current_room.e_to
					# s.append(room.e_to)
					# x.append(next_room)
		# direction_paths[room_num] = path

#
# x = []
# s = []
# # directions = []
# # last_direction = ''
# # current_room = player.current_room
# s.append(shortest_paths[0])
# # x.append('n')
# visited = set()
# while len(s) > 0:
# 	room_path = s.pop()
# 	# print(room)
# 	# direction = x.pop()
# 	# if (room == None):
# 	# 	continue
# 	if room_path not in visited:
# 		print(room.id)
# 		current_room = room
# 		# if x:
# 		# 	direction = x.pop()
# 		visited.add(room)
# 		# x.append()
# 		for next_room in trav_graph[room.id]:
# 			# print(room)
# 			# print(next_room)
# 			# if trav_graph[room][next_room]:
# 			# 	x.append(next_room)
#
# 			if next_room == 'n':
# 				if room.n_to:
# 					s.append(room.n_to)
# 					x.append(next_room)
# 			elif next_room == 's':
# 				if room.s_to:
# 					s.append(room.s_to)
# 					x.append(next_room)
# 			elif next_room == 'w':
# 				if room.w_to:
# 					s.append(room.w_to)
# 					x.append(next_room)
# 			elif next_room == 'e':
# 				if room.e_to:
# 					s.append(room.e_to)
# 					x.append(next_room)
# #
# 			# if next_room == 'n':
# 			# 	s.append(room.n_to)
# 			# elif next_room == 's':
# 			# 	s.append(room.s_to)
# 			# elif next_room == 'w':
# 			# 	s.append(room.w_to)
# 			# elif next_room == 'e':
# 			# 	s.append(room.e_to)
#
# 			# print(room.next_room_attr)
# 			# s.append(trav_graph[room.id][next_room])
# print(x)

# if next_room == 'n':
# 	if room.n_to:
# 		s.append(room.n_to)
# 		x.append(next_room)
# elif next_room == 's':
# 	if room.s_to:
# 		s.append(room.s_to)
# 		x.append(next_room)
# elif next_room == 'w':
# 	if room.w_to:
# 		s.append(room.w_to)
# 		x.append(next_room)
# elif next_room == 'e':
# 	if room.e_to:
# 		s.append(room.e_to)
# 		x.append(next_room)

# ---

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
	player.travel(move)
	visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
	print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
	print("TESTS FAILED: INCOMPLETE TRAVERSAL")
	print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
# 	cmds = input("-> ").lower().split(" ")
# 	if cmds[0] in ["n", "s", "e", "w"]:
# 		player.travel(cmds[0], True)
# 	elif cmds[0] == "q":
# 		break
# 	else:
# 		print("I did not understand that command.")

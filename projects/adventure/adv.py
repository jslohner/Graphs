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
opp = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
# print(trav_graph)
# ---
v = {room:False for room in world.rooms}
def dfs(room_id):
	v[room_id] = True
	for direction in 'nswe':
		if trav_graph[room_id][direction] and not v[trav_graph[room_id][direction]]:
			traversal_path.append(direction)
			dfs(trav_graph[room_id][direction])
			traversal_path.append(opp[direction])
dfs(0)
# ---
# q = []
# # q.append([world.starting_room])
# q.append([(world.starting_room.id, 'start')])
# shortest_paths = {}
# while len(q) > 0:
# 	p = q.pop(0)
# 	room = p[-1][0]
# 	if (room == None):
# 		continue
# 	if room not in shortest_paths:
# 		shortest_paths[room] = p
# 		for next_room in trav_graph[room]:
# 			if next_room not in shortest_paths:
# 				copy = p[:]
# 				copy.append((trav_graph[room][next_room], next_room))
# 				q.append(copy)
# # ---
# direction_paths = {}
# num_paths = {}
# for key in shortest_paths:
# 	direction_paths[key] = [x[1] for x in shortest_paths[key]]
# 	num_paths[key] = [x[0] for x in shortest_paths[key]]
#
# bfs_paths = {}
# for key in shortest_paths:
# 	path = [t[0] for t in shortest_paths[key]]
# 	bfs_paths[key] = path
#
# for key in bfs_paths:
# 	for room_num in bfs_paths[key]:
# 		if room_num != key:
# 			if room_num in direction_paths:
# 				del direction_paths[room_num]
#
# possible_connections = {}
# connections = {}
# for key in direction_paths:
# 	if len(world.rooms[key].get_exits()) > 1:
# 		possible_connections[key] = [x for x in trav_graph[key].values()]
#
# for key in possible_connections:
# 	for room in possible_connections[key]:
# 		if room in possible_connections:
# 			if (key not in connections) and (room not in connections):
# 				connections[key] = room
#
# for key in connections:
# 	new_path = []
# 	for d in direction_paths[connections[key]]:
# 		if d != 'start':
# 			new_path.insert(0, opp[d])
#
# 	room = world.rooms[key]
# 	for exit in room.get_exits():
# 		if exit == 'n':
# 			if room.n_to.id == connections[key]:
# 				new_path.insert(0, 'n')
# 		elif exit == 's':
# 			if room.s_to.id == connections[key]:
# 				new_path.insert(0, 's')
# 		elif exit == 'w':
# 			if room.w_to.id == connections[key]:
# 				new_path.insert(0, 'w')
# 		elif exit == 'e':
# 			if room.e_to.id == connections[key]:
# 				new_path.insert(0, 'e')
#
# 	direction_paths[key].extend(new_path)
# 	del direction_paths[connections[key]]
#
# # explored = {i:False for i in range(0, len(world.rooms))}
# # for key in direction_paths:
# # 	for direction in direction_paths[key]:
# # 		if direction != 'start':
# # 			player.travel(direction)
# # 			print(player.current_room.id)
# # 	for direction in reversed(direction_paths[key]):
# # 		if direction != 'start':
# # 			player.travel(opp[direction])
# # 			print(player.current_room.id)
#
# for key in direction_paths:
# 	path_back = []
# 	for direction in direction_paths[key]:
# 		if direction != 'start':
# 			traversal_path.append(direction)
# 			path_back.insert(0, opp[direction])
# 	if key not in connections:
# 		traversal_path.extend(path_back)
# # ---

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
	# print(player.current_room.id)
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

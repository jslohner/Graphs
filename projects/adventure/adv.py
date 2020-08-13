from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

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
# print(trav_graph)
# ---
q = []
# q.append([world.starting_room])
q.append([world.starting_room.id])
shortest_paths = {}
while len(q) > 0:
	p = q.pop(0)
	room = p[-1]
	if room not in shortest_paths:
		if (room == None):
			continue
		shortest_paths[room] = p
		for next_room in trav_graph[room]:
			if next_room not in shortest_paths:
				copy = p[:]
				copy.append(trav_graph[room][next_room])
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

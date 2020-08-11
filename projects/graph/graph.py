"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

	"""Represent a graph as a dictionary of vertices mapping labels to edges."""
	def __init__(self):
		self.vertices = {}
		# self.dft_checked = set()
		# self.dfs_checked = set()
		# self.dfs_paths = {}

	def add_vertex(self, vertex_id):
		"""
		Add a vertex to the graph.
		"""
		self.vertices[vertex_id] = set()

	def add_edge(self, v1, v2):
		"""
		Add a directed edge to the graph.
		"""
		if (v1 in self.vertices) and (v2 in self.vertices):
			self.vertices[v1].add(v2)
		else:
			raise IndexError('nonexistent vertex')

	def get_neighbors(self, vertex_id):
		"""
		Get all neighbors (edges) of a vertex.
		"""
		return self.vertices[vertex_id]

	def bft(self, starting_vertex):
		"""
		Print each vertex in breadth-first order
		beginning from starting_vertex.
		"""
		q = Queue()
		q.enqueue(starting_vertex)
		visited = set()
		while q.size() > 0:
			v = q.dequeue()
			if v not in visited:
				print(v)
				visited.add(v)
				for n in self.get_neighbors(v):
					q.enqueue(n)

	def dft(self, starting_vertex):
		"""
		Print each vertex in depth-first order
		beginning from starting_vertex.
		"""
		s = Stack()
		s.push(starting_vertex)
		visited = set()
		while s.size() > 0:
			v = s.pop()
			if v not in visited:
				print(v)
				visited.add(v)
				for n in self.get_neighbors(v):
					s.push(n)

	def dft_recursive(self, starting_vertex, checked=None):
		"""
		Print each vertex in depth-first order
		beginning from starting_vertex.

		This should be done using recursion.
		"""
		# lecture solution
		if checked is None:
			checked = set()
		checked.add(starting_vertex)
		print(starting_vertex)
		for n in self.vertices[starting_vertex]:
			if n not in checked:
				self.dft_recursive(n, checked)

		# original solution
		# if starting_vertex in self.dft_checked:
		# 	return
		# print(starting_vertex)
		# self.dft_checked.add(starting_vertex)
		# for n in self.get_neighbors(starting_vertex):
		# 	self.dft_recursive(n)

	def bfs(self, starting_vertex, destination_vertex):
		"""
		Return a list containing the shortest path from
		starting_vertex to destination_vertex in
		breath-first order.
		"""
		q = Queue()
		q.enqueue([starting_vertex])
		visited = set()
		while q.size() > 0:
			p = q.dequeue()
			v = p[-1]
			if v not in visited:
				if (v == destination_vertex):
					return p
				visited.add(v)
				for n in self.get_neighbors(v):
					copy = p[:]
					copy.append(n)
					q.enqueue(copy)

	def dfs(self, starting_vertex, destination_vertex):
		"""
		Return a list containing a path from
		starting_vertex to destination_vertex in
		depth-first order.
		"""
		s = Stack()
		s.push([starting_vertex])
		visited = set()
		while s.size() > 0:
			p = s.pop()
			v = p[-1]
			if v not in visited:
				if (v == destination_vertex):
					return p
				visited.add(v)
				for n in self.get_neighbors(v):
					copy = p[:]
					copy.append(n)
					s.push(copy)

	def dfs_recursive(self, starting_vertex, destination_vertex, checked=None, path=None):
		"""
		Return a list containing a path from
		starting_vertex to destination_vertex in
		depth-first order.

		This should be done using recursion.
		"""
		# lecture solution
		if checked is None:
			checked = set()
		if path is None:
			path = []
		checked.add(starting_vertex)
		path = path + [starting_vertex]
		if starting_vertex == destination_vertex:
			return path
		for n in self.get_neighbors(starting_vertex):
			if n not in checked:
				ans = self.dfs_recursive(n, destination_vertex, checked, path)
				if ans is not None:
					return ans
		return None

		# original solution
		# if destination_vertex in self.dfs_paths:
		# 	return self.dfs_paths[destination_vertex]
		# if len(self.dfs_paths) > 0:
		# 	p = self.dfs_paths[starting_vertex]
		# 	v = p[-1]
		# 	if v not in self.dfs_checked:
		# 		if (v == destination_vertex):
		# 			return p
		# 		self.dfs_checked.add(v)
		# 		for n in self.get_neighbors(v):
		# 			copy = p[:]
		# 			copy.append(n)
		# 			self.dfs_paths[n] = copy
		# 		return self.dfs_recursive(n, destination_vertex)
		# else:
		# 	self.dfs_paths[starting_vertex] = [starting_vertex]
		# 	return self.dfs_recursive(starting_vertex, destination_vertex)

if __name__ == '__main__':
	graph = Graph()  # Instantiate your graph
	# https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
	graph.add_vertex(1)
	graph.add_vertex(2)
	graph.add_vertex(3)
	graph.add_vertex(4)
	graph.add_vertex(5)
	graph.add_vertex(6)
	graph.add_vertex(7)
	graph.add_edge(5, 3)
	graph.add_edge(6, 3)
	graph.add_edge(7, 1)
	graph.add_edge(4, 7)
	graph.add_edge(1, 2)
	graph.add_edge(7, 6)
	graph.add_edge(2, 4)
	graph.add_edge(3, 5)
	graph.add_edge(2, 3)
	graph.add_edge(4, 6)

	'''
	Should print:
		{1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
	'''
	print(graph.vertices)

	'''
	Valid BFT paths:
		1, 2, 3, 4, 5, 6, 7
		1, 2, 3, 4, 5, 7, 6
		1, 2, 3, 4, 6, 7, 5
		1, 2, 3, 4, 6, 5, 7
		1, 2, 3, 4, 7, 6, 5
		1, 2, 3, 4, 7, 5, 6
		1, 2, 4, 3, 5, 6, 7
		1, 2, 4, 3, 5, 7, 6
		1, 2, 4, 3, 6, 7, 5
		1, 2, 4, 3, 6, 5, 7
		1, 2, 4, 3, 7, 6, 5
		1, 2, 4, 3, 7, 5, 6
	'''
	graph.bft(1)

	print('---------------')

	'''
	Valid DFT paths:
		1, 2, 3, 5, 4, 6, 7
		1, 2, 3, 5, 4, 7, 6
		1, 2, 4, 7, 6, 3, 5
		1, 2, 4, 6, 3, 5, 7
	'''
	graph.dft(1)

	print('---------------')

	graph.dft_recursive(1)

	print('---------------')

	'''
	Valid BFS path:
		[1, 2, 4, 6]
	'''
	print(graph.bfs(1, 6))

	'''
	Valid DFS paths:
		[1, 2, 4, 6]
		[1, 2, 4, 7, 6]
	'''
	print(graph.dfs(1, 6))
	print(graph.dfs_recursive(1, 6))

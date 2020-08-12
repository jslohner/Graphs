test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
	anc_mem = {}
	gen_mem = {}

	for t in ancestors:
		if t[1] not in anc_mem:
			anc_mem[t[1]] = set()
		anc_mem[t[1]].add(t[0])

	if starting_node not in anc_mem:
		return -1

	q = [starting_node]
	gen = 0
	gen_nums = []
	while len(q) > 0:
		gen += 1
		curr_node = q.pop(0)
		if curr_node in anc_mem:
			for n in anc_mem[curr_node]:
				q.append(n)
				gen_mem[n] = gen
				gen_nums.append(gen)

	max_gen = max(gen_nums)
	earliest_ancestors = []
	for key in gen_mem:
		if gen_mem[key] == max_gen:
			earliest_ancestors.append(key)
	return min(earliest_ancestors)

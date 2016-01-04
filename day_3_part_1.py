#day 3

lines = [line.rstrip('\n') for line in open('day_3.txt')]

grid = {'[0, 0]' : 1}
pos = [0,0]

#part-1
for line in lines :
	for o in line :
		if o == '>' :
			pos[0] += 1
		if o == '<' :
			pos[0] -= 1
		if o == '^' :
			pos[1] += 1
		if o == 'v' :
			pos[1] -= 1

		_pos = str(pos)

		if _pos in grid :
			grid[_pos] += 1
		else :
			grid[_pos] = 1

print "part-1 : " + str(len([p for p in grid if grid[p] >= 1]))
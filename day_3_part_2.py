#day 3

lines = [line.rstrip('\n') for line in open('day_3.txt')]

pos = [0,0]

#part-2
grid = {'[0, 0]' : 2}
pos_santa = [0,0]
pos_robo_santa = [0,0]

for line in lines :
	for o in line[0::2] :
		if o == '>' :
			pos_santa[0] += 1
		if o == '<' :
			pos_santa[0] -= 1
		if o == '^' :
			pos_santa[1] += 1
		if o == 'v' :
			pos_santa[1] -= 1

		_pos = str(pos_santa)

		if _pos in grid :
			grid[_pos] += 1
		else :
			grid[_pos] = 1

for line in lines :
	for o in line[1::2] :
		if o == '>' :
			pos_robo_santa[0] += 1
		if o == '<' :
			pos_robo_santa[0] -= 1
		if o == '^' :
			pos_robo_santa[1] += 1
		if o == 'v' :
			pos_robo_santa[1] -= 1

		_pos = str(pos_robo_santa)

		if _pos in grid :
			grid[_pos] += 1
		else :
			grid[_pos] = 1		

nb_house = len([p for p in grid if grid[p] >= 1])
print "part-2 : " + str(nb_house)
#day1

lines = [line.rstrip('\n') for line in open('day_1.txt')]

op = 0
floor = 0
for line in lines :
	for c in line :
		op += 1
		if c == '(' :
			floor += 1
		else :
			floor -= 1
		if floor == -1 :
			break

print op

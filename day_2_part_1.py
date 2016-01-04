#day 2

lines = [line.rstrip('\n') for line in open('day_2.txt')]


sum_paper = 0
l,w,h = 0,0,0


for line in lines :
	l,w,h = (int(x) for x in line.split('x'))
	sum_paper += 2*l*w + 2*w*h + 2*h*l
	sum_paper += min([(l*w),(w*h),(h*l)])

print sum_paper
#day 2

lines = [line.rstrip('\n') for line in open('day_2.txt')]


sum_paper = 0
l,w,h = 0,0,0

#part 2
rub = 0
for line in lines :
	l,w,h = (int(x) for x in line.split('x'))
	perimeters = [ 2*(l+h), 2*(l+w), 2*(w+h) ]
	surf = l*w*h
	rub += surf + min(perimeters)

print rub
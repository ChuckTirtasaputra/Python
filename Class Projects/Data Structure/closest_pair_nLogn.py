# Chuck Tirtasaputra
# closest points - n log n solution

# sample data (points and solution) 
# P = [(9,2),(2,7),(1,8),(4,3),(5,1),(7,4),(8,6),(3,5),(6,9)] 
# S = (((2, 7), (1, 8)), 1.4142135623730951)

from math import ceil, dist

P = [(9,2),(2,7),(1,8),(4,3),(5,1),(7,4),(8,6),(3,5),(6,9)]

def X(p):
	return p[0]

def Y(p):
	return p[1]

Px = sorted(P,key=X)
Py = sorted(P,key=Y)

# solution using Python Lists (inefficient)
def find_closest_pair(Px,Py):
	if len(Px) < 2: # list too short
		return ((None,None),float("inf"))
	elif len(Px) == 2: # only one pair
		return ((Px),dist(Px[0],Px[1]))
	elif len(Px) == 3: # best of three
		d1 = dist(Px[0],Px[1])
		d2 = dist(Px[0],Px[2])
		d3 = dist(Px[1],Px[2])
		if d1 <= d2 and d1 <= d3:
			return ((Px[0],Px[1]),d1)
		elif d2 <= d1 and d2 <= d3:
			return ((Px[0],Px[2]),d2)
		else:
			return ((Px[1],Px[2]),d3)
	else: # more than three, so solve recursively
		mid = ceil(len(Px)/2)
		Qx = Px[:mid]  # left side
		Rx = Px[mid:]  # right side
		Qy = Py[:mid]  # left side
		Ry = Py[mid:]  # right side
		Qpair = find_closest_pair(Qx,Qy)  # closest pair on left
		Rpair = find_closest_pair(Rx,Ry)  # closest pair on right
		delta = min(Qpair[1],Rpair[1])    # smallest distance of the two

		# find max x in Q (on left side)
		xmax = float("-inf")
		for i in Qx + Qy:
			if i[0] > xmax:
				xmax = i[0]

		# make list of points near (within delta) the max x vertical line
		S = []
		# TODO
		Lx = X(Qx[-1])
		for i in P:
			if abs(Lx - X(i)) < delta:
				S.append(i)
		Sy = sorted(S, key=Y)
		
		# find closest pair of points near the mid line
		Spair = ((None,None),float("inf"))
		# TODO
		for i in range(len(Sy)-1):
			for j in range(i+1, i+16):
				if dist(Sy[i%len(Sy)], Sy[j%len(Sy)]) < Spair[1] and dist(Sy[i%len(Sy)], Sy[j%len(Sy)]) != 0:
					Spair = ((Sy[i%len(Sy)], Sy[j%len(Sy)]), dist(Sy[i%len(Sy)], Sy[j%len(Sy)]))

		#returning the closest pair
		if Spair[1] < Qpair[1] and Spair[1] < Rpair[1]:
			return Spair
		elif Rpair[1] < Qpair[1] and Rpair < Spair[1]:
			return Rpair
		else:
			return Qpair
		#i%len(S)
		# choose best of Spair, Qpair, and Rpair

print(find_closest_pair(Px,Py))

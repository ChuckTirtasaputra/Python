# Closest Point O(n log n) 
import math

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def bruteForce(ax):
	mi = dist(ax[0], ax[1])
	p1 = ax[0]
	p2 = ax[1]
	ln_ax = len(ax)
	if ln_ax == 2:
		return p1, p2, mi
	for i in range(ln_ax-1):
		for j in range(i + 1, ln_ax):
			if i != 0 and j != 1:
				d = dist(ax[i], ax[j])
				if d < mi:  # Update min_dist and points
					mi = d
					p1, p2 = ax[i], ax[j]
	return p1, p2, mi
	
def closestPair(ax, ay):
	n = len(ax)
	print(ax)
	if n <= 3:
		bruteForce(ax)

	# split list in half
	mid = n // 2
	Lx = ax[:mid]
	Rx = ax[mid:]

	midpoint = ax[mid][0] 
	Ly = list()
	Ry = list()

	for x in ay:  # split ay into 2 arrays using midpoint
		if x[0] <= midpoint:
			Ly.append(x)
		else:
			Ry.append(x)
	
	# Call recursively both arrays after split
	(p1, q1, mi1) = closestPair(Lx, Ly)
	(p2, q2, mi2) = closestPair(Rx, Ry)

	# Determine smaller distance between points of 2 arrays
	if mi1 <= mi2:
		dis = mi1
		min = (p1, q1)
	else:
		dis = mi2
		min = (p2, q2)

	# Call function to account for points on the boundary

	(p3, q3, mi3) = closestSplitPair(ax, ay, dis, min)

	# Determine smallest distance for the array

	if dis <= mi3:
		return min[0], min[1], dis
	else:
		return p3, q3, mi3

def closestSplitPair(p_x, p_y, delta, best_pair):
    len_x = len(p_x)  # store length - quicker
    max_x = p_x[len_x // 2][0]  # select midpoint on x-sorted array
    # Create a subarray of points not further than delta from
    # midpoint on x-sorted array
    s_y = [x for x in p_y if max_x - delta <= x[0] <= max_x + delta]
    best = delta  # assign best value to delta
    len_y = len(s_y)  # store length of subarray for quickness
    for i in range(len_y - 1):
        for j in range(i+1, min(i + 7, len_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best

def solution(P):
    ax = sorted(P, key=lambda P: P[0])  # Presorting x
    ay = sorted(P, key=lambda P: P[1])  # Presorting y
    p1, p2, mi = closestPair(ax, ay)  # Recursive D&C function
    return p1,p2, mi

P = [(9,2),(2,7),(1,8),(4,3),(5,1),(7,4),(8,6),(3,5),(6,9)]

ax = sorted(P, key=lambda P: P[0])  # Presorting x
n = len(ax)
#print(ax[1])
solution(P)

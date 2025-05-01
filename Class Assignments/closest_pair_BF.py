# Brute Force Closest pair of points
import math

P = [(9,2),(2,7),(4,3),(1,8),(5,1),(7,4),(8,6),(3,5),(6,9)]

def bruteForce(P):
    dist = float("inf")
    n = len(P)

    # creates a list of x and y coords to be able to work with them better
    x = [lis[0] for lis in P]
    y = [lis[1] for lis in P]

    # basically loops through each pair 
    for point in P:
        for i in range(0, n-1):
            new = math.sqrt((point[0] - x[i])*(point[0] - x[i]) + (point[1] - y[i])*(point[1] - y[i]))
            if new != 0 and new < dist:
                dist = new
                p1 = point
                p2 = (x[i], y[i])

    return p1, p2, dist

(p1, p2, dist) = bruteForce(P)

print("Closests Pair of Points:", p1, p2, "\nDistance:", dist)

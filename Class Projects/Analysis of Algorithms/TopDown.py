# Chuck Tirtasaputra
'''
I think I got all of the 3 parts working. I ran into some trouble with my P function since I was trying to 
recreate the P function we made in class rather than the one from the book. 
'''

global intervals
global M

# 3a. top-down memoized recursive solution (p.256-257)
def p(i):
    if i == 0:
        return 0
    startTime = sorted[i-1][0]
    for j in range(i, 0, -1):
        if sorted[j-1][1] <= startTime:
            return j
    return 0

def M_Compute_Opt(j):
    if j == 0:
        return 0
    elif j in M:
        return M[j]
    else:
        M[j] = max(sorted[j-1][2] + M_Compute_Opt(p(j)), M_Compute_Opt(j-1))
        return M[j]

# 3b. solution code (p.258)
def FindSolution(j):
    if j == 0:
        return []
    elif (sorted[j-1][2] + M[p(j)]) >= M[j-1]:
        return [sorted[j-1]] + FindSolution(p(j))
    else:
        return FindSolution(j-1)

# 3c. bottom-up tabulation solution (p.259)
def Iterative_Compute_Opt(j):
    M[0] = 0
    for i in range(1, j+1):
        M[j] = max(sorted[i-1][2] + M[p(i)], M[i-1])
    return M[j]

# Testing and works with this particular test case
intervals = [[1, 4, 10], [2, 4, 11], [3, 5, 15], [5, 9, 2], [7, 10, 3]]
# sorted by the 2nd element of each lists
sorted = sorted(intervals, key = lambda x: int(x[1]))
M = {0: 0}
j = len(sorted)


print("List:", sorted)
print("Top-Down:", M_Compute_Opt(j)) # solution is 18
print("Bottom-Up:", Iterative_Compute_Opt(j))
print("Find Solution:", FindSolution(j))
#print("p(i)", p(j))


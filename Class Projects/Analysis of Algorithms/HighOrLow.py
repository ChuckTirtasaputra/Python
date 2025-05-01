# Chuck Tirtasaputra
'''
Exercise 2a. I think an instance this psuedocode wont work is:
n = 5
h = [1,5,50,200,25]
l = [1,5,20,1,20] 

Correct answer = 226
low stress week 1, low stress week 2, no job week 3, high stress job
week 4, low stres job week 5

Psuedocode answer = 76
low stress week 1, no job week 2, high stress week 3, no job week 4
high stress week 5

I got this code to work properly, but couldn't figure out how to do the 
FindSolution function so I just implemented a cache that would be a way to
show the path to the optimal solution instead. 
'''
from random import randint

global l
global h
# created a cache to see the path the code took to get to the maximum value
global cache 

cache = {0:0}
h = [2, 6, 9, 100, 20, 62, 3, 98, 67]
l = [17, 56, 32, 19, 55, 45, 45, 101, 3] 

# n = # of weeks (index of h/l)
leng = len(h)

def opt(n):
    # to stop code from breaking
    if len(h) != len(l):
        print("Lists given are not equal lengths")
        return 0
    # to stop code from breaking
    if n > len(h):
        print("'n' given is not within range")
        return 0
    # base case for opt(0)
    if n == 0:
        return 0
    # base case for opt(1)
    if n == 1:
        cache[n] = max(l[0], h[0])
        return cache[n]
    else:
        # golden line
        cache[n] = max((opt(n-1) + l[n-1]), (opt(n-2) + h[n-1]))
        return cache[n]

print("Hacker Problem")
print("Maximum Value:", opt(leng))
print("Pathway:", cache, "\n")

'''
Exercise 4a. I think an instance when the psuedocode does not give the 
right solution is when we give a scenario when the optimal minimum cost requires 
switching cities. The psuedocode does not take into account the moving cost.
So the example I give in the following (4b) would give make this code give
the wrong solution. The correct answer for the example I gave in 4b is 44.

Exercise 4b. An example of when the optimal plan has to move at least 3 times is:
n = 7
M = 5
N = [2, 20, 2, 20, 2, 20, 2]
S = [20, 2, 20, 2, 20, 2, 20]

The example above has this property because the moving cost does not 
cost more than the cost of just staying in a particular city. In the 
example above, the 5 (moving cost) + 2 (living cost at the other city)
will always be better than the 20 (living cost in the current city).

I got this code to work properly, but couldn't figure out how to do the 
FindSolution function so I just implemented a cache that would be a way to
show the path to the optimal solution instead. 
'''
global N
global S

cache = {0:0}

# n = # of months, M = moving cost
n = 10
M = 20 
N = [30, 35, 47, 59, 53, 21, 22, 25, 68, 44]
S = [71, 22, 99, 1, 3, 33, 62, 33, 51, 1]
# solution 296

'''
n = 25
M = 15   #Moving cost
N = []   #New York operating costs
S = []   #San Fran operating costs
cache = {0:0}

for i in range(n):
    N.append(randint(1,30))
    S.append(randint(1,30))
'''

def optN(n):
    # base case for opt(0)
    if n == 0:
        return 0
    # base case for opt(1)
    if n == 1:
        cache[n] = N[0]
        return cache[n]
    else:
        # golden line
        cache[n] = min((optN(n-1) + N[n-1]), (optS(n-1) + N[n-1]) + M)
        return cache[n]

def optS(n):
    # base case for opt(0)
    if n == 0:
        return 0
    # base case for opt(1)
    if n == 1:
        cache[n] = S[0]
        return cache[n]
    else:
        # golden line
        cache[n] = min((optS(n-1) + S[n-1]), (optN(n-1) + S[n-1]) + M)
        return cache[n]

solution = min(optN(n), optS(n))

print("Living Cost Problem")
print("Minimum Living Cost:", solution)
print("Pathway:", cache, "\n")
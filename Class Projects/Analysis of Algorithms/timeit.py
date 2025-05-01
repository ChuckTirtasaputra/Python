from timeit import timeit
from random import randint

def getData(n):
    n = n    #Number of months
    M = 15   #Moving cost
    N = []   #New York operating costs
    S = []   #San Fran operating costs
    cache = {0:0}

    for i in range(n):
        N.append(randint(1,50))
        S.append(randint(1,50))

    #Bottom up solution
    def NewSan(n, M, N, S):
        optN = [0 for i in range(n+1)]  #optN[i] is best total for first i months, ending in NY
        optS = [0 for i in range(n+1)]  #Same but for SF 

        for i in range(1,n+1):
            optN[i] = min(optN[i-1]+N[i-1], optS[i-1]+M+N[i-1]) 
            optS[i] = min(optS[i-1]+S[i-1], optN[i-1]+M+S[i-1])

        return min(optN[-1],optS[-1])
    
    #Brute Force solution
    def NewSanBF(n, M, N, S):
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

        return min(optN(n), optS(n))

    #Top-Down solution
    def NewSanTD(n, M, N, S):
        def optN(n):
            # base case for opt(0)
            if n == 0:
                return 0
            # base case for opt(1)
            if n == 1:
                cache[n] = N[0]
                return cache[n]
            if n in cache:
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
            if n in cache:
                return cache[n]
            else:
                # golden line
                cache[n] = min((optS(n-1) + S[n-1]), (optN(n-1) + S[n-1]) + M)
                return cache[n]

        return min(optN(n), optS(n))
        
    #Let's time it! Thanks to Brandon Chupp, who deciphered all this
    def wrapper(func, *args): #wraps a function to allow the timeit function to use it
        def wrapped():
            return func(*args)
        return wrapped

    #passes our NewSan function through the wrapper
    BU = wrapper(NewSan, n, M, N, S)
    TD = wrapper(NewSanTD, n, M, N, S)
    BF = wrapper(NewSanBF, n, M, N, S)

    #average runtime of 10,000 trials of size n
    #print(n,",", timeit(BU, number = 10000)/10000)
    print(timeit(TD, number = 10000)/10000)
    #print(timeit(BF, number = 10)/10)
    cache = {0:0}

for i in range(40,101):
    getData(i)
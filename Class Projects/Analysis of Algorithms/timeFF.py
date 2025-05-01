from timeit import timeit
from random import randint, sample
from DFS import * #depth first search file source: source: https://www.techiedelight.com/find-path-between-vertices-directed-graph/
from collections import deque
from copy import deepcopy

def getData(n):
    days = []
    roomie = {}

    # giving a number of days
    for i in range(1, n+1):
        days.append('d'+str(i))

    # setting the peoples to available days randomly
    for i in range(1, n+1):
        roomie['p'+str(i)] = sample(days, randint(0,n))

    # creating the graph
    def graph(roomie, days):
        cGraph = {} # the graph dictionary

        # creates dictionary for the people and their available days
        for i in roomie:
            cGraph[i] = []
        for people in roomie:
            for day in days:
                if day in roomie[people]:
                    cGraph[people].append(day)

        # connects the source to the people
        cGraph["src"] = []
        for i in roomie:
            cGraph["src"].append(i)

        # connects the days to the sink
        for i in days:
            cGraph[i] = ["sink"]
        cGraph['sink'] = []
        return cGraph

    # creating list of edges and their flow
    def edgelis(graph):
        edgeList = []
        flow = {}
        for i in graph:
            for j in graph[i]:
                edgeList.append((i, j))
        for i in edgeList:
            flow[i] = 0
        return edgeList, flow

    def augment(flow, pathEdges):
        for edge in pathEdges:
            if (edge[1], edge[0]) not in flow:
                flow[edge[1], edge[0]] = 0
            else:
                continue
        for edge in flow:
            if edge in pathEdges:
                flow[edge] = 1
            else:
                continue 
        return flow

    # ford fulkerson to see if its ergonomic and to find the pairings
    def fordFulkerson(roomie, days):
        path = deque()
        discovered = {}
        pathEdges = []
        pairs = []
        

        # rGraph is the residual graph
        cGraph = graph(roomie, days)
        rGraph = deepcopy(cGraph)
        
        # setting nodes to not visited
        for node in cGraph:
            discovered[node] = False

        edgeList, flow = edgelis(cGraph)
            
        # while there is an src to sink path
        while DFS(rGraph, "src", "sink", discovered, path)[0]:

            # reset currentPath
            currentPath = []
            # finding the paths
            currentPath = list(DFS(rGraph, "src", "sink", discovered, path)[1])

            # reset path
            path = deque()
            for i in range(len(currentPath)):
                if currentPath[i] != 'sink' and ((currentPath[i],currentPath[i + 1]) not in pathEdges):
                    # creating the list of edges in path
                    pathEdges.append((currentPath[i],currentPath[i + 1]))

            # resetting nodes to not visited 
            for i in discovered:
                discovered[i] = False
            
            # determining flow based on paths
            for i in flow:
                if i in pathEdges:
                    flow[i] = 1

            # updates the residual graph
            for i in pathEdges:
                # if the flow through an edge is 1
                if flow[i] == 1: 
                    # add the first point to the second
                    rGraph[i[1]].append(i[0]) 
                    # remove second point from first point
                    rGraph[i[0]].remove(i[1]) 

                    # for solutions
                    if (i[1] in days):
                        pairs.append(i)
                    elif i[::-1] in pairs:
                        pairs.remove(i[::-1])

            # updating the flow
            flow = augment(flow, pathEdges)

            # reset pathEdges
            pathEdges = []

        if len(rGraph['src']) == 0:
            #print("Ergonomic")

            # print pairings
            #print("Pairs:", pairs)
            #print()

            return rGraph, pairs
        else:
            #print("Not Ergonomic")
                
            # certificate(cGraph, rGraph, days)
            return rGraph, pairs  
    
    # certificate function to prove why its not ergonomic
    def certificate(cGraph, rGraph, days):
        path = deque()
        discovered = {}
        srcList = []
        lyst = []
        
        # setting nodes to not visited
        for node in cGraph:
            discovered[node] = False

        # makes list for switches (basically)
        for node in rGraph:
            # print(node)
            if DFS(rGraph, "src", node, discovered, path)[0]:
                if (node not in days) and (node != 'src'):
                    srcList.append(node)

            # resetting nodes to not visited 
            for i in discovered:
                discovered[i] = False
        # print("SrcList:", srcList)

        # makes list of possible light mapping
        for node in srcList:
            for day in cGraph[node]:
                if day not in lyst:
                    lyst.append(day)
            
        # if srcList is bigger than lyst than its not ergonomic
        if len(srcList) > len(lyst):
            print("People:", srcList)
            print("Possible nights they can cook:", lyst)
            print("Certificate: Since the number of people is bigger than the number of possible nights people can cook, it's not ergonomic")

    #Let's time it! Thanks to Brandon Chupp, who deciphered all this
    def wrapper(func, *args): #wraps a function to allow the timeit function to use it
        def wrapped():
            return func(*args)
        return wrapped

    #passes our NewSan function through the wrapper
    FF = wrapper(fordFulkerson, roomie, days)

    #average runtime of 10,000 trials of size n
    print(n,",", timeit(FF, number = 1000)/1000)


for i in range(1, 31):
    getData(i)

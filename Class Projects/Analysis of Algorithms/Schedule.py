from DFS import * #depth first search file source: source: https://www.techiedelight.com/find-path-between-vertices-directed-graph/
from collections import deque
from copy import deepcopy

# days needed to cook
'''
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
roomie = {'Nate': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 
        'Aidan': ['Monday', 'Wednesday', 'Friday', 'Saturday'],
        'Anna': ['Tuesday', 'Thursday', 'Friday', 'Sunday'],
        'Daniel': ['Saturday', 'Sunday'], 
        'Chuck': ['Tuesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'Jesse': ['Monday','Wednesday', 'Saturday', 'Sunday'],
        'Levi': ['Tuesday', 'Wednesday', 'Thursday', 'Friday']}
'''

days = [1, 2, 3, 4, 5, 6, 7]
roomie = {'A': [1, 2, 3, 4, 5], 
        'B': [1, 3, 5, 6],
        'C': [2, 4, 5, 7],
        'D': [6, 7], 
        'E': [2, 4, 5, 6, 7],
        'F': [1, 3, 6, 7],
        'G': [2, 3, 4, 5]}
'''

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
roomie = {'Nate': ['Monday'], 
        'Aidan': ['Monday'],
        'Anna': ['Tuesday'],
        'Daniel': ['Saturday', 'Sunday'], 
        'Chuck': ['Tuesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'Jesse': ['Monday','Wednesday', 'Saturday', 'Sunday'],
        'Levi': ['Tuesday', 'Wednesday', 'Thursday', 'Friday']}
'''

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
        print("Ergonomic")

        # print pairings
        print("Pairs:", pairs)
        print()

        return rGraph, pairs
    else:
        print("Not Ergonomic")
            
        certificate(cGraph, rGraph, days)
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


fordFulkerson(roomie, days)
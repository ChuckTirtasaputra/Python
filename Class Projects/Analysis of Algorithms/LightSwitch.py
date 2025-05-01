# Chuck Tirtasaputra
'''
I got all of the parts working. It checks if its ergonomic and prints the 
pairings if it is. If its not, it prints out the switches and possible light
mappings as a certificate.
'''
from DFS import * #depth first search file source: source: https://www.techiedelight.com/find-path-between-vertices-directed-graph/
from collections import deque
from copy import deepcopy

wa = [(1,2),(1,5),(8,5),(8,3),(11,3),(11,1),(5,1),(5,3),(4,3),(4,1),(1,1),(1,2)]
lts,sw = [(2,4),(2,2),(5,4)], [(6,2),(7,4),(6,3)]

# from the code snippet Daniel the GOAT
def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])
    # Return true if line segments AB and CD intersect
    # Source: http://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def visible(pt1,pt2,Walls):
    x1,y1 = pt1
    x2,y2 = pt2
    for i,wall in enumerate(Walls[:-1]):
        x3,y3 = wall
        x4,y4 = Walls[i+1]
        if intersect((x1,y1),(x2,y2),(x3,y3),(x4,y4)):
            return False
    return True  

# creating the graph
def graph(lts, sw, wa):
    liList = {} # the graph dictionary

    for i in sw:
        liList[i] = []
    for switch in sw:
        for light in lts:
            if visible(switch, light, wa) == True:
                liList[switch].append(light)
    # connects the source to the switch
    liList["src"] = sw
    # connects the lights to the sink
    for i in lts:
        liList[i] = ["sink"]
    liList['sink']=[]
    # print(liList)
    return liList

# creating list of edges and their flow
def edgelis(liList):
    edgeList = []
    flow = {}
    for i in liList:
        for j in liList[i]:
            edgeList.append((i, j))
    for i in edgeList:
        flow[i] = 0
    return edgeList, flow

# ford fulkerson to see if its ergonomic and to find the pairings
def fordFulkerson(lts, sw, wa):
    path = deque()
    discovered = {}
    pathEdges = []
    pairs = []

    # rGraph is the residual graph
    rGraph = {}
    liList = graph(lts, sw, wa)
    rGraph = liList
    cGraph = deepcopy(rGraph)
 
    # setting nodes to not visited
    for node in liList:
        discovered[node] = False

    edgeList, flow = edgelis(liList)
    
    # while there is an src to sink path
    while DFS(rGraph, "src", "sink", discovered, path)[0]:
        flow = {}
        edgeList = []

        # creating list of edges and their flow
        for i in rGraph:
            for j in rGraph[i]:
                edgeList.append((i,j))
        for i in edgeList:
            flow[i] = 0
        
        # finding the paths
        currentPath = list(DFS(rGraph, "src", "sink", discovered, path)[1])
        # print("Current Path:", currentPath)
        for i in range(len(currentPath)):
            if currentPath[i] != 'sink':
                #creating the list of edges in path
                pathEdges.append((currentPath[i],currentPath[i + 1]))
        # print("PathEdges:", pathEdges)

        # resetting nodes to not visited 
        for i in discovered:
            discovered[i] = False
        
        # determining flow based on paths
        for i in flow:
            if i in pathEdges:
                flow[i] = 1
        # print("Flow:", flow)

        # updates the residual graph
        for i in flow:
            # if the flow through an edge is 1
            if flow[i] == 1: 
                # add the first point to the second
                rGraph[i[1]].append(i[0]) 
                # remove second point from first point
                rGraph[i[0]].remove(i[1]) 
        print("rGraph:", rGraph)
        #print("cGraph:", cGraph)
        # print("Path:", path)

    if len(sw) == 0:
        print("Ergonomic")

        # print pairings
        for light in lts:
            switch = rGraph[light][0]
            pairs.append((switch, light))
        print("Pairs:", pairs)

        return rGraph, len(lts)
    else:
        print("Not Ergonomic")

        # print possible pairings and leaves out the rest
        for light in lts:
            if rGraph[light][0] != 'sink':
                switch = rGraph[light][0]
                pairs.append((switch, light))
            else:
                continue
        print("Pairs:", pairs)
        return rGraph, len(pairs)        

# certificate function to prove why its not ergonomic
def certifcate(cGraph, rGraph, lts):
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
            if (node not in lts) and (node != 'src'):
                srcList.append(node)

        # resetting nodes to not visited 
        for i in discovered:
            discovered[i] = False
    # print("SrcList:", srcList)

    # makes list of possible light mapping
    for node in srcList:
        for light in cGraph[node]:
            if light not in lyst:
                lyst.append(light)
    
    # if srcList is bigger than lyst than its not ergonomic
    if len(srcList) > len(lyst):
        print("Switches:", srcList)
        print("Possible lights that can be mapped:", lyst)
        print("Certificate: Since the number of switches is bigger than the number of lights that can be mapped, it's not ergonomic")

# Running the actual algorithm and functions
# copy of the original graph for certificate
cGraph = graph(lts, sw, wa)

# copy of the residual graph for certificate
rGraph, maxFlow = fordFulkerson(lts, sw, wa)

#print('cGraph:', cGraph)
#print('rGraph:', rGraph)
#print('Max Flow:', maxFlow)

certifcate(cGraph, rGraph, lts)
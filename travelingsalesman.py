'''
Algorithm reference: http://cs.indstate.edu/cpothineni/alg.pdf

Requirements:
- Accept problem instances on the command line
- Name the output file as the input file's name with .tour appended (for example 
  input tsp_example_1.txt will output tsp_example_1.txt.tour)
- Compile/Execute correctly and without debugging on engineering servers 
  according to specifications and any documentation you provide.

Input specifications:
- A problem instance will always be given to you as a text file.
- Each line defines a city and each line has three numbers separated by white 
  space.
- The first number is the city identifier
- The second number is the city's x-coordinate
- The third number is the city's y-coordinate.
 
Output specifications:
- You must output your solution into another text file with n+1 lines, where n 
  is the number of cities.
- The first line is the length of the tour your program computes.
- The next n lines should contain the city identifiers in the order they are 
  visited by your tour.
- Each city must be listed exactly once in this list.
'''

import sys
import datetime
from math import sqrt

def rowMin(cost, i):
    rMin = cost[i][0]
    for j in range(n):
        if cost[i][j] < rMin:
            rMin = cost[i][j]
    return rMin

def colMin(cost, j):
    cMin = cost[0][j]
    for i in range(n):
        if cost[i][j] < cMin:
            cMin = cost[i][j]
    return cMin

def reduceRows(cost):
    row = 0
    for i in range(n):
        rMin = rowMin(cost, i)
        if rMin != float('inf'):
            row = row + rMin
        for j in range(n):
            if cost[i][j] != float('inf'):
                cost[i][j] = cost[i][j] - rMin

def reduceCols(cost):
    col = 0
    for j in range(n):
        cMin = colMin(cost, j)
        if cMin != float('inf'):
            col = col + cMin
        for i in range(n):
            if cost[i][j] != float('inf'):
                cost[i][j] = cost[i][j] - cMin

# Calculate the bounds
# Parameters: start city, destination city, adjacency matrix of city distances,
# list of edge costs so far
def getBounds(start, dest, cost, edgeCost):
    n = len(cost)
    reduced = [row[:] for row in cost] # create copy of cost to be reduced

    # Filter out irrelevant costs by setting to infinity
    for j in range(n):
        reduced[start][j] = float('inf') # set start row to infinity
    for i in range(n):
        reduced[i][dest] = float('inf') # set dest column to infinity
    reduced[dest][start] = float('inf') # set [dest][start] to infinity

    reductionCost = reduceRows(reduced)
    reductionCost += reduceCols(reduced)

    # distance from start to dest + reduction cost + reduction cost so far
    edgeCost[dest] = cost[start][dest] + reductionCost + edgeCost[start]

# Execute branch and bound algorithm; called "main" in the reference
def branchAndBound(cost):
    n = len(cost)
    done = [False] * n # list to keep track of cities that have been processed

    initReductionCost = reduceRows(cost)
    initReductionCost += reduceCols(cost) # initial row + col reduction cost
    edgeCost = [initReductionCost] * n # list of lower-bound cost per city

    currentCity = 0 # start at first city in cost (arbitrary)
    while not any(done): # while there are Falses in done, i.e. unchecked cities
        # Calculate lower-bound cost from currentCity to all others
        for i in range(n):
            if done[i] == False:
                getBounds(k, i, cost, edgeCost) # TODO: initialize k

        # Find city with lowest lower-bound cost
        min = float('inf')
        for i in range(n):
            if done[i] == False:
                if edgeCost[i] < min:
                    min = edgeCost[i]
                    currentCity = i
        done[currentCity] = True
        
        for p in range(1, n):
            cost[j][p] = float('inf')
        for p in range(1, n):
            cost[p][currentCity] = float('inf')
        cost[currentCity][j] = float('inf')
        
        reduceRows(cost)
        reduceCols(cost)

    return # TODO: return something

# Parameters: list of [x, y] pairs, indexed by city ID
def createEdgeList(coords):    
    # Create empty 2D list of size (n * n)
    n = len(coords)
    edgeList = [None] * n
    for i in range(n):
        edgeList[i] = [float('inf')] * n

    for i in range(n):
        for j in range(n):
            if i == j:
                edgeList[i][j] = float('inf')
            else:
                # dist = sqrt((x2 - x1)^2 + (y2 - y1)^2)
                edgeList[i][j] = int(sqrt((coords[i][0] - coords[j][0])**2
                                        + (coords[i][1] - coords[j][1])**2))
    return edgeList

# Read input, call branch and bound function, write output
def main():
    if len(sys.argv) != 2:
        print("Usage: python travelingsalesman.py inputfilename")
    else:
        print("Start: " + str(datetime.datetime.now().time()))
        inFile = sys.argv[1] # first argument
        outFile = inFile + ".tour" # ex. input.txt -> input.txt.tour
        output = ""

        with open(inFile) as f: # inFile is open in this block and auto-closed after
            read_data = f.read() # get entire file content as string

        coords = [] # list of x, y coordinates, indexed by city ID
        arr = read_data.split('\n') # split content into lines
        for i in range(len(arr)): # for each line
            if len(arr[i]) > 0:
                arr[i] = arr[i].split() # split into [identifier, x, y]
                arr[i] = list(map(int, arr[i])) # convert contents to int
                coords.append(arr[i][1:3]) # add each [x, y] to coordinates
        edgeList = createEdgeList(coords)

        with open(outFile, "w") as f:
            f.write(output)
        print("Finish: " + str(datetime.datetime.now().time()))
main()
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

INT_MAX = 0
final_res = 0


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

#copy temp solution to final solution
def copyToFinal(curr_path, final_path, N):
    for i in range(0, N):
        final_path[i] = curr_path[i]
    final_path[N] = curr_path[0]

#function to find the min edge cost having the vertex i
def firstMin(edgeList, i, cityCount):
    global INT_MAX
    min = INT_MAX
    for k in range (0, cityCount):
        if edgeList[i][k] < min and i != k:
            min = edgeList[i][k]
    return min

#function to find the second min edge cost having an end at vertex i
def secondMin(edgeList, i, cityCount):
    global INT_MAX
    first = INT_MAX
    second = INT_MAX
    for j in range (j, cityCount):
        if i == j:
            continue

        if edgeList[i][j] <= first:
            second = first
            first = edgeList[i][j]
        elif edgeList[i][j] <= second and edgeList[i][j] != first:
            second = edgeList[i][j]

    return second

def TSPREec(edgeList, curr_bound, curr_weight, level, curr_path, final_path, cityCount, visited):
    global final_res
    if (level == cityCount):
        if (edgeList[curr_path[level - 1]][curr_path[0]] != 0):
            curr_res = curr_weight + edgeList[curr_path[level - 1]][curr_path[0]]

            if curr_res < final_res:
                copyToFinal(curr_path)
                final_res = curr_res
        return

    #for any other level iterate for all vetices to build the search space tree recursively
    for i in range (0, cityCount):
        #consider next vertex if it is not same (diagonal entry in adj matrix and not visited already
        if (edgeList[curr_path[level-1]][i] != 0 and visited[i] == false):
            temp = curr_bound
            curr_weight += edgeList[curr_path[level -1]][i]

            if (level == 1):
                curr_bound = curr_bound - ((firstMin(edgeList, curr_path[level-1], cityCount) + firstMin(edgeList, i, cityCount)) / 2)

            else:
                curr_bound = curr_bound - ((secondMin(edgeList, curr_path[level-1], cityCount) + firstMin(edgeList, i, cityCount)) / 2)
            
            
            if (curr_bound + curr_weight < final_res):
                curr_path[level] = i
                visited[i] = True

                #call helper function for next level
                TSPREec(edgeList, curr_bound, curr_weight, level + 1, curr_path, final_path, cityCount, visited)

            #else we need too prune the nodes
            curr_weight = curr_weight - edgeList[curr_poath[level-1]][i]
            curr_bound = temp
            for k in range(0, len(visited)):
                visited = False
            for k in range(0, len(visited) -1):
                visited[curr_path[k]] = True


def TSP(edgeList, cityCount, visited, final_path):
    curr_path[cityCount +1]

    curr_bound = 0
    for i in range (0, len(curr_path)):
        curr_path[i] = -1
    for i in range(0, len(visited)):
        visited = False

    #compute initial bound
    for i in range(0, cityCount):
        curr_bound = curr_bound + firstMin(edgeList, i, cityCount) + secondMin(edgeList, i, cityCount)

    visited[0] = True
    curr_path[0] = 0

    TSPREec(edgeList, curr_bound, 0, 1, curr_path, final_path, cityCount, visited)




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
        #edgeList = createEdgeList(coords)

        # get the number of cities
        cityCount = len(coords)
        #output final path list
        final_path[cityCount +1]

        #keep track of already visited nodes in a path
        visited[cityCount]
        for i in range(0, len(visited)):
            visited = False

        global INT_MAX
        #store final min weight of shortest tour
        minWeightShortestTour = INT_MAX

        #create the edge list
        edgeList = createEdgeList(coords)


        TSP(edgeList, cityCount, visited, final_path)

        print("Minimum cost : " + str(final_res))
        print("Path Taken : ");
        for i in range (0, cityCount):
            print(final_path[i], end=" ")
        print("")


        
        #with open(outFile, "w") as f:
      #      f.write(output)
      #  print("Finish: " + str(datetime.datetime.now().time()))
        

if __name__ == '__main__':
    main()
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

def rowMin(cost[n][n], i):
    rMin = cost[i][0]
    for j in range(n-1):
        if cost[i][j] < rMin:
            rMin = cost[i][j]
    return rMin

def colMin(cost[n][n], j):
    cMin = cost[0][j]
    for i in range(n-1):
        if cost[i][j] < cMin:
            cMin = cost[i][j]
    return cMin

def rowReduction(cost[n][n]):
    row = 0
    for i in range(n-1):
        rMin = rowMin(cost, i)
        if rMin != float('inf'):
            row = row + rMin
        for j in range(n-1):
            if cost[i][j] != float('inf'):
                cost[i][j] = cost[i][j] - rMin

def colReduction(cost[n][n]):
    col = 0
    for j in range(n-1):
        cMin = colMin(cost, j)
        if cMin != float('inf'):
            col = col + cMin
        for i in range(n-1):
            if cost[i][j] != float('inf'):
                cost[i][j] = cost[i][j] - cMin

# Calculate the bounds
# Arguments: start city, destination city, adjacency matrix of city distances,
# list of edge costs so far
def getBounds(start, dest, matrix, edgeCost):
	n = len(matrix)
	reduced = [row[:] for row in matrix] # create copy of matrix to be reduced

	# Filter out irrelevant costs by setting to infinity
	for j in range(n):
		reduced[start][j] = float("inf") # set start row to infinity
	for i in range(n):
		reduced[i][dest] = float("inf") # set dest column to infinity
	reduced[dest][start] = float("inf") # set [dest][start] to infinity

	reductionCost = reduceRows(reduced)
	reductionCost += reduceCols(reduced)

	# distance from start to dest + reduction cost + reduction cost so far
	edgeCost[dest] = matrix[start][dest] + reductionCost + edgeCost[start]

# Execute branch and bound algorithm; called "main" in the reference
def branchAndBound(matrix):
	n = len(matrix)
	done = [False] * n # list to keep track of cities that have been processed

	initReductionCost = reduceRows(matrix)
	initReductionCost += reduceCols(matrix) # initial row + col reduction cost
	edgeCost = [initReductionCost] * n # list of lower-bound cost per city

	currentCity = 0 # start at first city in matrix (arbitrary)
	while not any(done): # while there are Falses in done, i.e. unchecked cities
		# Calculate lower-bound cost from currentCity to all others
		for i in range(n):
			if done[i] == False:
				getBounds(k, i, matrix, edgeCost) # TODO: initialize k

		# Find city with lowest lower-bound cost
		min = float("inf")
		for i in range(n):
			if done[i] == False:
				if edgeCost[i] < min:
					min = edgeCost[i]
					currentCity = i
		done[currentCity] = True
		
		for p in range(1, n):
			matrix[j][p] = float("inf")
		for p in range(1, n):
			matrix[p][currentCity] = float("inf")
		matrix[currentCity][j] = float("inf")
		
		reduceRows(matrix)
		reduceCols(matrix)

	return # TODO: return something

# Read input, call branch and bound function, write output
def main():
	if len(sys.argv) != 2:
		print("Usage: python travelingsalesman.py inputfilename")
	else:
		inFile = sys.argv[1] # first argument
		outFile = inFile + ".tour" # ex. input.txt -> input.txt.tour
		output = ""

		with open(inFile) as f: # inFile is open in this block and auto-closed after
			read_data = f.read() # get entire file content as string

		cities = {} # to hold cities, key: city identifier, value: [x, y]

		arr = read_data.split('\n') # split content into lines
		for i in range(len(arr)): # for each line
			if len(arr[i]) > 0:
				arr[i] = arr[i].split() # split into [identifier, x, y]
				cities[arr[i][0]] = arr[i][1:3] # add to dict

		with open(outFile, "w") as f:
			f.write(output)
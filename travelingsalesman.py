'''
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
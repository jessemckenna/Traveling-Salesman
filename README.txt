Run:
	To run traveling salesman, execute the following console command:
	python travelingsalesman.py inputfilename

Prerequisite:
	A problem instance must be given as a text file with the following format:
	- Each line defines a city and each line has three numbers separated by 
	  white space
	- The first number is the city identifier
	- The second number is the city's x-coordinate
	- The third number is the city's y-coordinate

Result:
	The solution will be output into another text file with n+1 lines, where n 
	is the number of cities. Output filename will be the input filename, with
	the added file extension ".tour".

	Output contents:
	- The first line is the length of the tour computed
	- The next n lines contain the city identifiers in the order visited by the
	  tour
	- Each city is listed exactly once
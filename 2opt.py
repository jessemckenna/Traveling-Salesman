# Group 27: Heather Godsell, Jesse McKenna, Mario Franco-Munoz
# CS325 Project: Traveling Salesman

import sys
import datetime
from math import sqrt
from math import pow

MAX_TRIES = 20
TIME_LIMIT = 175 # start finishing up after this many seconds

class Node:
    def __init__(self, coords):
        self.ID = coords[0] #attribute to keep track of the ID
        self.x = coords[1]  #attribute to keep track of x coord
        self.y = coords[2]  #attribute to keep track of y coord


#source: https://en.wikipedia.org/wiki/2-opt      
def opt2Swap(route, i, k, n, best_distance):
    new_distance = best_distance
    new_distance -= getDistance(route[i], route[i - 1]) # disconnected
    new_distance += getDistance(route[k], route[i - 1]) # new connection

    if k + 1 == n: # replace connection with ending city (city 0)
        new_distance -= getDistance(route[k], route[0])
        new_distance += getDistance(route[i], route[0])
    else: # replace connection with city k + 1
        new_distance -= getDistance(route[k], route[k + 1])
        new_distance += getDistance(route[i], route[k + 1])

    if new_distance < best_distance:
        #"take route[0] to route[i-1] and add them in reverse order to new_route" 
        new_route = route[:i]    #i is not inclusive, so this is the equivalent as i-1

        #"take route[i] to route[k] and add them in reverse order to new_route"
        new_route.extend(reversed(route[i:k+1]))     #again, upper bounds are not inclusive in python

        #"take route[k+1] to end and add them in order to new_route"
        new_route.extend(route[k+1:])

        return new_distance, new_route

    else:
        return new_distance, route


def getDistance(node1, node2):
    #get the euclidean distance
    d = sqrt(pow((node2.y - node1.y), 2) + pow((node2.x - node1.x), 2))

    #round the number
    d = int(round(d))
    return d


def routeDistance(route, n):
    d = 0 # distance
    for i in range(1, n): # sum distances between nodes in the order given
        d += getDistance(route[i - 1], route[i])
    d += getDistance(route[-1], route[0]) # add distance back to start

    return d


# source: http://www.technical-recipes.com/2012/applying-c-implementations-of-2-opt-to-travelling-salesman-problems/
# Parameters: route (an array of Node objects), n (count of objects in route)
def opt2(route, n, startTime):
    existing_route = route
    best_distance = routeDistance(route, n)
    tries = 0

    global TIME_LIMIT
    global MAX_TRIES

    improveFound = True      #extra bool variable since we do not have access to the "goto" label in python

    while tries < MAX_TRIES and (datetime.datetime.now() - startTime).seconds < TIME_LIMIT:
        if improveFound == False:
            break
        improveFound = False
        for i in range(1, n - 1):
            for k in range(i + 1, n):
                new_distance, new_route = opt2Swap(existing_route, i, k, n, best_distance)
                if new_distance < best_distance: # improvement found; reset
                    tries = 0
                    improveFound = True
                    existing_route = new_route
                    best_distance = new_distance
                    break
                
            if improveFound == True:
                break

        tries += 1

    return best_distance, existing_route


#get min distance from a given node
def minDistance(arr, src):
    min = sys.maxsize
    for i in arr:
        temp = getDistance(src, i)
        if temp < min and i != src:
            min = temp
            nearestN = i

    return nearestN


def greedyRoute(graph, n):
    cities = graph[:] # remaining cities to travel to
    route = [cities.pop(0)] # resulting route (begins with start city)
    current = graph[0]


    while len(cities) > 0:
        current = minDistance(cities, current)

        cities.remove(current)
        route.append(current) # add closest node to route
    
    return route


def main():
    if len(sys.argv) != 2:
        print("Usage: python travelingsalesman.py inputfilename")
    else:
        startTime = datetime.datetime.now()
        print("Start: " + str(startTime))

        inFile = sys.argv[1] # first argument
        outFile = inFile + ".tour" # ex. input.txt -> input.txt.tour

        with open(inFile) as f: # inFile is open in this block and auto-closed after
            read_data = f.read() # get entire file content as string

        vertices = []   #store all the nodes in a list
        count = 0       #for initialization of node's order
        bestTour = []

        arr = read_data.split('\n') # split content into lines
        for i in range(len(arr)): # for each line
            if len(arr[i]) > 0:

                arr[i] = arr[i].split() # split into [identifier, x, y]
                arr[i] = list(map(int, arr[i])) # convert contents to int

                newNode = Node(arr[i])
                vertices.append(newNode) # add each city (Node) to vertices
                count += 1

        greedy = greedyRoute(vertices, count) # begin with a greedy tour
        print("Set up completed in " + str(datetime.datetime.now() - startTime))

        tourLength, bestTour = opt2(vertices, len(vertices), startTime)

        with open(outFile, "w") as f:
            f.write(str(tourLength) + "\n") # write tour length to first line
            for i in range(count):
                f.write(str(bestTour[i].ID) + "\n")

        finishTime = datetime.datetime.now()
        elapsedTime = finishTime - startTime

        print("Finish: " + str(finishTime))
        print("Elapsed: " + str(elapsedTime))


if __name__ == '__main__':
    main()

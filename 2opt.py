



import sys
import datetime
from random import seed
from random import randint
from math import sqrt
from math import pow

class Node:

    def __init__(self, coords):
        self.ID = coords[0] #attribute to keep track of the ID
        self.x = coords[1]  #attribute to keep track of x coord
        self.y = coords[2]  #attribute to keep track of y coord



#source: https://en.wikipedia.org/wiki/2-opt      
def opt2Swap(route, i, k):

    #"take route[0] to route[i-1] and add them in reverse order to new_route" 
    new_route = route[:i]    #i is not inclusive, so this is the equivalent as i-1

    #"take route[i] to route[k] and add them in reverse order to new_route"
    new_route.extend(reversed(route[i:k+1]))     #again, upper bounds are not inclusive in python

    #"take route[k+1] to end and add them in order to new_route"
    new_route.extend(route[k+1:])

    return new_route


def getDistance(node1, node2):
    #get the euclidean distance
    d = sqrt(pow((node1.y - node1.x), 2) + pow((node2.y - node2.x), 2))

    #round the number
    d = int(round(d))
    return d
    

def opt2():
    improved = False
    swappableNodes = 0
    while !improved:
       start_again:
       best_distance = calculateTotalDistance(existing_route)
       for i in range(1, swappableNodes - 1):
           for k in range(i + 1, swappableNodes):
               new_route = opt2Swap(existing_route, i, k)
               new_distance = calculateTotalDistance(new_route)
               if new_distance < best_distance:
                   existing_route = new_route
                   goto start_again # TODO

# Fisher-Yates shuffle
def shuffle(list):
    n = len(list)
    for i in range(n):
        j = randint(i, n - 1) # i <= j < n
        list[i], list[j] = list[j], list[i] # swap elements i and j



def main():
    if len(sys.argv) != 2:
        print("Usage: python travelingsalesman.py inputfilename")
    else:
        print("Start: " + str(datetime.datetime.now().time()))
        
        seed(None) # seed from current time

        inFile = sys.argv[1] # first argument
        outFile = inFile + ".tour" # ex. input.txt -> input.txt.tour
        output = ""

        with open(inFile) as f: # inFile is open in this block and auto-closed after
            read_data = f.read() # get entire file content as string

        
        vertices = []        #store all the nodes in a list
        count = 0           #for initialization of node's order
        tempX = 0
        tempY = 0
        tempID = 0

        arr = read_data.split('\n') # split content into lines
        for i in range(len(arr)): # for each line
            if len(arr[i]) > 0:
                count = count + 1

                temp = [int(x) for x in (arr[i].strip().split(" "))] # split into identifier, x, y
         
                
                n = Node(temp)  #the above could be combined into one line later, just wanted to be clear
                vertices.append(n)



        #shuffle the nodes to randomize the path as per 2-opt procedure
        shuffle(vertices)
        
        #call main driver program here



if __name__ == '__main__':
    main()
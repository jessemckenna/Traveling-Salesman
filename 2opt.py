



import sys
import datetime
from math import sqrt
from random import shuffle

class Node:

    def __init__(self, coords):
        self.ID = coords[0]   #attribute to keep track of the ID
        self.x = coords[1]       #attribute to keep track of x coord
        self.y = coords[2]      #attribute to keep track of y coord



#source: https://en.wikipedia.org/wiki/2-opt      
def optSwap(route, i, k):

    #"take route[0] to route[i-1] and add them in reverse order to new_route" 
    new_route = route[:i]    #i is not inclusive, so this is the equivalent as i-1

    #"take route[i] to route[k] and add them in reverse order to new_route"
    new_route.extend(reversed(route[i:k+1]))     #again, upper bounds are not inclusive in python

    #"take route[k+1] to end and add them in order to new_route"
    new_route.extend(route[k+1:])

    return new_route



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

       

        #test call
        print("exiting")
        for i in vertices:
            print(str(i.x) + " " + str(i.y))



if __name__ == '__main__':
    main()
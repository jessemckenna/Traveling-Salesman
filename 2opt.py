import sys
import datetime
from math import sqrt

class Node:

    def __init__(self, coords):
        self.ID = coords[0]   #attribute to keep track of the ID
        self.x = coords[1]       #attribute to keep track of x coord
        self.y = coords[2]      #attribute to keep track of y coord
        self.order = coords[3]     #attribute to keep track of the order

    def addVertices(self, listInput):
        for i in listInput:
            self.order 









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
         
                tempOrder = count     #initialize the node order - 2-OPT is supposed to use a random order 
                                     #so we can change this later we would basically have to implement a function
                                     #that makes a distribution of the IDs (randomization without repetition)
                                     #it's kind of annoying, but I've already done it once in C or C++, it's in my code
                                     #folder somewhere... -mario
                temp.append(tempOrder)
                
                n = Node(temp)  #the above could be combined into one line later, just wanted to be clear
                vertices.append(n)

                #arr[i] = list(map(int, arr[i])) # convert contents to int
                #coords.append(arr[i][1:3]) # add each [x, y] to coordinates









        #test call
        print("exiting")
        for i in vertices:
            print(str(i.x) + " " + str(i.y))



if __name__ == '__main__':
    main()
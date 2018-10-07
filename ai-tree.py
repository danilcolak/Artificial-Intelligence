import sys
class Node:
    def __init__(self): #Node initialize
        self.cannibal = None
        self.missioner= None
        self.boatSide= None
        self.parent= None
        self.children = []

    def createChild(self,c,m,b):
        newChild = Node()
        newChild.cannibal=c
        newChild.missioner=m
        newChild.boatSide=b
        newChild.parent=self
        if (newChild.birthControl()):
            self.children.append(newChild)

    def printFunc(self, p=""): #print function
        print(p,self.cannibal,self.missioner,self.boatSide)

    def birthControl(self): # controls if the child is possible for the situation
        if (self.parent is not None):
            if(self.parent.parent is not None):
                if(self.parent.parent.cannibal == self.cannibal and self.parent.parent.missioner == self.missioner and self.parent.parent.boatSide == False): # controls for  if tree is not repeating to the same step
                    return False
        if (self.missioner != 0):
            if(self.cannibal > self.missioner):  #controls for the situation that cannibals are more than the missioners to prevent missioner's death
                return False
        if ((3 - self.missioner) != 0):
            if ((3 - (self.cannibal)) > (3 - (self.missioner))): # controls for the other side of the land
                return False
        if(self.cannibal > 3 or self.cannibal < 0):
            return False
        if (self.missioner > 3 or self.missioner < 0):
            return False
        return True

    def mychildren(self):
        if (self.boatSide == True): #when boat goes to the other side
            self.createChild(self.cannibal - 2, self.missioner, not self.boatSide)
            self.createChild(self.cannibal, self.missioner - 2, not self.boatSide)
            self.createChild(self.cannibal - 1, self.missioner - 1, not self.boatSide)
            self.createChild(self.cannibal - 1, self.missioner, not self.boatSide)
            self.createChild(self.cannibal, self.missioner - 1, not self.boatSide)
        else: # when boat cames from the other side
            self.createChild(self.cannibal + 2, self.missioner, not self.boatSide)
            self.createChild(self.cannibal, self.missioner + 2, not self.boatSide)
            self.createChild(self.cannibal + 1, self.missioner + 1, not self.boatSide)
            self.createChild(self.cannibal + 1, self.missioner, not self.boatSide)
            self.createChild(self.cannibal, self.missioner + 1, not self.boatSide)


def recursive(root, p="", dept = 0):
    if (dept > 11): # dept counts the step size if we want we can find solution in more steps  ,but the minimum steps for the algorithm is 11
        return
    root.mychildren()
    root.printFunc(p)
    if (root.cannibal == 0 and root.missioner == 0 and root.boatSide == False):# controls the recursive function for infinite loop
        print(dept)
        sys.exit(0)

    for child in root.children:
        recursive(child, p + "|  ", dept + 1)

def main() :
    root = Node()
    root.cannibal = 3
    root.missioner = 3
    root.boatSide = True

    recursive(root)

if __name__ == '__main__':
    main()


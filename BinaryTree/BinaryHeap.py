## creates a BinaryHeap (Max)
##
##

import random

class BinaryHeapNode:
    priority, value = None, None
    def __init__(self, value, priority = 1):
        self.priority = priority
        self.value = value
    
class BinaryHeap:
    tail, theList,  =  0, []
    def __init__(self):
        pass
    
    def insert(self, x):
        if ( not isinstance(x, BinaryHeapNode) ):
            raise Exception("Must insert BinaryHeapNode object")
        self.theList.append(x)
        self.percolateUp(self.tail)
        self.tail += 1

    def empty(self):
        return self.tail == 0

    def peek(self):
        return self.theList[0]
    
    def deleteMin(self):
        top = self.theList[0]
        self.tail -= 1
        self.theList[0] = self.theList[self.tail]
        self.percolateDown()
        return top

    def percolateDown(self):
        parent = 0
        done = False
        while ( not done):
            if ( not self.hasLeftChild(parent) and \
                 not self.hasRightChild(parent)): break
            old_parent = parent
            left_child = 2*parent+1
            right_child = 2*parent+2
            if ( self.hasLeftChild(parent)):
                if (self.theList[left_child].priority > \
                    self.theList[parent].priority):
                    parent = left_child
            if ( self.hasRightChild(parent)):
                if (self.theList[right_child].priority > \
                    self.theList[parent].priority):
                    parent = right_child
            if ( old_parent != parent ):
                self.swap(old_parent, parent)
            else:
                break
        

    def hasLeftChild(self, index):
        return 2*index+1 <= self.tail

    def hasRightChild(self, index):
        return 2*index+2 <= self.tail
            
    def percolateUp(self, child):
        if ( child == 0 ): return
        parent = int((child-1)/2)
        while (child != 0 and self.theList[parent].priority < self.theList[child].priority ):
            self.swap(parent,child)
            child = parent
            parent = int((child-1)/2)

    def swap(self, parent, child):
            self.theList[parent], self.theList[child] = \
                                  self.theList[child], self.theList[parent]
            


def main():
    print("Running...")
    vars = 20
    x = [i for i in range(vars)]
    y = [i for i in range(10,(10+vars))]
    random.shuffle(y)
    print(y)
    L = []
    for i in range(vars):
        L.append(BinaryHeapNode(y[i],x[i]))

    heap = BinaryHeap()
    print("inserting into Binary Heap...")
    for node in L:
        heap.insert(node)
        print(heap.peek().priority)
        
    print("removing from Binary Heap...")
    while( not heap.empty() ):
        print(str(heap.deleteMin().value))
        
    print("Done")

if __name__ == '__main__': main()

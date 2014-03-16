import sys
import Queue

class BiTreeNode:
    left, right, parent = None, None, None
    def __init__(self):
        pass

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getParent(self):
        return self.parent

    def setLeft(self,node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def setParent(self, node):
        self.parent = node

class BiTreeIntNode(BiTreeNode):
    val = None
    def __init__(self, val = -1):
        super(BiTreeIntNode, self)
        self.val = val

    def getValue(self):
        return self.val

    def setValue(self, value):
        self.val = value

class BiTreeStruct:
    def __init__(self, root = BiTreeIntNode() ):
        if ( isinstance(root, BiTreeIntNode) ):
            self.root = root
            self.size = 0;
        else:
            raise Exception("root must be of class BiTreeNode")

    def getRoot(self):
        return self.root

    def setRoot(self,node):
        if ( isinstance(root, BiTreeIntNode) ):
            self.root = node
        else:
            raise Exception("root must be of class BiTreeIntNode")

    #populate from an array
    # arr[0] = size
    # arr[1] = beginning tree
    # left child are at i*2
    # right child are at i*2+1
    def populate(self, arr):
        if (len(arr) < 2):
            raise Exception("array must contain at least 2 entries")
        self.root.setValue(arr[1])
        current = self.root
        self.size += 1
        i = 1;
        while ( self.size < arr[0] ):
            left = self.nextLeft(i)
            right = self.nextRight(i)
            if ( self.hasChild(left,arr) and current.getLeft() == None ):
                current = self.putAndGetChild("L", current, arr[left])
                self.size += 1
                i = left
            elif ( self.hasChild(right,arr) and current.getRight() == None):
                current = self.putAndGetChild("R", current, arr[right])
                self.size += 1
                i = right
            elif ( current.getParent() == None ):
                break
            else:
                current = current.getParent()
                i = int(i/2)

    def putAndGetChild(self, LorR, node, value):
        tmpNode = BiTreeIntNode(value)
        tmpNode.setParent(node)
        if (LorR == "L" ):
            node.setLeft(tmpNode)
            return node.getLeft()
        elif (LorR == "R"):
            node.setRight(tmpNode)
            return node.getRight()
        raise Exception("Improper Use of putAndGetchild")

    def hasChild(self,LorR, arr):
        if (LorR > arr[0] or arr[LorR] == None ):
            return False
        return True

    def nextLeft(self,index):
        return index*2

    def nextRight(self,index):
        return index*2+1


    def printInOrder(self, space = " "):
        self.recursiveInOrder(self.root, space)


    def recursiveInOrder(self, node, space):
        if (node == None): return
        nextSpace = space+space
        theValue = space
        theValue += str(node.getValue())
        self.recursiveInOrder(node.getLeft(),nextSpace)
        print(theValue)
        self.recursiveInOrder(node.getRight(),nextSpace)

    def toArray(self):
        theList = [self.size]
        q = Queue.Queue()
        q.put(self.root)
        while (not q.empty() ):
            tempNode = q.get()
            theList.append(tempNode.getValue())
            if (tempNode.getLeft() != None ):
                q.put(tempNode.getLeft())
            if (tempNode.getRight() != None ):
                q.put(tempNode.getRight())
        return theList
        


def main():
    print('Running Code...')
    tree = BiTreeStruct()
    arr = [9,4,2,6,1,3,5,7,5,6]
    for i in range(len(arr)):
        sys.stdout.write(str(arr[i])+',')
    print()
    tree.populate(arr)
    tree.printInOrder()
    print("=======")
    L = tree.toArray()
    for x in L:
        sys.stdout.write(str(x)+',')
    print();
    print('Done')
        
if __name__ == '__main__':main()
    

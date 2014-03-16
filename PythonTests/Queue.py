class QueueNode:
    value, next = None, None
    def __init__(self):
        pass

class Queue:
    head, tail, size = None, None, 0
    def __init__(self):
        pass

    def put(self, x):
        tmpNode = QueueNode()
        tmpNode.value = x
        tmpNode.next = None
        if (self.head == None ):
            self.head = tmpNode
            self.tail = self.head
        else:
            self.tail.next = tmpNode
            self.tail = self.tail.next
        self.size += 1

    def get(self ):
        tmpNode = self.head
        self.head = self.head.next
        self.size -= 1
        return tmpNode.value

    def empty(self):
        return self.size == 0
        
def main():
    q = Queue()
    a = [3,4,6,7]
    for x in a:
        q.put(x)
    while( not q.empty() ):
        print(q.get())

if __name__ == '__main__': main()

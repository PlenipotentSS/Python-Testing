

def change(alist):
    blist  = alist[:]
    blist[2] = 2
    return blist


def theList():
    global alist
    alist = [1,5,3,4]
    print alist[2]
    newList = change(alist)
    print newList[2]
    print alist[2]


theList()

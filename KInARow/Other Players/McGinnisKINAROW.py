import copy
import random
import time

ksize = 4
board = []
playTime = 0
debug = False
def prepare(k, mRows, nColumns, maxMillisecPerMove, isPlayingX, debugging):
    global ksize
    ksize = k
    
    global board
    board = [['' for c in range(nColumns)] for r in range(mRows)]
    
    global playTime
    playtime = maxMillisecPerMove
    
    global debug
    debug = debugging
    
    errors = ''
    if k > mRows or k > nColumns:
        errors += 'There is no way to win with k bigger than the board\n'
    
    if len(errors) > 0:
        return errors
    else:
        return 'ok'

def introduce():
    return '''Name: Daigakusei\nCreator: Brett McGinnis\nClue: I like rock band and beer'''

def nickname():
    return 'Gakusei'

def successors(state):
    states = []
    for r in range(len(state[1])):
        for c in range(len(state[1][r])):
            if state[1][r][c] == ' ':
                temp = copy.deepcopy(state)
                temp[1][r][c] = state[0]
                temp[0] = other(temp[0])
                states += [temp]
    return states
def makeMove(state):
    r = random.randint(0,len(states)-1)
    states = successors(state) 
    return [[other(state[0]),states[r]],sayings(0)]
def makeGoodMove(state):
    possibleMoves = successors(state)
    timet = time.time()
    maxPos = 0
    minPos = 0
    max = 0
    min = 0
    for i in range(len(possibleMoves)):
        maxT = makeGoodMoveRec(state,2, True, state[0],timet)
        minT = makeGoodMoveRec(state,2, False, state[0],timet)
        if maxT >= max:
            max = maxT
            maxPos = i
        if minT <= min:
            min = minT
            minPos = i
    SVmax =  staticValue(possibleMoves[maxPos])[0]
    SVmin =  staticValue(possibleMoves[minPos])[1]
    if SVmax == 1000 or SVmin == 1000:
        if SVmax == 1000:
            return [[other(state[0]),possibleMoves[maxPos][1]],sayings(1000)]
        else:
            return [[other(state[0]),possibleMoves[minPos][1]],sayings(1000)]
    if SVmax == -1000 or SVmin == -1000:
        if SVmax == -1000:
            return [[other(state[0]),possibleMoves[maxPos][1]],sayings(-1000)]
        else:
            return [[other(state[0]),possibleMoves[minPos][1]],sayings(-1000)]
    if SVmax == -100 or SVmin == -100:
        if SVmax == -100:
            return [[other(state[0]),possibleMoves[maxPos][1]],sayings(-100)]
        else:
            return [[other(state[0]),possibleMoves[minPos][1]],sayings(-100)]
    if SVmax == 100 or SVmin == 100:
        if SVmax == 100:
            return [[other(state[0]),possibleMoves[maxPos][1]],sayings(100)]
        else:
            return [[other(state[0]),possibleMoves[minPos][1]],sayings(100)]
    else:
        return [[other(state[0]),possibleMoves[maxPos][1]],sayings(0)]
    
##True = Max, False = Min
def makeGoodMoveRec(state, depth, isMax, origPlayer, startTime):
    if playTime > (time.time()-startTime-1)*.001:
        return 0
    staticvalue = staticValue(state)
    if isMax:
        if staticvalue[0] == 1000:
            if origPlayer == state[0]:
                if debug == True:
                    print 'Alpha could win'
                return 1000
    else:
        if staticvalue[1] == -1000:
            if origPlayer == state[0]:
                if debug == True:
                    print 'Beta could win'
                return -1000
    if depth > 0:
        succ = successors(state)
        for i in range(len(succ)):
            makeGoodMoveRec([other(succ[i][0]),succ[i][1]], depth - 1, isMax, origPlayer)
    if isMax:
        return staticvalue[0]
    else:
        return staticvalue[1]
'''
Static value Searches for all paths of size ksize
in the rows, columns, and both diagnals
1000 means 1 away from winning
100 means 2 away from winning
10 means add to exsiting spot
1 place
-1000 means about to lose
-100 meanse 2 away from losing
-10 blocking a single or pair
'''
def staticValue(state):
    max = 0
    min = 0
    maxPos = []
    minPos = []
    ##search rows
    for r in range(len(state[1])):
        for c in range(len(state[1][r])-ksize+1):
            temp = evalKsize(state[0],state[1][r][c:c+ksize])
            if temp > max:
                max = temp
                maxPos = []
                for i in range(len(state[1][r][c:c+ksize])):
                    maxPos += [[r,c+i]]
            if temp < min:
                min = temp
                minPos = []
                for i in range(len(state[1][r][c:c+ksize])):
                    minPos += [[r,c+i]]
    ##search columns
    for r in range(len(state[1])-ksize+1):
        for c in range(len(state[1][r])):
            pos = []
            values = []
            for i in range(ksize):
                pos +=[[r+i,c]]
            for i in range(len(pos)):
                values += state[1][pos[i][0]][pos[i][1]]
            temp = evalKsize(state[0],values)
            if temp > max:
                max = temp
                maxPos = pos
            if temp < min:
                min = temp
                minPos = pos
    ##search topright to bottom left diagnals
    for r in range(len(state[1])-ksize+1):
        for c in range(len(state[1][r])-ksize+1):
            pos = []
            values = []
            for i in range(ksize):
                pos += [[r+i,ksize+c-i-1]]
            for i in range(len(pos)):
                values += state[1][pos[i][0]][pos[i][1]]
            temp = evalKsize(state[0],values)
            if temp > max:
                max = temp
                maxPos = pos
            if temp < min:
                min = temp
                minPos = pos
    ##search top left to bottom right diagnals
    for r in range(len(state[1])-ksize+1):
        for c in range(len(state[1][r])-ksize+1):
            pos = []
            values = []
            for i in range(ksize):
                pos += [[r+i,c+i]]
            for i in range(len(pos)):
                values += state[1][pos[i][0]][pos[i][1]]
            temp = evalKsize(state[0],values)
            if temp > max:
                max = temp
                maxPos = pos
            if temp < min:
                min = temp
                minPos = pos
    return [max,min,maxPos,minPos]

## assume i am X
def evalKsize(player, array):
    xFound = False
    oFound = False
    bFound = False
    bFound2 = False
    bFound3 = False
    value = 0
    isX = 1
    if player == 'O':
        isX = -1
    for r in range(len(array)):
        if array[r] == 'X':
            xFound = True
        elif array[r] == 'O':
            oFound = True
        elif array[r] == '-':
            return 0
        elif array[r] == ' ':
            if bFound2:
                bFound3 = True
            elif bFound:
                bFound2 = True
            else:
                bFound = True
    if xFound == False and oFound == False and bFound == True:
        return isX * 1
    if xFound == True and oFound == True:
        return 0
    if ksize  == 2:
        if xFound == True and bFound == True:
            value = isX * 1000
        elif oFound ==  True and bFound == True:
            value = isX * -1000
    else:
        if xFound == True and bFound3 == True:
            return isX * 10
        elif xFound == True and bFound2 ==True:
            return isX * 100
        elif xFound == True and bFound == True:
            return isX * 1000
        elif oFound == True and bFound3 == True:
            return isX * -10
        elif oFound == True and bFound2 == True:
            return isX * -100
        elif oFound == True and bFound == True:
            return isX * -1000
    return value
    
    
    

def printBoard(board):    
    for row in board:
        print row
        
def other(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'
def sayings(score):
    if score == 1000:
        return 'kthxbai ^_^'
    elif score == -1000:
        return 'You just got lucky. Its no big'
    elif score == 100:
        return 'Bout to win. Going for the last beer pong cup'
    elif score == -100:
        return 'Denied just like your physics midterm'
    else:
        return random.choice(
            ['i lol at your fail',
            'Your kung foo is not strong enough',
            'Your about as hard to see though as glass',
            'Your about as skilled as a wasu noob',
            'U iz a freshman',
            'Your skills are questionable',
            'Husky Football is the greatest team EVER',
            'You + game = fail',
            'Just wait till beer pong, cuss then its ON LIKE DONKY KONG',
            'Bring it!',
            'Your doing it wrong',
            'Im from tech support your code haz bug',
            'i iz a Hax0r',
            'Your bouts to get pwnd',
            'LOLz'])

#Najib Morcos
#CSE 415 HW 3

k = 0
mRows = 0
nColumns = 0
maxMs = 0
PlayX = False
debugging = False
##Prepares following functions to be used by calling game
##Returns ok if maxMs is over 50 and a playable k and board is passed
def prepare(ks, m, n, maxMilli, PlayingX, debug):
    global k
    global mRows
    global nColumns
    global maxMs
    global PlayX
    global debugging
    k = ks
    mRows = m
    nColumns = n
    maxMs = maxMilli/1000
    PlayX = PlayingX
    debugging = debug
    myMax = (mRows*mRows + nColumns*nColumns)*3
    if maxMs < 200:
        return "I need at least " + str(myMax) + " milliseconds"
    elif mRows < 2 or nColumns < 2 or k < 2:
        return "We either have no board or k doesn't make sense"
    else:
        return "ok"

def introduce():
    return "K IN A ROW Player \n\
            Najib Morcos\n\
            Scarface"
def nickname():
    return "Montana"

def other(player):
   if player=='X': return 'O'
   else: return 'X'

##returns a list of possible successors for the state passed
def successors(state):
    import copy
    myPiece = state[0]
    board = state[1]
    possibleStates = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ' ':
                temp = copy.deepcopy(board)
                temp[i][j] = myPiece
                b = [' ', ' ']
                b[0] = other(myPiece)
                b[1] = temp
                possibleStates += [b]
    return possibleStates

##a simple move function that returns the next available state
def makeMove(state):
    myPiece = state[0]
    board = state[1]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ' ':
                board[i][j] = myPiece
                newState = [other(mySide), board]
                utterance = "This move is as good as any"
                return [newState, utterance]

'''
Calculates the static value for the state passed
For every row,column and diagonal the function counts the number of
Xs and Os in k segments.  For each k segment that only contains one or the other
it calculates a total bassed on 10 to the power number of of only Xs - 1
This function works similar to the function given from class for a standard tic-tac-toe
board but is made generic for any k game
'''
def staticValue(state):
    global k
    myPiece = state[0]
    board = state[1]
    rows = len(board)
    columns = len(board[0])
    TX = 0
    TO = 0
    Fx = False
    Fo = False
    
#rows
    for L in range(rows):
        for i in range(columns):
            F = False
            xs = 0
            os = 0
            for j in range(k):
                if i + j < columns:
                    if board[L][i+j] == '-':
                        F = True
                        break
                    elif board[L][i+j] == 'X':
                        xs += 1
                    elif board[L][i+j] == 'O':
                        os += 1
                else:
                    F = True
            if F == False:
                if xs > 0 and os == 0:
                    TX += 10**(xs-1)
                    Fx = Fx or (xs == k)
                if os > 0 and xs == 0:
                    TO += 10**(os-1)
                    Fo = Fo or (os == k)
   
#col
    for L in range(columns):
        for i in range(rows):
            F = False
            xs = 0
            os = 0
            for j in range(k):
                if i + j < rows:
                    if board[i+j][L] == '-':
                        F = True
                        break
                    elif board[i+j][L] == 'X':
                        xs += 1
                    elif board[i+j][L] == 'O':
                        os += 1
                else:
                    F = True
            if F == False:
                if xs > 0 and os == 0:
                    TX += 10**(xs-1)
                    Fx = Fx or (xs == k)
                if os > 0 and xs == 0:
                    TO += 10**(os-1)
                    Fo = Fo or (os == k)  
 
#upper left down right
    for L in range(rows):
        for i in range(L):
            F = False
            xs = 0
            os = 0
            for j in range(k):
                if L -i- j >= 0 and i + j < columns:
                    if board[L-i-j][i+j] == '-':
                        F = True
                        break
                    elif board[L-i-j][i+j] == 'X':
                        xs += 1
                    elif board[L-i-j][i+j] == 'O':
                        os += 1
                else:
                    F = True
            if F == False:
                if xs > 0 and os == 0:
                    TX += 10**(xs-1)
                    Fx = Fx or (xs == k)
                if os > 0 and xs == 0:
                    TO += 10**(os-1)
                    Fo = Fo or (os == k)  
#second half of first diag
    for i in range(1, columns):
        m = i-1
        for L in range(rows-1, -1,-1):
            m += 1
            F = False
            xs = 0
            os = 0
            for j in range(k):
                if L - j >= 0 and m + j < columns:
                    if board[L-j][m+j] == '-':
                        F = True
                        break
                    elif board[L-j][m+j] == 'X':
                        xs += 1
                    elif board[L-j][m+j] == 'O':
                        os += 1
                else:
                    F = True
            if F == False:
                if xs > 0 and os == 0:
                    TX += 10**(xs-1)
                    Fx = Fx or (xs == k)
                if os > 0 and xs == 0:
                    TO += 10**(os-1)
                    Fo = Fo or (os == k)  

#upper right down left

    for L in range(rows,-1,-1):
        for i in range(rows):
            F = False
            xs = 0
            os = 0
            for j in range(k):
                if L+i+j < rows and i + j < columns:
                    if board[L+i+j][i+j] == '-':
                        F = True
                        break
                    elif board[L+i+j][i+j] == 'X':
                        xs += 1
                    elif board[L+i+j][i+j] == 'O':
                        os += 1
                else:
                    F = True
            if F == False:
                if xs > 0 and os == 0:
                    TX += 10**(xs-1)
                    Fx = Fx or (xs == k)
                if os > 0 and xs == 0:
                    TO += 10**(os-1)
                    Fo = Fo or (os == k)  
  

#second half of second diag
    for i in range(1, columns):
        for L in range(rows):
            F = False
            xs = 0
            os = 0
            for j in range(k):
                if L + j < rows and L + i + j < columns:
                    if board[L+j][L+i+j] == '-':
                        F = True
                        break
                    elif board[L+j][L+i+j] == 'X':
                        xs += 1
                    elif board[L+j][L+i+j] == 'O':
                        os += 1
                else:
                    F = True
            if F == False:
                if xs > 0 and os == 0:
                    TX += 10**(xs-1)
                    Fx = Fx or (xs == k)
                if os > 0 and xs == 0:
                    TO += 10**(os-1)
                    Fo = Fo or (os == k)  


    #print TX
    #print TO
    return [TX-TO,Fx,Fo]
timeStart = 0
'''
returns the best possible move for the given state
Uses one level of successors to calculate the val of each successor
If there is a lot of time remaining function recalculates val using a minimax
two level method
'''
sayNum = -1
def makeGoodMove(state):
    import time
    global timeStart
    global maxMs
    global PlayX
    global mRows
    global nColumns
    global debugging
    timeStart = time.time()
    best = minimax(state,0,1)
    if best[1] == 11.5:   #not enough time
        return [state, "not enough time to make a move"]
    import time
    a = time.time() - timeStart
    if (best[1] == 10.5):
        if debugging: print "cut off occurs found win"
    elif a*mRows*nColumns/4 < (maxMs - a):
            best2 = minimax(state,1,1)
            if best2[1] != 11.5 and best[0] != None:  ##RECENT CHANGE
                best = best2
    val = best[1]
    global sayNum
    sayings = ["I'm Tony Montana! You mess with me, you messin' with the best! " , " You know what? forget you! How about that? ",
           "I always tell the truth. Even when I lie.", "Lesson number one: Don't underestimate the other guy's greed! ",
           "Every day above ground is a good day. ", "You wanna mess with me? Okay. You wanna play rough? Okay. Say hello to my little friend!",
           "Who put this thing together? Me, that's who! Who do I trust? Me! ", "What the hell is wrong with this guy, man? He kidding me or what? ",
           "Me, I want what's coming to me. ", "Where'd you get the beauty scar, tough guy?",
           "I only tell you once. Don't mess me, Tony. Don't you ever try to mess me. ", "Who did you kill for this? ",
           "Here pelican, pelican, pelican... ", "You think you can take me? You need an army if you gonna take me! ",
           "You wanna waste my time, OK? You wanna play rough? ", "Can't you see what we're becoming? We're losers. We're not winners, we're losers."]
    if sayNum >= len(sayings)-1:
        sayNum = -1
    sayNum += 1
    return [best[0], sayings[sayNum]]

##Helper function implements minimaxing to return either the max or min value when given a state
##The value and function depends on the depth it is given
def minimax(state,depth,first):
    global PlayX
    global timeStart
    global maxMs
    import time
    if (PlayX and state[0] == 'X') or (not(PlayX) and state[0] == 'X'):
        best = [None,-100000]
    else:
        best = [None,100000]
    import time
    if time.time() - timeStart >= maxMs:
        return [None, 11.5]  #11.5 means time out use old best
    Lst = successors(state)
    for n in range(len(Lst)):
        import time
        if time.time() - timeStart >= maxMs:
            return [None, 11.5]  #11.5 means time out use old best
        if depth == 0:
            temp = staticValue(Lst[n])
            val = temp[0]
            if PlayX and temp[1] and first == 1:
                return [Lst[n],10.5]
            if not(PlayX) and temp[2] and first == 1:
                return [Lst[n],10.5]
        else:
            step = minimax(Lst[n],depth-1,2)
            val = step[1]
            if val == 11.5:
                return [None, 11.5]  #11.5 means time out use old best
            if val == 10.5 and first == 1:
                return [Lst[n],10.5]
        if PlayX and Lst[n][0] == 'O' and val >= best[1]:
            best = [Lst[n],val]
        elif PlayX and Lst[n][0] == 'X' and val <= best[1]:
            best = [Lst[n],val]
        if not(PlayX) and Lst[n][0] == 'X' and val <= best[1]:
            best = [Lst[n],val]
        elif not(PlayX) and Lst[n][0] == 'O' and val >= best[1]:
            best = [Lst[n],val]
    return best

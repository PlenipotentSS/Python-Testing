import copy
import time

def introduce():
    output = "When I was growing up, my family was so poor we couldn`t afford to pay attention!"
    output += "I'm a little program made by Steven Stevenson, but pitty that fool!"
    output += "I believe in the Golden Rule - The Man with the Gold.. rules."
    output += "Quit yo Jibber-jabber! Let's Play!"
    return output

def nickname():
    return "Mr. T"

def other(mySide):
    if mySide == 'X':
        return 'O'
    else:
        return 'X'

def prepare(k, mRows, nColumns, maxMillisecPerMove, isPlayingX, debugging):
    if k > mRows and k > nColumns:
        output = "I can't be beat, I won't be beat "
        output += str(k) + " in a row on a " + str(mRows) + " by " + str(nColumns) + " board! FOOL!"
        return output
    elif maxMillisecPerMove < 20:
        output = "Geez, " + str(maxMillisecPerMove) + " milliseconds! I pitty the fool who drinks soy milk!"
        return output
    else:
        global K
        K = k
        global ROWS
        ROWS = mRows
        global COLS
        COLS = nColumns
        global maxTime
        maxTime = maxMillisecPerMove *.001
        global side
        if isPlayingX:
            side = "X"
        else:
            side = 'O'
        global pState
        board = []
        for r in range(ROWS):
            columns = []
            for c in range(COLS):
                columns.append(' ')
            board.append(columns)
        pState = [side,board]
        global debug
        if debugging:
            debug = True
        else:
            debug = False
        global numMoves
        numMoves = 0
        global win
        win = False
        return "OK"

def successors(state):
    board = state[1]
    sList = []
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == ' ':
                temp = copy.deepcopy(board)
                temp[r][c] = state[0]
                newState = [ other(state[0]), temp]
                sList += [newState]
    return sList

def makeMove(state):
    global numMoves
    numMoves += 1
    mySide = state[0]
    newBoard = copy.deepcopy(state[1])
    global ROWS
    global COLS
    for r in range(ROWS):
        for c in range(COLS):
            if newBoard[r][c] == ' ':
                newBoard[0][0] = mySide
                utterance = "What did you say to me paper champion? "
                newState = [other(mySide), newBoard]
                global pState
                pState = bestState
                return [newState, utterance]
    

def makeGoodMove(state):
    global numMoves
    numMoves += 1
    startc = time.time()
    bestScore, bestState = minimax(state[0], state, 3, -1000000, 10000000, startc)
    global pState
    pState = bestState
    utterance = "I pitty the fool! "
    if bestScore < 50:
        utterance = "I'm almost finished... just wait, I'm gonna bust you up!"
    elif bestScore < 1000:
        utterance = "Pain..."
    elif bestScore < 5000:
        utterance = "Do you know me? Of course you do. 'Cause I'm famous!"
    elif bestScore < 10000:
        utterance = "Quit yo Jibber-jabber! yo pathetic!"
    elif bestScore > 10000:
        utterance = "You're washed up, finished! I'm the baddest in the world!"
    return [bestState, utterance]

def minimax(origSide, state, depth, min, max, timer):
    global maxTime
    if depth == 0:
        return [staticEval(state),state]
    if state[0] == origSide:
        x = min
        newState = state
        sList = successors(state)
        for poss in range(len(sList)):
            thisEval, stateEval = minimax(origSide,sList[(len(sList) - poss - 1)], depth-1, x, max, timer)
            if thisEval > x:
                x = thisEval
                newState = sList[(len(sList) - poss - 1)]
            if x > max:
                global debug
                global numMoves
                if debug:
                    print "In Move " + str(numMoves) + " of the game, it is " + origSide + \
                                      "'s turn, and an alpha cutoff occurs at Ply " + str(3-depth) + \
                                      " out of 3 because provisional value is " + str(x) +  \
                                      " and the other is " + str(max) +"."
                return [max, newState]
            if time.time() - timer > maxTime - 10*.001:
                break
        return [x, newState]
    if state[0] == other(origSide):
        x = max
        newState = state
        sList = successors(state)
        for poss in range(len(sList)):
            thisEval, stateEval = minimax(origSide, sList[poss], depth-1, min, x, timer)
            if thisEval < x:
                x = thisEval
                newState = sList[poss]
            if x < min:
                global debug
                global numMoves
                if debug:
                    print "In Move " + str(numMoves) + " of the game, it is " + origSide + \
                                      "'s turn, and an beta cutoff occurs at Ply " + str(3-depth) + \
                                      " out of 3 because provisional value is " + str(x) + \
                                      " and the other is " + str(min) +"."
                return [min, newState]
            if time.time() - timer > maxTime - 20*.001:
                break
        return [x, newState]
    
## Collects a list of all possible winnings
## Evaluates the state by having a score connected to each option:
## 15000(W) + 5000(almost sure win) + 5000(almost win)
##                    + 1000(2 away from win) + 10*(num of entries w/o other entry)
## - ( 15000(L) + 5000(almost sure Loss) + 5000(almost loss)
##                    + 1000(2 away from loss) + 10*(num of  other entries w/o your entry))
def staticEval(state):
    mySide = other(side)
    board = state[1]
    global K
    ROWS = len(board)
    COLS = len(board[0])
    cList = []
    rList = []
    dList = []
    d2List = []
    for r in range(ROWS):
        for c in range(COLS):
            if r+K < ROWS + 1:
                temp = []
                for j in range(r,K+r):
                    temp += [board[j][c]]
                cList += [temp]
            if c+K < COLS + 1:
                temp = []
                for j in range(c,K+c):
                    temp += [board[r][j]]
                rList += [temp]
            if c+K < COLS + 1 and r+K < ROWS + 1:
                d1 = []
                dr = r
                dc = c
                for i in range(K):
                    d1 += [board[dr][dc]]
                    dr += 1
                    dc += 1
                dList += [d1]
            if c-(K-1) > -1 and r+K < ROWS + 1:
                d2 = []
                dr = r
                dc = c
                for i in range(K):
                    d2 += [board[dr][dc]]
                    dr += 1
                    dc -= 1
                d2List += [d2]
    runningTotal = 0
    runningTotal += tabulateScore(cList, mySide)
    runningTotal += tabulateScore(rList, mySide)
    runningTotal += tabulateScore(dList, mySide)
    runningTotal += tabulateScore(d2List, mySide)
    return runningTotal

def tabulateScore(thisList, mySide):
    global K
    score = 0
    for i in range(len(thisList)):
        count = thisList[i].count(mySide)
        otherCount = thisList[i].count(other(mySide))
        nullCount = thisList[i].count('-')
        if nullCount != 0:
            count = 0
        else:
            ##COUNTS
            if count == K:
                score += 150000
            if count == K-1 and otherCount == 0 and \
                     thisList[i][0] == ' ' or thisList[i][K-1] == ' ':
                score += 5000
            if count == K-1 and otherCount == 0:
                score += 5000
            if count == K-2 and \
                     thisList[i][0] == thisList[i][K-1] == ' ':
                score += 1000
            if count == K-2 and otherCount == 0:
                score += 300
            if count > 0 and otherCount == 0:
                score += 10*count
            ##OTHER COUNTS
            if otherCount == K:
                score -= 15000
            if otherCount == K-1 and count == 0:
                score -= 5000
            if otherCount == K-1 and count == 0 and \
                     thisList[i][0] == ' ' or thisList[i][K-1] == ' ':
                score -= 5000
            if otherCount == K-1 and count == 0:
                score -= 2000
            elif otherCount == K-2 and \
                     thisList[i][0] == thisList[i][K-1] == ' ':
                score -= 1000
            if otherCount == K-2 and count == 0:
                score -= 300
            if otherCount > 0 and count == 0:
                score -= 10*count
    return score
        
        

import copy
import time
import random

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
        numMoves = 0
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
        global oldUtterance
        oldUtterance = []
        global debugUtter
        debugUtter = ""
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
            if newBoard[ROWS - 1 -r][COLS - 1 -c] == ' ':
                newBoard[0][0] = mySide
                utterance = "What did you say to me paper champion? "
                newState = [other(mySide), newBoard]
                global pState
                pState = bestState
                return [newState, utterance]

def makeGoodMove(state):
    global side
    startc = time.time()
    [bestScore, bestState] = minimax(state[0], state, 4, -90000000, 900000000, startc)
    global pState
    pState = bestState
    getUtterance = False
    utterance = ""
    while not getUtterance:
        if debug:
            break
        else:
            global oldUtterance
            if bestScore < 50:
                uList = ["You... Naked?",
                             "You make me Angry",
                             "Dun Mess with Me!",
                             "I pitty the fool! ",
                             "Suckka!",
                             "If you put down one motha, you put down motha's around the world.",
                             "Don't mess with my motha!",
                             "" + other(side) + "'s are for sissies!",
                             "Wanna hurtz donut?",
                             "I'll give you a birthday present...",
                             "clean my gold with the special cleaner!",
                             "If you think I'm big, you should meet my brothers!",
                             "Go eat a fish!",
                             "Pain...",
                             "Snickers! ",
                             "Hey You with the teeth...",
                             "Wake Up, Fool!",
                             "WHAT!? Fool! come back here!",
                             "Want a bike? Let me get my tank! PAIN!",
                             "Take that toe dipper!",
                             "I'm going to keep my eye on you.",
                             "I pitty the fool that plays you!",]
                utterance = random.choice(uList)
            elif bestScore < 5000:
                uList = ["It takes a smart guy to play dumb.",
                             "You sure you wanna go there punk!?",
                             "That's it you're going in the water!",
                             "Take that speedwalker!",
                             "Fool!!",
                             "You're half a glass short of a woopass!",
                             "You're a disgrace to the man race",
                             "What's that again? Trouble, with a capital T",
                             "Smart guy to play dumb against me fool!.",
                             "Don't let me catch you cryin'",
                             "FOOL!",
                             "I'll play easy on you, ha Sucka!",
                             "I'm gonna kill that crazy Murdock!!",
                             "" + other(side) + "'s are fools!",
                             "Quit yo Jibberjabber!",
                             "AAAARRRRHHHHH",
                             "Trouble, with a capital T",
                             "Smart guy to play dumb against me fool!.",
                             "Don't let me catch you cryin'",
                             "What? What do you mean four sucka?"
                             "Who you jokin', sucka! I'm gonna smahs you!",
                             "Hungry for some " + other(side) + "?",
                             "Get some nuts!"]
                utterance = random.choice(uList)
            elif bestScore > 5000:
                uList = ["I'm the baddest in the world!",
                             "I win you lose, suckka!",
                             "I win, want a cookie?",
                             "Time to fly!"]
                oldUtterance = []
                utterance = random.choice(uList)
        if len(oldUtterance) >= 20:
            lastUtterance = oldUtterance.pop()
            oldUtterance.append(lastUtterance)
            if len(lastUtterance) > 30 and len(utterance) < 30 and lastUtterance != utterance:
                oldUtterance = []
                oldUtterance.append(utterance)
                break
            elif len(lastUtterance) < 30:
                oldUtterance = []
                oldUtterance.append(utterance)
                break
        elif len(oldUtterance) > 0:
            lastUtterance = oldUtterance.pop()
            oldUtterance.append(utterance)
            if len(lastUtterance) < 30 and oldUtterance.count(utterance) == 0:
                oldUtterance.append(utterance)
                break
            elif len(lastUtterance) > 30 and len(utterance) < 30 and lastUtterance != utterance:
                oldUtterance.append(utterance)
                break
        else:
            oldUtterance.append(utterance)
            break
    if debug:
        numMoves = 0
        for i in range(len(bestState[1])):
            numMoves += bestState[1][i].count('X')
            numMoves += bestState[1][i].count('O')
        global debugUtter
        utterance = "In Move " + str(numMoves) + debugUtter
    return [bestState, utterance]

def minimax(origSide, state, depth, min, max, timer):
    global debug
    global numMoves
    global debugUtter
    global maxTime
    if time.time() - timer > maxTime - K*100*.001:
        return [staticEval(state), state]
    sList = successors(state)
    if depth == 0 or len(sList) == 0:
        return [staticEval(state), state]
    if state[0] == origSide:
        x = min
        newState = state
        for poss in range(len(sList)):
            thisResult = minimax(origSide, sList[poss], depth-1, x, max, timer)
            thisEval = thisResult[0]
##            print thisEval
##            for j in range(len(sList[poss][1])):
##                print sList[poss][1][j]
            if thisEval > x:
                x = thisEval
                newState = sList[poss]
            if x > max:
                if debug:
                    debugUtter = " of the game, it is " + origSide + \
                                      "'s turn, and an alpha cutoff occurs at Ply " + str(1-depth) + \
                                      " out of 3 because provisional value is " + str(x) + \
                                      " and the other player could get: " + str(max) +"."

                return [max, newState]
        return [x, newState]
    else:
        y = max
        newState = state
        for poss in range(len(sList)):
            thisResult = minimax(origSide, sList[poss], depth-1, min, y, timer)
            thisEval = thisResult[0]
##            print thisEval
##            for j in range(len(sList[poss][1])):
##                print sList[poss][1][j]
            if thisEval < y:
                y = thisEval
                newState = sList[poss]
            if y < min:
                if debug:
                    debugUtter = " of the game, it is " + origSide + \
                                      "'s turn, and an beta cutoff occurs at Ply " + str(1-depth) + \
                                      " out of 3 because provisional value is " + str(y) + \
                                      " and the other player could get: " + str(min) +"."

                return [min, newState]
        return [y, newState]        
    
## Collects a list of all possible winnings
## Evaluates the state by having a score connected to each option:
def staticEval(state):
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
    runningTotal += tabulateScore(cList)
    runningTotal += tabulateScore(rList)
    runningTotal += tabulateScore(dList)
    runningTotal += tabulateScore(d2List)
    return runningTotal

def tabulateScore(thisList):
    global side
    mySide = side
    global K
    score = 0
    otherSide = other(mySide)
    for i in range(len(thisList)):
        count = thisList[i].count(mySide)
        otherCount = thisList[i].count(otherSide)
        if thisList[i].count('-') == 0:
            if count > 0:
                ##print thisList[i]
                firstSide = thisList[i].index(mySide)
                if count == K:
                    score += 10000
                if count == K-1 and otherCount == 0:
                    score += 600
                if count == K-2  and otherCount == 0:
                    score += 180
                if otherCount == K-2 and count == 1:
                    score += 80
                if otherCount == K-1 and count == 1:
                    score +=70
                if count == 2 and thisList[i][firstSide+1] == mySide and otherCount == 0:
                    score += 10
                if otherCount == 0:
                    score += 4
                score += 1
            if otherCount > 0:
                firstSide = thisList[i].index(otherSide)
                if otherCount == K:
                    score -= 1000
                if otherCount == K-1 and count == 0:
                    score -= 1000
                if otherCount == K-2 and count == 0:
                    score -= 300
                if count == K-2 and otherCount == 1:
                    score -= 80
                if count == K-1 and otherCount == 1:
                    score -= 70
                if otherCount == 2 and thisList[i][firstSide+1] == otherSide and count == 0:
                    score -= 10
                if count == 0:
                    score -= 4
                score -= 1
    return score
        
        

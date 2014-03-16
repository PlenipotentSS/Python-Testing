'''ss377KINAROW.py

This module contains a player for K-in-a-row. It's personality is Mr T.
It takes a given game stage and computes moves, and comments accordingly.


'''

import copy
import time
import random


##
## Returns Introduction of the personality of this Player
##
def introduce():
    output = "When I was growing up, my family was so poor we couldn`t afford to pay attention!"
    output += "I'm a little program made by Steven Stevenson, but pitty that fool!"
    output += "I believe in the Golden Rule - The Man with the Gold.. rules."
    output += "Quit yo Jibber-jabber! Let's Play!"
    return output

##
## Returns Personalities nickname
##
def nickname():
    return "Mr. T"

##
## returns the other player's symbol
##
def other(mySide):
    if mySide == 'X':
        return 'O'
    else:
        return 'X'

##
## Prepares the the global variables, with the passed variables.
##      if maxMillisecPerMove < 20, then the game cannot be played
##      if the dimensions of the board is not proper, the game cannot be played
## return OK if game is ready to be played
##
def prepare(k, mRows, nColumns, maxMillisecPerMove, isPlayingX, debugging):
    if k > mRows and k > nColumns:
        output = "I can't be beat, I won't be beat "
        output += str(k) + " in a row on a " + str(mRows) + " by " + str(nColumns) + " board! FOOL!"
        return output
    elif maxMillisecPerMove < 20:
        output = "Geez, " + str(maxMillisecPerMove) + " milliseconds! I pitty the fool who drinks soy milk!"
        return output
    else:
        global K, ROWS, COLS, side, debug, maxTime,debug, oldUtterance, largeUtter
        K = k
        numMoves = 0
        ROWS = mRows
        COLS = nColumns
        maxTime = maxMillisecPerMove *.001
        if isPlayingX:
            side = "X"
        else:
            side = 'O'
        if debugging:
            debug = True
        else:
            debug = False
        oldUtterance = []
        largeUtter = []
        global debugUtter
        debugUtter = ""
        return "OK"

##
## returns a list of all possible moves for this player given a game state
##
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

##
## returns a 'dumb' move for this player
##
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

##
## returns the best move for this player and an appropriate utterance
##      best move is defined by the static eval function, and the use of
##      a minimax search with alphabeta pruning
##
def makeGoodMove(state):
    global side
    startc = time.time()
    [bestScore, bestState] = minimax(state[0], state, 4, -90000000, 900000000, startc)
    global pState
    pState = bestState
    getUtterance = False
    utterance = ""
    global oldUtterance, largeUtter
    numUtt = 0
    while not getUtterance:
        if debug:
            break
        else:
            if bestScore < 5000:
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
                             "Fool! come back here!",
                             "Less Jib, more Jab!",
                             "Want a bike? Let me get my tank! PAIN!",
                             "Take that toe dipper!",
                             "I'm going to keep my eye on you.",
                             "pitty!",
                             "It takes a smart guy to play dumb.",
                             "Sure you wanna go there punk!?",
                             "That's it you're going in the water!",
                             "Take that speedwalker!",
                             "Fool!!",
                             "Just half a glass short of some woopass!",
                             "You're a disgrace to the man race",
                             "Always smart to play dumb!.",
                             "Don't let me catch you cryin'",
                             "FOOL!",
                             "I'll play easy on you, ha Sucka!",
                             "Crazy Murdock!!",
                             "" + other(side) + "'s are fools!",
                             "Quit yo Jibberjabber!",
                             "AAAARRRRHHHHH",
                             "Trouble, with a capital T",
                             "Don't let me catch you cryin'",
                             "What do you mean four sucka?"
                             "Who you jokin'",
                             "sucka! I'm gonna smash you!",
                             "Hungry for some " + other(side) + "?",
                             "Get some nuts!",
                             "I'm educated in pain!"]
                utterance = random.choice(uList)
            elif bestScore > 5000:
                uList = ["I'm the baddest in the world!",
                             "I win you lose, suckka!",
                             "I win, want a cookie?",
                             "Time to fly!"]
                oldUtterance = []
                utterance = random.choice(uList)
        if len(oldUtterance) >= 45:
            lastUtterance = oldUtterance.pop()
            oldUtterance.append(lastUtterance)
            if len(utterance) > 30 and largeUtter.count(utterance) == 0 and len(lastUtterance) < 30:
                largeUtter.append(utterance)
                oldUtterance = []
                oldUtterance.append(utterance)
                break
            elif len(utterance) < 30 and oldUtterance.count(utterance) == 0:
                oldUtterance = []
                oldUtterance.append(utterance)
                break
        elif len(oldUtterance) > 0:
            lastUtterance = oldUtterance.pop()
            oldUtterance.append(lastUtterance)
            if len(utterance) > 30 and largeUtter.count(utterance) == 0 and len(lastUtterance) < 30:
                largeUtter.append(utterance)
                oldUtterance.append(utterance)
                break
            elif len(utterance) < 30 and oldUtterance.count(utterance) == 0:
                oldUtterance.append(utterance)
                break
        elif len(oldUtterance) == 0:
            if len(utterance) > 30:
                largeUtter.append(utterance)
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

##
## Recursively looks at different Plys of the game state to determine
## the highest scoring move throughout all the successors (given allotted time)
##
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
## returns an appropriate value for this current state
##          (value is determined by tabulateScore())
##
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

##
## Tabulate score is the value processor for staticEval():
## It's function to determine the score is as follows:
##      where K = num of this players entries for win
##          and K-1 = num entries where 1 move away from win
##          and i:K = i num of this players
##      where O = num of other players entries for win
##          and i:O i num of other players
##  10000K + 600(K-1) + 180(K-2) + 80(K-2 ^ i:O) + 70(K-1 ^ 1:O) + 10(2:K ^ 0:O) + 4(0:O) + 1(1:K)
##  - [ 1000O + 1000(O-1 ^ 0:K) + 70(O-1 ^ 1:O) + 300(O-2 ^ O:K) + 80(O-2 ^ 1:K) + 10(2:O ^ 0:K) + 4(0:K) + 1(1:O)
##
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
                if count == K-1 and otherCount == 1:
                    score -= 70
                if otherCount == K-2 and count == 0:
                    score -= 300
                if count == K-2 and otherCount == 1:
                    score -= 80
                if otherCount == 2 and thisList[i][firstSide+1] == otherSide and count == 0:
                    score -= 10
                if count == 0:
                    score -= 4
                score -= 1
    return score
        
        

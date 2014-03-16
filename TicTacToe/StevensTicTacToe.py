'''StevenTicTacToe.py
Assignment 2
'''

def myNameIs():
   return "Steven's great Tic-Tac-Toe player"

def myCreatorIs():
   return "Steven Amazing-ness"

def makeMove(currentState):
   global utterance
   for i in range(3):
       if currentState[1][i].count(' ') != 0:
          break
   else:
       print "X and O tied!"
       return -1
   anyWin = anyWinForSide(currentState, True)
   if anyWin != False:
      return -1
   else:
      utterance = "Will this work for " + currentState[0]
   newState = bestMove(currentState)
   anyWin = anyWinForSide(newState, True)
   if anyWin != False:
      utterance = "I won!"
   return newState

def other(player):
   if player=='X': return 'O'
   else: return 'X'

def myUtterance():
   global utterance
   return utterance

def staticEvalBoard(mySide, board, state):
    score = -1
    y = 0
    x = 0
    result = state
    if board.count(' ') == 9:
       result[1][1] = mySide
       return result
    else:
       r1 = board[0:3]
       r2 = board[3:6]
       r3 = board[6:9]
       c1 = [board[0], board[3], board[6]]
       c2 = [board[1], board[4], board[7]]
       c3 = [board[2], board[5], board[8]]
       d1 = [board[0], board[4], board[8]]
       d2 = [board[2], board[4], board[6]]
       lines = [[r1,'r1'],[r2,'r2'],[r3,'r3'],[c1,'c1'],[c2,'c2'],[c3,'c3'],[d1,'d1'],[d2,'d2']]
       for i in range(len(lines)):
          thisLine = lines[i][0]
          if thisLine.count(' ') >= 1:
             if thisLine.count(mySide) == 2:
                newPos = getPos(thisLine, lines[i][1],i)
                y = newPos[0]
                x = newPos[1]
                result[y][x] = mySide
                return result
             if thisLine.count(other(mySide)) == 2:
                newPos = getPos(thisLine, lines[i][1],i)
                y = newPos[0]
                x = newPos[1]
                score = 100
             elif thisLine.count(mySide) == 1 and \
                     thisLine.count(other(mySide)) == 1:
                if score < 10:
                   newPos = getPos(thisLine, lines[i][1],i)
                   if newPos != -1:
                      y = newPos[0]
                      x = newPos[1]
                      score = 0
             else:
                if score < 100:
                   newPos = getPos(thisLine, lines[i][1],i)
                   if newPos != -1:
                      y = newPos[0]
                      x = newPos[1]
                      score = 10
    result[y][x] = mySide
    return result

def getPos(thisLine, line, i):
   if line[0] == 'r':
      newPos = i*3 + thisLine.index(' ')
      y = 0;
      if newPos >= 6:
         y += 2
      elif newPos >=3:
         y += 1
      x = newPos % 3
      return [y,x]
   if line[0] == 'c':
      if thisLine.count(' ') == 0:
         return -1
      else:
         x = int(line[1]) -1
         y = thisLine.index(' ')
         return [y,x]
   if line == 'd1':
      if thisLine.count(' ') == 0:
         return -1
      else:
         x = y = thisLine.index(' ')
         return [y,x]
   if line == 'd2':
      if thisLine.count(' ') == 0:
         return -1
      else:
         y = thisLine.index(' ')
         x = y
         if x == 0:
            x = 2
         elif x == 2:
            x = 0
         return [y,x]
      

def bestMove(currentState):
    mySide = currentState[0]
    board = currentState[1]
    fullBoard = [0,0,0,0,0,0,0,0,0]
    k = 0
    for i in range(3):
        for j in range(3):
           fullBoard[k] = board[i][j]
           k += 1
    newBoard = staticEvalBoard(mySide, fullBoard, board)
    return [other(mySide),newBoard]

def anyWinForSide(state, describe = False):
    global utterance
    mySide = state[0]
    board = state[1]
    d1 = ['','','']
    d2 = ['','','']
    c = [['','',''],['','',''],['','','']]
    for i in range(3):
        r = board[i]
        if len(r) != 3:
            break
        c[0][i] = r[0]
        c[1][1-i] = r[1]
        c[2][2-i] = r[2]
        d1[i] = r[i]
        d2[i] = r[2-i]
        winSide = checkWins(mySide,r)
        if winSide != -1:
            if describe:
               print "There was a win for "+winSide+" on Row " + str(i) 
            return True
    otherLines = [[d1,"Main Diagonal"],[d2,"Secondary Diagonal"], \
                  [c[0],"First Column"],[c[1],"Second Column"], \
                  [c[2],"Third Column"]]
    for i in range(len(otherLines)):
       winSide = checkWins(mySide, otherLines[i][0])
       if winSide != -1:
           if describe:
               print "There was a win for "+winSide+" on the " + otherLines[i][1]
           return True
    else:
        return False

def checkWins(mySide,line):
   if line.count(mySide) == 3:
      return mySide
   elif line.count(other(mySide)) == 3:
      return other(mySide)
   else:
      return -1


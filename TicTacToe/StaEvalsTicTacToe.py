'''MarysTicTacToe.py
test program for harness.

'''
 
def myNameIs():
   return "Mary's awesome Tic-Tac-Toe player"

def myCreatorIs():
   return "Mary Jackson"

def makeMove(currentState):
   global utterance
   mySide = currentState[0]
   board = currentState[1]
   fullBoard = [mySide,' ',' ',' ',' ',' ',' ',' ',' ',' ']
   index = 1
   for i in range(3):
      for j in range(3):
          fullBoard[index] = board[i][j]
          index += 1
   if fullBoard.count(' ') == 0:
      utterance = 'It\'s a Cat\'s Game!'
      return -1
   anyWin = anyWinForSide(currentState, True)
   if anyWin != False:
      return -1
   theMove, bestScore = bestMove( fullBoard )
   row, col = divmod(theMove-1,3)
   board[row][col] = mySide
   utterance = 'I chose the best place, it\'s Static Eval Score was: ' \
               + str(bestScore) + '! It\'s position was: ' + str(theMove) + '!'
   newState = [other(mySide), board]
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

def findFirstMove(currentState):
   mySide = currentState[0]
   global utterance
   utterance = "I give up!"
   return -1

## Static eval: 100A + 10B + C - [100D + 10E + F]
def bestMove(currentState):
   mySide = currentState[0]
   theMove = 1
   possibleLines = [
        [('23','59','47'),('13','58'),('12','57','69')],
        [('17','56'),('19','28','37','46'),('45','39')],
        [('14','53','89'),('79','52'),('78','51','36')]
   ]
   bestScore = 0
   for i in range(1,10):
        indices = divmod(i-1, 3)
        row = indices[0]
        column = indices[1]
        score = 0
        for adj in possibleLines[row][column]:
           adj1 = int(adj[0])
           adj2 = int(adj[1])
           thisLine = [currentState[adj1], currentState[adj2],currentState[i]]
           if thisLine[0] == thisLine[1] == thisLine[2] == mySide:
                score += 100
           if thisLine[0] == thisLine[1] == thisLine[2] == other(mySide):
                score -= 100
           if thisLine.count(mySide) == 2 and thisLine.count(other(mySide)) == 0:
                score += 10
           if thisLine.count(other(mySide)) == 2 and thisLine.count(mySide) == 0:
                score -= 10
           if thisLine.count(mySide) == 1 and thisLine.count(other(mySide)) == 0:
                score += 1
           if thisLine.count(other(mySide)) == 1 and thisLine.count(mySide) == 0:
                score -= 1
        if score >= bestScore and currentState[i] == ' ' and i != 0:
           theMove = i
           bestScore = score
   if currentState.count(' ') == 9:
      theMove = 5
   return [theMove,bestScore]

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



           
               















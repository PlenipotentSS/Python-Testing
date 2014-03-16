'''MarysTicTacToe.py
test program for harness.

'''
 
def myNameIs():
   return "Mary's awesome Tic-Tac-Toe player"

def myCreatorIs():
   return "Mary Jackson"

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
   newState = findFirstMove(currentState)
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
   board = currentState[1]
   for i in range(3):
      for j in range(3):
         if board[2-i][j] == ' ':
            board[2-i][j]=mySide
            return [other(mySide), board]
   global utterance
   utterance = "I give up!"
   return -1

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


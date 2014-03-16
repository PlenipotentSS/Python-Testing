'''UserTicTacToe.py
Assignment 2
'''

def myNameIs():
   return "User's great Tic-Tac-Toe player"

def myCreatorIs():
   return "User Userson"

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
      

def bestMove(currentState):
    mySide = currentState[0]
    board = currentState[1]
    emptyBoard = False;
    for i in range(3):
       if board[i].count(' ') == 0:
          emptyBoard = True
       else:
          break
    else:
       return -1
    fullBoard = [0,0,0,0,0,0,0,0,0]
    k = 0
    for i in range(5):
       print "Where would you like to move?"
       y = raw_input("row: ")
       x = raw_input("column: ")
       if board[int(y) -1][int(x) -1] == ' ':
          board[int(y) -1][int(x) -1] = mySide
          break;
       else:
          print "That's an illegal move, try again..."
    newState = [other(mySide), board]
    return newState

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


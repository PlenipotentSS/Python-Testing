'''TicTacToeAssign2.py'''

initialState = ['X', [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]]
# Here the 'X' means that it is X's turn to move, and the board is empty.

def prettyPrint(state):
    whoseMove = state[0]
    board = state[1]
    print '  1   2   3'
    for i in range(3):
        r = board[i]
        print str(i+1) +' '+r[0]+' | '+r[1]+' | '+r[2]
        if i<2: print ' -----------'
    print 'It is '+whoseMove+"'s turn to move"
    
#prettyPrint(initialState)

player1 = None
player2 = None
def getPlayers(playerModule1, playerModule2):
    try:
        global player1
        player1 = __import__(playerModule1)
        player1OK = True
    except:
        print "Error trying to import "+playerModule1
        print errno
        print strerror
        player1OK = False
    try: 
        global player2
        player2 = __import__(playerModule2)
        player2OK = True
    except:
        print "Error trying to import "+playerModule2
        player2OK = False
    return player1OK and player2OK

def copyState(state):
    newState = [state[0], [state[1][0][:], state[1][1][:], state[1][2][:]]]
    return newState

def holdMatch(player1, player2):
    print "Here is the Tic-Tac-Toe matchup with"
    print player1.myNameIs()+" playing X, and"
    print player2.myNameIs()+" playing O."
    print player1.myNameIs()+" was written by "+player1.myCreatorIs()+", and"
    print player2.myNameIs()+" was written by "+player2.myCreatorIs()+"."

    print "Here's the starting board:"    
    prettyPrint(initialState)
    print 25*'='
    currentState = copyState(initialState)
    for turn in range(5):
        newState = player1.makeMove(currentState)
        # test for legality, for win, and for draw go here.
        if newState==-1:
            break
        prettyPrint(newState)
        print player1.myNameIs()+ "says: "+player1.myUtterance()
        print 25*'='
        currentState = copyState(newState)
        newState = player2.makeMove(currentState)
        if newState==-1:
            break
        # test for legality, for win, and for draw go here.
        prettyPrint(newState)
        print player2.myNameIs()+ "says: "+player2.myUtterance()
        print 25*'='
        currentState = copyState(newState)
    print "Game Over"

finished = False
while not finished:
    print 25* "+"
    print "Welcome to Tic Tac Toe!"
    print "Please select From these players:"
    print "    Mary (computer)"
    print "    Steven (computer)"
    print "    User"
    print "    StaEval"
    inputP1 = raw_input("1st Player Name?:")
    inputP2 = raw_input("2nd Player Name?:")
    player1 = inputP1 + "sTicTacToe"
    player2 = inputP2 + "sTicTacToe"
    readyToPlay = getPlayers(player1, player2)
    if readyToPlay:
      holdMatch(player1, player2)
      s = raw_input("Play Again? (y/n)")
      if s == 'n':
          finished = True
      else:
          print ""
    else:
      print "At least one of the two players has a problem, and so"
      print "we are not ready to hold the match."
      s = raw_input("Try Again? (y/n)")
      if s == 'n':
          finished = True
      else:
          print ""
    print ""
    print "Thanks for Playing! Goodbye!"
  

#prettyPrint(copyState(initialState))
            


#---------


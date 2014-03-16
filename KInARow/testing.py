import ss377KINAROW as player1

sampleState = ['X', [
    ['-',' ',' ',' ','-'],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    ['-',' ',' ',' ','-']]]

print player1.prepare(4, 5, 5, 500, True, False)
print player1.introduce()
player1.pState = sampleState
for i in range(15):
    print " "
    move = player1.makeGoodMove(player1.pState)
    for j in range(player1.ROWS):
         print move[0][1][j]
    print player1.nickname() + ": " +move[1]


##for i in range(len(sampleState[1])):
##    print sampleState[1][i]              
##studentSuccessors = player1.successors(sampleState)
##statEval = player1.staticEval(sampleState)
###print statEval
##sBest = player1.makeGoodMove(sampleState)
###sBestStatEval = player1.staticEval(sBest)
##print sBest[0]
###print sBestStatEval
##for i in range(len(sBest[1][1])):
##    print sBest[1][1][i]

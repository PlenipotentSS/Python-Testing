import ss377KINAROW as player1

sampleState = ['O',[
    ['-',' ',' ',' ','-'],
    ['X','X','X','O',' '],
    [' ','O','X','X',' '],
    [' ','O','O','O','X'],
    ['-',' ',' ',' ','-']

    ]]

player1.prepare(4, 5, 5, 5000, False, False)
##thisStatic = player1.staticEval(sampleState)
##print thisStatic
sList = player1.successors(sampleState)
best = -500000
state = []
for i in range(len(sList)):
    thisStatic = player1.staticEval(sList[i])
    print thisStatic
    for j in range(len(sList[i][1])):
        print sList[i][1][j]
    if thisStatic > best:
        best = thisStatic
        state = sList[i]
print best
for j in range(len(state[1])):
    print state[1][j]

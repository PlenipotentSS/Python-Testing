# -*- coding: utf-8 -*-
import time
import ss377KINAROW as player1
import userinput as player2

player1.prepare(5, 7, 7, 5000, True, False)
player2.prepare(5, 7, 7, 5000, False, True)

##10x10 board:
##['X', [['-',' ',' ',' ',' ',' ',' ',' ',' ','-'],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],['-',' ',' ',' ',' ',' ',' ',' ',' ','-']]]

sampleState = ['X', [
    ['-',' ',' ',' ',' ',' ','-'],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    ['-',' ',' ',' ',' ',' ','-']]]

newBoard = sampleState
p1utterances = []
p1largeUtter = []
repeats = 0
for j in range(32):
    print "==== current Turn: " + newBoard[0]
    startt = time.time()
    newBoard, utterance = player1.makeGoodMove(newBoard)
    endt = time.time()
##    print
    for i in range(len(newBoard[1])):
        print newBoard[1][i]
    print utterance
##    print "that took " + str((endt-startt)) + " seconds"
    if p1largeUtter.count(utterance) != 0:
        repeats += 1
        p1utterances.append("    extra: " +utterance)
    else:
        p1utterances.append(utterance)
        if len(utterance) > 30:
            p1largeUtter.append(utterance)

    print "==== current Turn: " + newBoard[0]
    startt = time.time()
    newBoard, utterance = player2.makeMove(newBoard)
    endt = time.time()
##    print
    for i in range(len(newBoard[1])):
        print newBoard[1][i]
    print utterance
##    print "that took " + str((endt-startt)) + " seconds"

print "================END==================="
for i in range(len(newBoard[1])):
    print newBoard[1][i]
print "There were " + str(repeats) + " Large utterances repeated."
print "The utterances in sequence were:"
for m in range(len(p1utterances)):
    print "  " + p1utterances[m]
oldUtterance = ""
for l in range(len(p1utterances)):
    if len(p1utterances[l]) > 30 and len(oldUtterance) > 30:
        print "--->Problem: " + p1utterances[l]
    oldUtterance = p1utterances[l]
    
averageU = p1utterances[4:]
sum = 0
for n in range(len(averageU)):
    sum += len(averageU[n])
avg = sum / len(averageU)
print "The average count of characters after 4 moves were:" + str(avg)




##sampleState = ['X', [
##    ['-',' ',' ',' ',' ',' ','-'],
##    [' ',' ',' ',' ',' ',' ',' '],
##    [' ',' ',' ','X',' ',' ',' '],
##    [' ',' ',' ',' ',' ',' ',' '],
##    [' ',' ','O',' ',' ',' ',' '],
##    [' ',' ',' ',' ',' ',' ',' '],
##    ['-',' ',' ',' ',' ',' ','-']]]
##
##newBoard, utterance = player1.makeGoodMove(sampleState)
##for i in range(len(newBoard[1])):
##    print newBoard[1][i]

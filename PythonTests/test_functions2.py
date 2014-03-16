# ten_x_plus1(7) -> 71
# ten_x_plus1(1) -> 11
# print ten_x_plus1(121) -> 1211
def ten_x_plus1(x):
    '''Takes the value x and computes (10 * x ) + 1
    '''
    return (10 * x ) + 1

#EVAL FUNCTION FOR EVALUATING A ONE LINE IF_ELSE CONDITION
def if_else(condition, trueVal, falseVal):
    if condition:
        return trueVal
    else:
        return falseVal
    
#HELPER FUNCTION FOR SUBSTITUTION CIPHER
def make_stringCheck(minLet,maxLet, offset):
    return lambda x: if_else( ((x + offset) % maxLet) < minLet, (x + offset) % maxLet + (minLet), (x + offset) % maxLet + 1 ) 

# print substitution_cipher("abc Iz this Secure?",6) -> Vhij Pg aopz Zljbyl?
# print substitution_cipher("Hey you, Jack!",3) -> Lic csy, Nego!
# print substitution_cipher("The answer to the ultimate question is...",10) ->Esp lydhpc ez esp fwetxlep bfpdetzy td...
def substitution_cipher(string, offset):
    '''Uses the substition cipher and substitutes the characters of
    the given stringstring with the character that is offset +1 number away
    Observed Special case: if capital letter, then add 7 away
    '''
    cipher = ''
    for n in range(len(string)):
        thisC = ord(string[n])
        if thisC >= 65 and thisC <= 90:
            findLetRegion = make_stringCheck(65,90, offset)
            newPlace = findLetRegion(thisC)
        elif thisC >= 97 and thisC <= 122:
            findLetRegion = make_stringCheck(97,122, offset)
            newPlace = findLetRegion(thisC)
        else:
            newPlace = (ord(string[n]))
        cipher += chr(newPlace)
    return cipher

# print diff_doubles([2,5,1.5,100,3,8,7]) -> [-3, -98.5, -5, 7]
# print diff_doubles([1]) -> [1]
# print diff_doubles([100,100,1.5,-1.5,50,3,7,20]) -> [0, 3.0, 47, -13]
def diff_doubles(theList):
    '''Takes the difference of values in a list, subtracting the first from
    the second variable. If odd, prints last variable (acts as the last subtracts
    zero)
    '''
    length = len(theList)
    numDoubles = length / 2
    remainder = length % 2 == 1
    newList = []
    for n in range(numDoubles):
        index = n*2
        diff = theList[index] - theList[index+1]
        newList.insert(n,diff)
    if remainder:
        newList.insert(numDoubles, theList[length-1])
    return newList

# print future_tense(['program','debug','execute','crash','repeat']) -> ['will program', 'will debug', 'will execute', 'will crash', 'will repeat']
# print future_tense(['google']) -> ['will google']
# print future_tense(['act','blow-up','integrate','define','return','loop']) -> ['will act', 'will blow-up', 'will integrate', 'will define', 'will return', 'will loop']
def future_tense(theList):
    '''Takes a list of verbs and puts them in future tense, ignoring
    irregular verbs
    '''
    newList = []
    for n in range(len(theList)):
        newList.insert(n,"will " + theList[n])
    return newList

#HELPER FUNCTION FOR FUNCTION past_tense THAT EVALUATES WHETHER THE GIVEN STRING CONTAINS A VOWEL
def find_vowel(string):
    theVowels = ['a','e','i','o','u']
    for n in range(5):
        if theVowels[n] in string:
            return True
    return False

# print past_tense(['program','debug','execute','crash','repeat']) -> ['programmed', 'debugged', 'executed', 'crashed', 'repeated']
# print past_tense(['try']) -> ['tried']
# print past_tense(['eat','read','pick','dance','laugh','find','play','anticipate']) -> ['eated', 'readed', 'picked', 'danced', 'laughed', 'finded', 'played', 'anticipated']
def past_tense(theList):
    '''Takes a list of verbs and puts them into past tense, ignoring
    irregular verbs
    '''
    newList = []
    for n in range(len(theList)):
        thisWord = theList[n]
        lastLetter = thisWord[-1]
        prevLastVowel = find_vowel(thisWord[-2])
        if lastLetter == 'e':
            addSuffix = 'd'
        elif lastLetter == 'y' and not prevLastVowel:
            thisWord = thisWord[0:-1]
            addSuffix = 'ied'
        elif prevLastVowel and not find_vowel(thisWord[-3]) and not find_vowel(lastLetter)  and lastLetter != 'y' and lastLetter != 'w':
            addSuffix = lastLetter + "ed"
        else: 
            addSuffix = 'ed'
        newList.insert(n,thisWord + addSuffix)
    return newList

# print combinations([0,1,2],2) -> [[0, 1], [0, 2], [1, 2]]
# print combinations(range(5),3) -> [[0, 1, 2], [0, 1, 3], [0, 1, 4], [0, 2, 3], [0, 2, 4], [0, 3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
# print combinations(['red','green','blue','black'],2) -> [['red', 'green'], ['red', 'blue'], ['red', 'black'], ['green', 'blue'], ['green', 'black'], ['blue', 'black']]
#
# FOR OTHER OUTPUTS SEE EXTENSIONS.TXT
def combinations(theList, r):
    '''Takes a list and creates the amount of combinations defined by user
    input r
    '''
    listSize = len(theList)
    if r > listSize:
        return None
    newList = []
    comboSize = range(r)
    tmpList = []
    for n in comboSize:
        tmpList.append(theList[n])
    newList.append(tmpList)
    j = 0
    while j < listSize:
        finished = False
        tmpList = []
        i = 0
        for i in reversed(range(r)):
            if comboSize[i] != i + listSize - r:
                finished = False;
                break
        else:
            break
        comboSize[i] += 1
        for m in range(i+1, r):
            comboSize[m] = comboSize[m-1] + 1
        for j in comboSize:
            tmpList.append(theList[j])
        newList.append(tmpList)
    return newList


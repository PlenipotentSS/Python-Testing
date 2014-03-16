#!/usr/bin/env python
import re

class PlayFairCipher(object):
    # Data will be encoded by a key word
    def __init__(self):    
        """Constructor w/ param"""
        self.codeMatrix = [ ["","","","",""],
                            ["","","","",""],
                            ["","","","",""],
                            ["","","","",""],
                            ["","","","",""]]
        self.codePointer = [0,0];   #place char first, then update pointer ([row,col])
        self.alphabet = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.original = ['a','b','c','d','e',
                         'f','g','h','i','k',
                         'l','m','n','o','p',
                         'q','r','s','t','u',
                         'v','w','x','y','z']
    
    #store input variables from user
    def __init__(self, key):
        """Constructor w/ param"""
        self.key = key
        self.codeMatrix = [ ["","","","",""],
                            ["","","","",""],
                            ["","","","",""],
                            ["","","","",""],
                            ["","","","",""]]
        self.codePointer = [0,0];   #place char first, then update pointer ([row,col])
        self.alphabet = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.original = ['a','b','c','d','e',
                         'f','g','h','i','k',
                         'l','m','n','o','p',
                         'q','r','s','t','u',
                         'v','w','x','y','z']

    def setKey(self, key):
        self.key = key

    def occupied(self, c):
        ''' Checks whether the alphabet char
            has been used already or not
            return true if used, false otherwise'''
        index = ord(c) - 97
        if index >= 10:
            index = index-1
        if self.alphabet[index] == 0:
            self.alphabet[index] = 1
            return False
        else:
            return True

    def storeKey(self):
        '''Stores the key in the matrix,
            replacing and storing any
            used characters
            return null'''
        temp = self.key
        x = self.codePointer
        row = x[0]
        col = x[1]
        n = len(temp)
        for i in range(0,n):
            if self.occupied(temp[i]) is False:
                self.codeMatrix[row][col] = temp[i]
                if col==4:
                    row = row+1
                    col = 0
                else:
                    col = col+1
        self.codePointer = [row,col]
        
    def storeRemaining(self):
        ## Stores remaining alphabet after
        ## the key has stored. Run storeKey First!
        n = len(self.original)
        x = self.codePointer
        row = x[0]
        col = x[1]
        for i in range(0,n):
            if self.occupied(self.original[i]) is False:
                self.codeMatrix[row][col] = self.original[i]
                if col==4:
                    row = row+1
                    col = 0
                else:
                    col = col+1
    
    def createMatrix(self):
        self.storeKey()
        self.storeRemaining()
    
    def encode(self,string):
        print "Encoding PlayFair Matrix..."
        p = re.compile( '[^a-zA-z]' )
        string = p.sub('', string)
        string = string.lower()
        returnString = '';
        if len(string)%2 != 0:
            string = string+'x'
        for i in range(0,len(string),2):
            val_1 = string[i]
            if val_1 == 'j':
                val_1 = 'i'
            val_2 = string[i+1]
            if val_2 == 'j':
                val_2 = 'i'
            for j in range(0,5):
                if self.codeMatrix[j].__contains__(val_1):
                    val_1c = j
                    val_1r = self.codeMatrix[j].index(val_1)
                if self.codeMatrix[j].__contains__(val_2):
                    val_2c = j
                    val_2r = self.codeMatrix[j].index(val_2)
            if val_1c == val_2c:
                next_1r = (val_1r+1)%5
                next_2r = (val_2r+1)%5
                returnString = returnString + self.codeMatrix[val_1c][next_1r]
                returnString = returnString + self.codeMatrix[val_1c][next_2r]
            elif val_1r == val_2r:
                next_1c = (val_1c+1)%5
                next_2c = (val_2c+1)%5
                returnString = returnString + self.codeMatrix[next_1c][val_1r]
                returnString = returnString + self.codeMatrix[next_2c][val_1r]
            else:
                returnString = returnString + self.codeMatrix[val_1c][val_2r]
                returnString = returnString + self.codeMatrix[val_2c][val_1r]
            returnString = returnString + " "
        print "Encoded Message:"
        print returnString.upper()
    
    def decode(self, string):
        print "Decoding PlayFair Matrix..."
        p = re.compile( '[^a-zA-z]' )
        string = p.sub('', string)
        string = string.lower()
        returnString = '';
        for i in range(0,len(string),2):
            val_1 = string[i]
            if val_1 == 'j':
                val_1 = 'i'
            val_2 = string[i+1]
            if val_2 == 'j':
                val_2 = 'i'
            for j in range(0,5):
                if self.codeMatrix[j].__contains__(val_1):
                    val_1c = j
                    val_1r = self.codeMatrix[j].index(val_1)
                if self.codeMatrix[j].__contains__(val_2):
                    val_2c = j
                    val_2r = self.codeMatrix[j].index(val_2)
            if val_1c == val_2c:
                next_1r = (val_1r-1)%5
                next_2r = (val_2r-1)%5
                returnString = returnString + self.codeMatrix[val_1c][next_1r]
                returnString = returnString + self.codeMatrix[val_1c][next_2r]
            elif val_1r == val_2r:
                next_1c = (val_1c-1)%5
                next_2c = (val_2c-1)%5
                returnString = returnString + self.codeMatrix[next_1c][val_1r]
                returnString = returnString + self.codeMatrix[next_2c][val_1r]
            else:
                returnString = returnString + self.codeMatrix[val_1c][val_2r]
                returnString = returnString + self.codeMatrix[val_2c][val_1r]
        print "Encoded Message:"
        print returnString.upper()
    
    def printMatrix(self):
        print "Following is the matrix used for encoding/decoding purposes:"     
        print ""
        for i in range(0,5):
            print self.codeMatrix[i]
        print ""

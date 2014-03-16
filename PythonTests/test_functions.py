import Queue

def remove(string, chars):
    char_list = []
    return_string = []
    for c in chars:
        char_list.append(c)
    for c in string:
        remove = False
        for i in char_list:
            if ( c == i ):
                remove = True
        if (not remove):
            return_string.append(c)
    return "".join(return_string)


def reverseString(string):
    stack = []
    start = 0
    for i in range(len(string)):
        if ( string[i] == " "):
            stack.append(string[start:(i+1)])
            start = i+1
    if (start != len(string)):
        stack.append(string[start:len(string)]+" ")
    stack.reverse()
    return "".join(stack)
    
def atoi(string):
    i = 0
    size = len(string)
    neg = False
    if (string[0] == '-'):
        i += 1
        neg = True
    value = 0
    while( i < size):
        value *= 10
        value += ord(string[i])-ord('0')
        i += 1
    if (neg):
        value *= -1
    return value

def itoa(intval):
    string_list = []
    neg = False
    if ( intval < 0):
        neg = True
        intval *= -1
    if ( intval == 0) :
        return "0"
    while( intval != 0 ):
        string_list.append( str(intval % 10))
        intval = int(intval/10)
    string_list.reverse()
    return_string = "".join(string_list)
    if (neg):
        return_string = "-"+return_string
    return return_string

def telephoneWords(number,filename):
    if ( isinstance(number, int)):
        number = str(number)
    f = open(filename,'w')
    recursiveTelephoneWords(number, 0, "",f)
    f.close()

def recursiveTelephoneWords(number, index, word,f):
    if (index == len(number)):
        f.write(word+'\n')
        return
    key = number[index]
    index += 1
    if ( key == '0' or key == '1'):
        word += key
        recursiveTelephoneWords(number,index, word, f)
    else:
        for i in range(0,3):
            char = getCharKey(int(key),i)
            word += char
            recursiveTelephoneWords(number,index, word, f)
            word = word[:-1]
            

def getCharKey( key, place):
    keys = [['0'],     \
            ['1'], ['A','B','C'], \
                ['D','E','F'], \
                ['G','H','I'], \
                ['J','K','L'], \
                ['M','N','O'], \
                ['P','R','S'], \
                ['T','U','V'], \
                ['W','X','Y']]
    return keys[key][place]

def main():
    s = "Hello There World"
    r = "e"
    print(remove(s, r))

    print(reverseString(s))

    val = atoi("-1123512")
    print(type(val))
    print(str(val))
    val = itoa(-1123512)
    print(type(val))
    print(str(val))

    telephone_num = 2852693
    file_string = 'anne_number_codes.txt'
    telephoneWords(telephone_num,file_string)

if __name__ == '__main__':main()

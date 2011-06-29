import string

def getAlphabetizedNamesFromFile():
    fd = open('names.txt')
    names = fd.readlines()
    names = names[0]
    names = names.split(',')
    names = [x.strip('"') for x in names]
    names.sort()
    names = [string.lower(x) for x in names]
    return names


def getScore(name, num):

    score = 0
    for letter in name:
        score += ord(letter) - 96

    return score * num


def scoreFile():
    names = getAlphabetizedNamesFromFile()
    numNames = 1

    score = 0
    for name in names:

        score += getScore(name, numNames)
        numNames += 1
    
    return score

print scoreFile()

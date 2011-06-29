

def product(word):
    i = 1
    for x in word:
        i = i * int(x)
    return i

def getNum():
    fd = open('num.dat')
    text = fd.readlines()
    num = ''
    for line in text:
        num = num + line.strip()
    return num


def findHighestProductOfFive():

    num = getNum()

    x = 0
    y = 5

    candidate = 0
    candidate_info = ''

    while (y < 1001):

        iProduct = product(num[x:y])

        if iProduct > candidate:
            candidate = iProduct
            candidate_info = num[x:y]

        x += 1
        y += 1
        
    print candidate, ': ', candidate_info

findHighestProductOfFive()


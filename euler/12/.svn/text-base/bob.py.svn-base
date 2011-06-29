from math import sqrt

def getNthTriangleNum(num):

    return sum(range(1,num+1))



def getFactorsDumb(num):

    vals = []
    for x in xrange(1,num+1):

        if num % x == 0:
            vals.append(x)
    return vals
    

def isFactor(num, candidate):
    if num % candidate == 0:
        return True
    else:
        return False
    

def getFactorsSmart(num):

    factors = []

    for candidate in range(1,sqrt(num)+1):

        if isFactor(num, candidate):
            factors.append(candidate)

        if isFactor(num, num / candidate):
            factors.append(num / candidate)

    factors = list(set(factors))
    factors.sort()
                   
    return factors


def getFactorsCrazy(num):

    return [(n, num/n) for n in xrange(1,sqrt(num)) if num % n == 0]



def testFuncs():
    for x in range(1, 41):


        if getFactorsDumb(x) != getFactorsSmart(x):

            print 'the factors of ' , x, ' are: ', getFactorsSmart(x)
            print 'the factors of ' , x, ' are: ', getFactorsDumb(x)


def findNum():
    i = 1
    while True:

        triangle = getNthTriangleNum(i)

        length = len(getFactorsSmart(triangle))

        if length > 500:
            break

        i += 1

        print triangle

    print 'FOUND IT: ', triangle



#findNum()

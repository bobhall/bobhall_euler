from math import sqrt


MAX_SUM_SIZE = 28123

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

    factors.pop()
    return factors



def isPerfectNumber(n):

    return n == sum(getFactorsSmart(n))


def isAbundant(n):

    return n < sum(getFactorsSmart(n))


def getAbundants():

    ret_list = []
    for i in xrange(1,MAX_SUM_SIZE+1):
        if isAbundant(i):
            ret_list.append(i)
        
    return ret_list


print 'generating abundants....'
abundants = getAbundants()

def canBeWrittenAsAbundantSums(n):

    i = 0

    while abundants[i] < n:

        j = i

        while abundants[i] + abundants[j] <= n:



            if abundants[i] + abundants[j] == n:

                print n, ': ', abundants[i], ' plus ', abundants[j]

                return True

            j += 1

        i += 1


    return False



def useHashTable():


    d = {}


    print 'populating hash table....'
    
    for i in abundants:

        for j in abundants:

            d[ i+j ] = 1


    print 'searching hash table....'

    sum = 0
    for num in xrange(1,MAX_SUM_SIZE+4):

        if not d.has_key(num):
            print 'found one ', num
            sum += num

    print '\nSUM: ', sum



useHashTable()

def bruteForceSlow():
    sum = 0
    for i in xrange(8000,8200):
        if not canBeWrittenAsAbundantSums(i):

            print i
            
            sum += i

    print 'SUM: ', sum
        




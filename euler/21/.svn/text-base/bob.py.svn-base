from math import sqrt

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




def d(n):

    factors = getFactorsSmart(n)

    if len(factors) > 0:
        factors.pop()

    return sum(factors)

soFar = 0
for num in xrange(1,10001):

    if num == d(d(num)) and num != d(num):

        print 'found one: ', num, ' ', d(num)
        
        soFar += num

print soFar
    

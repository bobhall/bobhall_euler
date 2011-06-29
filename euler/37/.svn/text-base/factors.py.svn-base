from math import sqrt, ceil


def isFactor(num, candidate):
    if num % candidate == 0:
        return True
    else:
        return False

def getFactorsSmart(num):

    factors = []

    for candidate in range(1, int(ceil(sqrt(num)))+1):

        if isFactor(num, candidate):
            factors.append(candidate)

        if isFactor(num, num / candidate):
            factors.append(num / candidate)

    factors = list(set(factors))
    factors.sort()
                   
    return factors

def isPrimeFactors(num):

    if num == 1 or num == 2:
        return False

    return len(getFactorsSmart(num)) == 2


def isPrimeSlow(num):

    if num == 1 or num == 2 or num == 0:
        return False


    for x in xrange(2,num):

        if num % x == 0:
            return False

    return True



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

def isPandigital(text):

    if len(text) != 9:
        return False

    text = list(text)
    text.sort()

    return text == ['1','2','3','4','5','6','7','8','9']

def func():
    n = 1
    nums_found = set()
    UPPER_BOUND = 10000

    # why is the upper bound 10000?
    #
    # well, it's 5 digits, which leaves 4 left in order to be 9-pandigital.
    # 9 * 999 < 10000 and 99 * 99 < 10000, therefore you can never have
    # the remaining digits be factors of a 5 digit number
    while n < UPPER_BOUND:

        divisors = getFactorsSmart(n)

        for divisor in divisors:

            # Eg, '7254' + '39' + '186', since 7254 = 39 * 186
            s = str(n) + str(divisor) + str(n / divisor)

            if isPandigital(s):

                print 'found one: \t', n, ' = ', divisor, ' x ', n/divisor
                nums_found.add(n)
                
        n += 1


    print '\ndistinct values: ', len(nums_found)
    print 'sum: ', sum(nums_found)

func()
        

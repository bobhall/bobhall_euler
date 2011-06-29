


#
# return a list of primes between 2 and the largest prime greater than or equal to num
#
# This function reads the primes from a file containing the first 10,000 primes
#
# The 10,000th prime is 104729, so this function breaks after that
#
def getPrimesFromFile(num):

    if num > 104729:
        return []
    
    try:
        fd = open('primes.dat')

    except IOErrror:
        print "You do not have your input file set up!"
        return []
        

    nums = [int(x) for x in fd.read().split()]

    index = 0

    for x in nums:
        index = nums.index(x)
        if x > num:
            break

    return nums[:index]


#
# Returns a list of primes between 2 and the largest prime greater than or equal to num
#
def getPrimes(num):

    candidates = range(0,num+1)

    j = 2
    while (j < num):

        i = j

        if candidates[i] != 0:

            increment = i
            i += increment
    
            while (i < num+1):
                
                candidates[i] = 0
                i += increment

        j += 1


    return [x for x in candidates if x != 0 and x != 1]



    

def isPrime(num):

    if num == 0 or num == 1 or num == 2:
        return True

    i = 2

    while (i <= (num+1) / 2):

        if num % i == 0:
            return i
        i += 1

    return 0


def getPrimeFactors2(num):

    factors = []

    while isPrime(num):

        factor = isPrime(num)
        factors.append(factor)
        num = num / factor

    factors.append(num)

    return factors
        
        
        


            
def testIsPrime():

    primes = getPrimesFromFile(3000)

    for x in primes:
        if isPrime(x):
            print 'success'
        else:
            print 'fail'
        
#testIsPrime()    

def TestPrimes():
    for x in range(0,10000):
    
        nums1 = getPrimes(x)
        nums2 = getPrimesFromFile(x)

        if (nums1 != nums2):
            print 'Failed on: ', x, nums1, nums2
        else:
            print 'Success'

#TestPrimes()    



def getPrimeFactors(num):

    factors = []

    primes = getPrimes(num)

    print primes

    for p in primes:

        print p, ' % ', num, ' is ', p%num

        while num % p == 0:

            num = num / p
            factors.append(p)

    return factors
            







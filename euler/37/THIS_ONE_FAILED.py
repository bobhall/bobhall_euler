from operator import add


def isPrimeSlow(num):

    if num == 1 or num == 2 or num == 0:
        return False


    for x in xrange(2,num):

        if num % x == 0:
            return False

    return True
        
def test(nums):

    for num in nums:
        print "testing ", num
        print isPrimeSlow(num)
        print ''


def getPrimesSeive(num):

    nums = range(0,num+1)

    nums[0] = 0
    nums[1] = 0

    i = 2

    while i < len(nums) / 2:

        j = i
        val = nums[i]
    
        if val == 0:
            break


        while j < len(nums):

            j += val
            if j < len(nums):
                nums[j] = 0

        i += 1

        while nums[i] == 0 and i < len(nums):
            i += 1


    nums.sort()

    return list(set(nums))
        


def isPrimePrime(n):

    if n == 2 or n == 3 or n == 5 or n == 7:
        return False

    n = str(n)
    copy = n

    while len(n) > 0:

        if not isPrimeSlow(int(n)):

            return False

        n = n[1:]

    while len(copy) > 0:

        if not isPrimeSlow(int(copy)):

            return False

        copy = copy[0:len(copy)-1]
        
    return True
        




def func():

    LIMIT = 1000000
    
    print 'generating primes....'

    primes = getPrimesSeive(LIMIT)
    print 'checking all primes under: ', LIMIT

    num_found = 0
    
    for prime in primes:
        if isPrimePrime(prime):

            num_found += 1
            print 'found one: ', prime


        print prime

func()

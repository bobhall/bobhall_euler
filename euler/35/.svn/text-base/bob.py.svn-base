from operator import add

from collections import deque

#
# Return a list of primes under num using the seive of eratosthenes
#
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


    ret_list = []
    for i in nums:
        if i != 0:
            ret_list.append(i)

    return ret_list


primes = getPrimesSeive(1000000)        

def isPrime(n):
    return primes.count(n) > 0
    

def isRotationalPrime(n):

    rotations = deque(str(n))

    for rotation in range(0,len(rotations)):

        out_str = ''

        for d in rotations:
            out_str += d

        if not isPrime(int(out_str)):
            return False

        rotations.rotate(1)

    return True



def func():

    count = 0
    for prime in primes:

        if isRotationalPrime(prime):

            print 'found: ', prime
            count += 1

    print '\nTotal: ', count


func()

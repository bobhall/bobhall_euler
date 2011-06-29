

def isPrime(n):

    if n <= 0:
        return False

    if n == 1:
        return False
    if n == 2:
        return True

    for num in xrange(2,n):

        if n % num == 0:
            return False

    return True



def generatePrimes(a,b):

    n = 0

    while isPrime( n*n + (a*n) + b ):

        n += 1

    return n




def bruteForce():

    max_so_far = 0

    nums1 = range(-1000,1000)
    nums2 = range(-1000,1000)

    a = 0
    b = 0


    for num1 in nums1:

        for num2 in nums2:

            number_of_primes = generatePrimes(num1,num2)


            print num1, ' and ', num2, ' generated ', number_of_primes, ' primes'

            if number_of_primes > max_so_far:

                max_so_far = number_of_primes
                a = num1
                b = num2

    
    print a, ' and ', b, ' generated ', max_so_far, ' primes'


bruteForce()

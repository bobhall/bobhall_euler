
    

def isPrime(num):

    if num == 0 or num == 1:
        return False

    if num  == 2:
        return True

    i = 2

    while (i <= (num+1) / 2):

        if num % i == 0:
            return False
        i += 1

    return True



def getNthPrime(n):

    if n == 0:
        return 2

    prime = 0
    count = 0

    while count != n:

        if isPrime(prime):
            
            count += 1

        prime += 1


    return prime - 1

def test():
    for x in range(0, 20):
        print x, ": ", getNthPrime(x)


print getNthPrime(10001)

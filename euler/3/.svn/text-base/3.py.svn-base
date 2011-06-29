
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
        

print 'The prime factors of 600851475143 are: '

for factor in getPrimeFactors2(600851475143):
    print factor

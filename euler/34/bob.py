



facts = {}

facts[0] = 0
facts[1] = 1
facts[2] = 2
facts[3] = 6
facts[4] = 24
facts[5] = 120
facts[6] = 720
facts[7] = 5040
facts[8] = 40320
facts[9] = 362880


def factorial(n):


    if n == 1 or n == 0:
        return 1

    if n == 2:
        return 2

    if facts.has_key(n):
        return facts[n]

    else:
        answer = n * factorial(n-1)
        facts[n] = answer
        return answer

def hasProperty(n):

    print n

    num = str(n)

    sum = 0
    for c in num:

        sum += facts[int(c)]

    return sum == n




for i in range(3,3000000):
    if hasProperty(i):

        print i

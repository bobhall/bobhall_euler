from math import sqrt

def isTriple(nums):

    return sqrt(nums[0]) + sqrt(nums[1]) + sqrt(nums[2]) == 1000
    

def isTriple2(nums):

    return nums[0]**2 + nums[1]**2 == nums[2]**2


def getSquares(num):

    l = []

    i = 1

    while i**2 < num:

        l.append(i**2)
        i += 1
    return l

def getTriples():

    a = 1
    b = 1
    c = 1

    l = []

    while a < 500:

        b = a+1

        while a + b < 775:

            c = 1000 - (a + b)

            l.append((a,b,c))

            b += 1

        a += 1

    return l


l = getTriples()

for x in l:
    if isTriple2(x):
        print x
        break


    



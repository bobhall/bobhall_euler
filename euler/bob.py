
from operator import add



def getTriangleNum(n):


    return reduce(add, range(1,n+1))



def getFactors(n):

    if n == 1:
        return [1]

    ret_list = []
    for x in range(1,n+1):

        if n % x == 0:
            ret_list.append(x)

    return ret_list



def func():

    i = 1
    triangle = 1
    num_factors = 1

    while num_factors < 500:

        i += 1

        triangle = triangle + i

        num_factors = len(getFactors(triangle))

        print triangle, ': ', num_factors

        

func()

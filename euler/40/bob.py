

#
# The sequence of numbers follows this pattern: 12345678910111213141516171819202122 ....
# Ie, 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ... and concatenating them together.
# 
# This function returns the nth digit of that sequence.
#

def d(n):

    if n <= 0:
        return 0

    m = 1
    s = ''

    while len(s) <= n+1:

        s += str(m)
        m += 1

    return s[n-1]

product = 1
for x in range(0,7):
    val = int(d(pow(10,x)))
    product = product * val
    print "d(" + str(pow(10,x)) + ") is: " + str(val)


print '\nThe product is: ', product

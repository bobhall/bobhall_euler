
def isPandigital(text):
    text = list(text)
    text.sort()

    return text == ['1','2','3','4','5','6','7','8','9']


def isPandigitalOnBothEnds(text):

    text = list(text)
    
    if len(text) < 9:
        return False

    return isPandigital(text[-9:]) and isPandigital(text[:9])




fibs = {}
fibs[1] = 1
fibs[2] = 2
#
# Return the nth fib number
#
def fib(n):

    if fibs.has_key(n):
        return fibs[n]

    else:
        answer = fib(n-1) + fib(n-2)
        fibs[n] = answer
        return answer


print 'initializing table...'
b = 1
while b < 2800:
    fib(b)
    b += 300


def func():
    print 'searching...'
    n = 2749
    found_it = 0

    while 1:

        if n % 100 == 0:
            print n, ': has ', len(str(fib(n))), ' digits'

        if isPandigitalOnBothEnds(str(fib(n))):
            found_it = n
            break

        n += 1

    print '\nFound it: ', found_it

func()

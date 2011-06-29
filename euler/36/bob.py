
def isPalindrome(text):
    return text == text[::-1]


def decToBinary(n):

    ret_str = ''

    while n > 0:

        ret_str = str(n%2) + ret_str
        n = n / 2

    return ret_str


sum = 0
for num in range(1,1000000):

    if isPalindrome(str(num)):

        ones_zeros = decToBinary(num)

        if isPalindrome( ones_zeros ):

            sum += num
            print 'Dec: ', num, '\tbin: ', ones_zeros

print '\nSum: ', sum




def isPalindrome(word):
    return word == word[::-1]
    

def bruteForce():

    candidate = 0

    for i in range(1,999):

        for j in range(1, 999):

            product = i*j

            if isPalindrome(str(product)):

                if product > candidate:

                    candidate = product
    

    return candidate


print bruteForce()

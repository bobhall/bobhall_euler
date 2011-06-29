from factors import isPrimeFactors

# I'm just going to put this comment here.

#
#  A number n, is right truncatable if n is prime, and it continues to be prime as you "peel" off digits from the right:
#  Eg. 31139 -> 3113 -> 311 -> 31 -> 3 (these are all prime, therefore 31139 is a right-truncatable prime)
#
#  This function generates a list of truncatable primes of n-digit length and under.
#
def generateRightTruncatables(n):

    list1 =     [2,3,5,7]
    list2 =     []
    ret_list =  []

    if n == 1:
        return list1

    for i in range(1,n):
        for l in list1:
            for d in [1,3,7,9]:
                candidate = 10*l + d
                if isPrimeFactors(candidate):
                    list2.append(candidate)
                    ret_list.append(candidate)
        list1 = list2
        list2 = []

    return ret_list

def isLeftTruncatable(n):
    
    text = str(n)
    for i in range(1,len(text)):
        
        text = text[1:]
        if not isPrimeFactors(int(text)):
            return False

    return True

def func():
    nums = set()
    i = 2
    while len(nums) < 11:
    
        for i in generateRightTruncatables(i):
            if isLeftTruncatable(i):
                nums.add(i)
        i += 1


    nums = list(nums)
    nums.sort()

    print 'The primes that are truncatable from both left and right are: '
    for num in nums:
        print num

    print '\nTheir sum is: ', sum(nums)


func()

def isDivisiblebyAll(num):

    better = [11,12,13,14,15,16,17,18,19,20]

    # If x is divisible by 20, it's divisible by 2, 4, 5, 10
    # If x is divisible by 18, it's divisible by 9
    #, etc, etc, etc
    
    for x in better:
#    for x in range(1,21):
        if num % x != 0:
            return False

    return True

def findNum():
    
    i = 20
    while (1):
    
        if isDivisiblebyAll( i ):
            break;
        i = i + 20
    

    print i


findNum()

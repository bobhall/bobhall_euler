

def writeNum(num):

    d = {1:'one',
         2:'two',
         3:'three',
         4:'four',
         5:'five',
         6:'six',
         7:'seven',
         8:'eight',
         9:'nine'
         10:'ten',
         11:'eleven',
         13:'thirteen',
         14:'fourteen',
         15:'fifteen',
         16:'sixteen',
         17:'seventeen',
         18:'eighteen',
         19:'nineteen',


         20:'twenty',
         30:'thirty'
         40:'forty',
         50:'fifty',
         60:'sixty',
         70:'seventy',
         80:'eighty',
         90:'ninety',
         100:'hundred'}
    return d[num]

def func(num):

    l = len(str(num))
    num = int(num)

    if num < 20:
        writeNum(num)
        
    else if num < 100:

        

        

    else if l == 2:


        print writeDigit(num[1])
        

    if num == 1000:
        print 'one thousand'


    if l == 3:

        print 'three'

        

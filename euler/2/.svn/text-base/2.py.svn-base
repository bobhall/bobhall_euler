#!/usr/local/bin/python2.6

array = []

array.append(1)
array.append(2)

first = array[0]
second = array[1]

while (first + second < 4000000):
    val = first + second
    array.append(val)

    first = second
    second = val


sum = 0
for x in range(0,len(array)):
    if ( array[x] % 2 == 0 ):
        sum += array[x]

print sum


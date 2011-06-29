from itertools import permutations


iter = permutations([0,1,2,3,4,5,6,7,8,9])

i = 0

while i < 999999:
    iter.next()
    i+=1

print iter.next()


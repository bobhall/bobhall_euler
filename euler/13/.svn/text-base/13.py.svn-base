from operator import add

fd = open('nums.dat')
nums = fd.readlines()

print str(reduce(add, [int(x) for x in nums]))[:10]

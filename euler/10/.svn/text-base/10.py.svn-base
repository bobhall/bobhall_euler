from operator import add


nums = range(0,2000001)

nums[0] = 0
nums[1] = 0

i = 2

print 'seiving.... '

while i < len(nums) / 2:

    j = i
    val = nums[i]

    if val == 0:
        break

    print 'eliminating multiples of: ', val

    while j < len(nums):

        j += val
        if j < len(nums):
            nums[j] = 0


    i += 1

    while nums[i] == 0 and i < len(nums):
        i += 1
        

print 'adding up primes....'
print reduce(add, nums)


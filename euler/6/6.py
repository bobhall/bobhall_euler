from operator import add

m = range(1,101)
print pow(reduce(add, m), 2) - reduce(add, [pow(x,2) for x in m])

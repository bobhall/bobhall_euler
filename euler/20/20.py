from operator import add
from math import factorial


print reduce(add,[int(x) for x in str(factorial(100))])

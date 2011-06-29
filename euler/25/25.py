

d = {}
# Get the nth fibonacci sequence
def fib(n):

    if n == 1 or n == 2 or n == 0:
        return 1

    elif d.has_key(n):
        return d[n]

    else:
        answer = fib(n-1) + fib(n-2)
        d[n] = answer
        return answer


n = 1
while len(str(fib(n))) < 1000:
    n += 1

print n

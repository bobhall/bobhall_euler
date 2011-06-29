
d = {}
d[(20,20)] = 1

def func(a,b):

    if d.has_key((a,b)):
        return d[(a,b)]

    else:

        if a+1 > 20:
            if b+1 > 20:
                answer = 1
            answer = func(a,b+1)

        elif b+1 > 20:
            if a+1 > 20:
                answer = 1
            answer = func(a+1,b)

        else:
            answer = func(a+1,b) + func(a,b+1)

        d[(a,b)] = answer
        return answer


print func(0,0)
    

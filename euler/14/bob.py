
#
#  Collatz sequences look like this:
#  13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#

#
#  Which number under 1000000 has the longest chain?
#

def collatz(num):
    if num % 2 == 0:
        return num / 2
    else:
        return (3*num) + 1



d = {}
def getSequenceLen(num):

    # Base case
    if num == 1:
        return 1

    if d.has_key(num):
        return d[num]

    else:
        answer = 1 + getSequenceLen(collatz(num))
        d[num] = answer
        return answer


def findLongest(max):

    candidate_num = 0
    candidate_seq_len = 0

    for x in range(1,max+1):

        length = getSequenceLen(x)

        if length > candidate_seq_len:
            candidate_seq_len = length
            candidate_num = x

    return candidate_num, candidate_seq_len


print findLongest(1000000)        

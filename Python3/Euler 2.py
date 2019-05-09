import math

test = math.sqrt(23)

# Starting with 1 and 2, look at the Fibonacci sequence, under 4 million, and find the sum of the even valued terms
# create fibanacci sequence
limit = 4000000
i = 1
sum = 0
fibprev = 1
fibcurr = 2
fibnext = 0

while fibcurr < limit:

    if fibcurr % 2 == 0:
        sum += fibcurr
    fibnext = fibcurr + fibprev
    fibprev = fibcurr
    fibcurr = fibnext

print (sum)

# limit it to under 4 million
# sum even valued terms


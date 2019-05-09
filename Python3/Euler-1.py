# sum of all multiples of 3 or 5, below 1000
# loop iterate from 1-1000, compare each value to 3 or 5, if match, save value, move on to next.
i = 1000
sum = 0

for x in range(1, i):
    if x%3 == 0 or x%5 == 0:
        print(x)
        sum += x

print(sum)


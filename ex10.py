#generate lists of random amount of random numbers
#print out common elements in both

import random

a = sorted(random.sample(range(1,30), random.randint(10,20)))
b = sorted(random.sample(range(1,30), random.randint(10,20)))
c = [elem for elem in set(a) if elem in set(b)]

print(*a, sep = ", ")
print(*b, sep = ", ")
print(*c, sep = ", ")


"""
a2 = sorted(random.sample(range(1,30), 12))
b2 = sorted(random.sample(range(1,30), 16))
result_overlaps = [i for i in set(a2) if i in b2]
result = [i for i in result_overlaps if result_overlaps.count(i) == 1]
"""
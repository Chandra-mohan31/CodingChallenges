import itertools
from itertools import product


def b(s):
    # s = input()
    check = True
    rev = s[::-1]
    #print (rev)
    # print(s.islower())
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            # print("True")
            check = False
    if (rev == s and s.islower() and check):
        # print('Beat')
        return 1
    else:
        # print("No baet")
        return int(0)


n = int(input())
arr = []
for i in range(26):
    arr.append(chr(97+i))
# print(arr)
x = []
a = ['1', '2', '3']
# x=list(itertools.combinations_with_replacement(arr, n))
for roll in product(arr, repeat=n):
    x.append(roll)

# Str = ''.join([str(e) for e in a])
# print(Str)
summ = 0
for i in range(len(x)):
    s = ''.join([str(e) for e in x[i]])

    # summ = summ+
    #  print(s)
    summ += b(str(s))
    #
print(summ)

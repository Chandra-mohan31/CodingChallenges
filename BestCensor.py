
# import math
# print("enter the integers l,r,x:")
# s = input()
# arr = []
# arr = s.split()
# l = int(arr[0])
# r = int(arr[1])
# x = int(arr[2])


# def bestcensor(l, r, x):
#     # print(L, R, X)
#     # arrRange = []
#     # for i in range(L, R+1):
#     #     arrRange.append(i)
#     # # print(arrRange)
#     arrS1 = []
#     arrS2 = []

#     i = math.log(l, 2)
#     print(i)

#     for j in range(l, r+1):
#         if(pow(2, i) < j):
#             i += 1
#         arrS1.append(int(pow(2, i)))
#     print(arrS1)

#     for j in range(l, r+1):
#         if(x*i < j):
#             i += 1
#         arrS2.append(x*i)
#     print(arrS2)


# bestcensor(l, r, x)
import math
t = int(input())
for f in range(t):
    arr = input().split()
    l = int(arr[0])
    r = int(arr[1])
    x = int(arr[2])
    i = math.log(l, 2)
    arr = []
    arr1 = []
    for j in range(l, r+1):
        if(pow(2, i) < j):
            i += 1
        arr1.append(int(pow(2, i)))
        arr.append(int(j))
    print(arr)
    print(arr1)
    arr2 = []
    # i=math.log(l,2)
    for j in range(l, r+1):
        if(x*i < j):
            i += 1
        arr2.append(int(x*i))
    print(arr2)
    s2 = s1 = 0
    for i in range(len(arr)):
        if(abs(arr1[i]-arr[i]) < abs(arr2[i]-arr[i])):
            s1 += 1
        elif(abs(arr1[i]-arr[i]) > abs(arr2[i]-arr[i])):
            s2 += 1
    print(s1, s2)
    if s1 > s2:
        print(1)
    elif s1 < s2:
        print(2)
    else:
        print(0)

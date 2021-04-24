import sympy


def prime(n):
    c = 0
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            c += 1
    if c > 0:
        return False
    else:
        return True


def zed(n):
    if(n == 1):
        return int(0)
    elif(prime(n)):
        return int(1)
    elif(not prime(n)):
        x, y = findxy(n)
        return ((y*zed(x))+(x*zed(y)))
    # elif n==4:
    #     return 4


def strange_sum(L, R):
    # Write your code here
    sum1 = 0
    a = []
    for i in range(L, R+1):
        # sum1+=zed(i)
        a = divi(i)
        for j in a:
            sum1 += zed(j)

    return sum1


def divi(m):
    a = []
    for i in range(1, m+1):
        if m % i == 0:
            a.append(int(i))
    return a


def findxy(m):
    x, y = 0, 0
    for i in range(2, int(m/2)+1):
        for j in range(i, int(m/2)+1):
            if i*j == m:
                x = i
                y = j
                if x >= y:
                    x, y = y, x
                #print(x, y)
                return x, y


T = int(input())
for _ in range(T):
    s = input()
    arr = []
    arr = s.split()
    L = int(arr[0]) % 998244353
    R = int(arr[1]) % 998244353
    # print (L)

    out_ = strange_sum(L, R)
    print(out_)


print(sympy.isPrime(3))

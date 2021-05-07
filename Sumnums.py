

def numSquares(self, n: int) -> int:
    no_perfect = 0
    squares = []
    for i in range(1, int(n**0.5)+1):
        squares.append(i**2)
    v = []

    def printAllSubsetsRec(arr, n, v, Sum):

        if (Sum == 0):
            return len(v)

        if (Sum < 0):
            return sys.maxsize

        if (n == 0):
            return sys.maxsize

        x = printAllSubsetsRec(arr, n - 1, v, Sum)

        v.append(arr[n - 1])
        y = printAllSubsetsRec(arr, n, v,
                               Sum - arr[n - 1])
        v.pop(len(v) - 1)

        return min(x, y)

    def printAllSubsets(arr, n, Sum):

        v = []
        return printAllSubsetsRec(arr, n, v, Sum)

    arr = squares
    Sum = n
    m = len(arr)

    return printAllSubsets(arr, m, Sum)

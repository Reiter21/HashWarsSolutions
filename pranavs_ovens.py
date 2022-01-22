def findMinMoves(ovens):
    total, n = sum(ovens), len(ovens)

    if total % n:
        return -1
    target, res, toRight = total / n, 0, 0
    
    for m in ovens:
        toRight = m + toRight - target
        res = max(res, abs(toRight), m - target)

    return int(res)

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    print(findMinMoves(arr))

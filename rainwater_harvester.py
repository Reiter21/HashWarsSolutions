t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    
    left, right = 0, n-1
    ans = 0
    left_max = 0
    right_max = 0
    while (left < right):
        if arr[left] < arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                ans += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                ans += right_max - arr[right]
            right -= 1
    print(ans)
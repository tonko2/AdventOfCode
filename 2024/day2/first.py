import sys

data = sys.stdin.read()
lines = data.splitlines()

def check(arr):    
    increase = False
    if arr[0] < arr[1]:
        increase = True
    for i in range(len(arr) - 1):
        if increase:
            if 1 <= arr[i + 1] - arr[i] <= 3:
                continue
            return False
        else:
            if 1 <= arr[i] - arr[i + 1] <= 3:
                continue
            return False  
    return True

ans = 0
for line in lines:
    numbers = [int(num) for num in line.split()]
    ans += check(numbers)
print(ans)

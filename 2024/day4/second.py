import sys

data = sys.stdin.read()
lines = data.splitlines()

grid = []
for line in lines:
    grid.append(line)

def countXmas(grid, y, x):    
    if y - 1 < 0 or x - 1 < 0 or x + 1 >= len(grid[0]) or y + 1 >= len(grid):
        return 0
    str1 = grid[y - 1][x + 1] + grid[y + 1][x - 1]
    str2 = grid[y + 1][x + 1] + grid[y - 1][x - 1]
    if (str1 == "MS" or str1 == "SM") and (str2 == "MS" or str2 == "SM"):
        return 1
    else:
        return 0

ans = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'A':
            ans += countXmas(grid, i, j)
print(ans)

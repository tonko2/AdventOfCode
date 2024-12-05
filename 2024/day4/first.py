import sys

data = sys.stdin.read()
lines = data.splitlines()

grid = []
for line in lines:
    grid.append(line)
ans = 0

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

def countXmas(grid, y, x):
    res = 0
    for k in range(8):
        s = ""
        for i in range(3):
            nx = x + dx[k] * (i + 1)
            ny = y + dy[k] * (i + 1)
            if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
                break
            s += grid[ny][nx]
        if s == "MAS":
            res += 1            
    return res

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'X':
            ans += countXmas(grid, i, j)
print(ans)

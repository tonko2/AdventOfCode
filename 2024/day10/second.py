import sys
data = sys.stdin.read()
lines = data.splitlines()

grid = [line for line in lines]
pos = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '0':
            pos.append((j, i))
            
            
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs(start_x, start_y, x, y, cnt):
    global ans
    if cnt == 9:        
        ans += 1
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid) or grid[ny][nx] == '.':
            continue
        num = int(grid[ny][nx])
        if num == cnt + 1:
            dfs(start_x, start_y, nx, ny, num)
    return

ans = 0
for x, y in pos:
    dfs(x, y, x, y, 0)

print(ans)
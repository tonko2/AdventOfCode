import sys
data = sys.stdin.read()
lines = data.splitlines()

grid = []
for line in lines:
    grid.append(line)    

N = len(grid)
M = len(grid[0])
grid2 = []
for i in range(N):
    grid2.append(list('.' * M))
    
for i in range(N):
    for j in range(M):
        if grid[i][j] == '.':
            continue
        for k in range(N):
            for l in range(M):
                if i == k and j == l:
                    continue
                if grid[i][j] == grid[k][l]:
                    print(f'x = {j}, y = {i}, x2 = {l}, y2 = {k}')
                    x = j
                    y = i
                    x2 = l
                    y2 = k
                    x_abs = abs(j - l)
                    y_abs = abs(i - k)                    
                    if x > x2:
                        x, y, x2, y2 = x2, y2, x, y                    
                    if y < y2:
                        x = x - x_abs
                        y = y - y_abs
                        x2 = x2 + x_abs
                        y2 = y2 + y_abs                        
                    else:
                        x = x - x_abs
                        y = y + y_abs
                        x2 = x2 + x_abs
                        y2 = y2 - y_abs
                    if x < 0 or x >= N or y < 0 or y >= M:
                        pass
                    else:
                        grid2[y][x] = '#'
                    if x2 < 0 or x2 >= N or y2 < 0 or y2 >= M:
                        pass
                    else:
                        grid2[y2][x2] = '#'                            
                
ans = sum(row.count('#') for row in grid2)
for row in grid2:
    print(row)
print(ans)
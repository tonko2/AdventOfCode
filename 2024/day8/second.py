import sys
data = sys.stdin.read()
lines = data.splitlines()

grid = [list(line) for line in lines]
N = len(grid)
M = len(grid[0])

# 腹点を格納するマップ
grid2 = [['.'] * M for _ in range(N)]

# アンテナの位置を記録
antennas = {}
for i in range(N):
    for j in range(M):
        if grid[i][j] != '.':
            freq = grid[i][j]
            if freq not in antennas:
                antennas[freq] = []
            antennas[freq].append((j, i))  # (x, y) 形式で保存

# 腹点を計算
for freq, positions in antennas.items():
    n = len(positions)
    if n < 2:
        # 1つしかアンテナがない場合は無視
        continue

    # 各アンテナは自身を腹点として追加
    for x, y in positions:
        grid2[y][x] = '#'

    # アンテナ同士の直線上に腹点を計算
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = positions[i]
            x2, y2 = positions[j]

            # x, y の範囲を計算
            dx = x2 - x1
            dy = y2 - y1
            gcd = abs(dx) if dy == 0 else abs(dy) if dx == 0 else abs(__import__('math').gcd(dx, dy))
            step_x = dx // gcd
            step_y = dy // gcd

            x, y = x1, y1
            while 0 <= x < M and 0 <= y < N:
                grid2[y][x] = '#'
                x += step_x
                y += step_y

            # 逆方向も計算
            x, y = x2, y2
            while 0 <= x < M and 0 <= y < N:
                grid2[y][x] = '#'
                x -= step_x
                y -= step_y

# 一意な腹点の数を計算
ans = sum(row.count('#') for row in grid2)

# 結果を出力
for row in grid2:
    print("".join(row))
print(ans)

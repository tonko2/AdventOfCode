import sys

data = sys.stdin.read()
lines = data.splitlines()

def turn_right(direction):
    return {'^': '>', '>': 'v', 'v': '<', '<': '^'}[direction]

def move_forward(x, y, direction):
    if direction == '^':
        return x, y - 1
    elif direction == 'v':
        return x, y + 1
    elif direction == '<':
        return x - 1, y
    elif direction == '>':
        return x + 1, y

def in_bounds(x, y, rows, cols):
    return 0 <= y < rows and 0 <= x < cols

grid = []
for line in lines:    
    grid.append(line)

rows = len(grid)
cols = len(grid[0])

guard_x = guard_y = 0
direction = '^'
found = False
for i in range(rows):
    for j in range(cols):
        if grid[i][j] in '^>v<':
            guard_x, guard_y = j, i
            direction = grid[i][j]
            found = True
            break
    if found:
        break

visited = set()
visited.add((guard_x, guard_y))

seen_states = set()

while True:
    state = (guard_x, guard_y, direction)
    if state in seen_states:
        break
    seen_states.add(state)
    visited.add((guard_x, guard_y))
    nx, ny = move_forward(guard_x, guard_y, direction)

    if in_bounds(nx, ny, rows, cols) and grid[ny][nx] == '#':
        direction = turn_right(direction)
    else:
        guard_x, guard_y = nx, ny
        if not in_bounds(guard_x, guard_y, rows, cols):
            break

print(len(visited))

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

grid = [list(line) for line in lines]
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

start_pos = (guard_x, guard_y)

def simulate(grid, guard_x, guard_y, direction):
    seen_states = set()
    while True:
        state = (guard_x, guard_y, direction)
        if state in seen_states:
            return True
        seen_states.add(state)

        nx, ny = move_forward(guard_x, guard_y, direction)
        if not in_bounds(nx, ny, rows, cols):            
            return False
        if grid[ny][nx] == '#':            
            direction = turn_right(direction)
        else:            
            guard_x, guard_y = nx, ny

loop_count = 0
for y in range(rows):
    for x in range(cols):        
        if (x, y) == start_pos:
            continue
        
        if grid[y][x] == '.':            
            grid[y][x] = '#'            
            if simulate(grid, guard_x, guard_y, direction):
                loop_count += 1        
            grid[y][x] = '.'

print(loop_count)

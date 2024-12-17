import sys

buttonA = []
buttonB = []
prize = []

try:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        if line.startswith("Button A"):
            a_coords = tuple(map(int, line.split(":")[1].strip().replace("X+", "").replace("Y+", "").split(", ")))
            buttonA.append(a_coords)

        elif line.startswith("Button B"):
            b_coords = tuple(map(int, line.split(":")[1].strip().replace("X+", "").replace("Y+", "").split(", ")))
            buttonB.append(b_coords)

        elif line.startswith("Prize"):
            p_coords = tuple(map(int, [x.split("=")[1] for x in line.split(", ")]))
            prize.append(p_coords)

except EOFError:
    pass

N = len(prize)
ans = 0
for index in range(N):
    x, y = buttonA[index]
    x2, y2 = buttonB[index]
    x3, y3 = prize[index]
    
    candidate = 1000
    for i in range(100):
        for j in range(100):
            totalX = x * i + x2 * j 
            totalY = y * i + y2 * j           
            if x3 == totalX and y3 == totalY:
                candidate = min(candidate, i * 3 + j)
    if candidate != 1000:
        ans += candidate    
                
print(ans)
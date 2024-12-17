import sys
import math

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
    x3 += 10000000000000
    y3 += 10000000000000

    lcm = math.lcm(x, y)
    L1 = lcm // x
    L2 = lcm // y
    
    numerator = x3 * L1 - y3 * L2
    denominator = x2 * L1 - y2 * L2    
    
    if denominator != 0:
        if numerator % denominator == 0:
            b = numerator // denominator
            if (x3 - x2 * b) % x == 0:
                a = (x3 - x2 * b) // x            
                ans += a * 3 + b    
                
print(ans)
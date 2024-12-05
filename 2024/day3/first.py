import sys
import re

data = sys.stdin.read()
lines = data.splitlines()

def evaluate_all_mul(expression):
    matches = re.findall(r"mul\((\d+),(\d+)\)", expression)
    results = []
    for match in matches:        
        num1, num2 = map(int, match)
        results.append(num1 * num2)
    return results

ans = 0
for line in lines:
    ans += sum(evaluate_all_mul(line))
print(ans)
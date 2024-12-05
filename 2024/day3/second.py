import re

with open("input.txt", "r") as file:
    text = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
matches = re.finditer(pattern, text)

flag = True
ans = 0

for match in matches:
    if match.group() == "do()":
        flag = True
    elif match.group() == "don't()":
        flag = False
    elif flag and match.group(1) and match.group(2):
        a, b = int(match.group(1)), int(match.group(2))
        ans += a * b

print(ans)

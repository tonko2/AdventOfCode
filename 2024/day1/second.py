import sys
from collections import defaultdict

data = sys.stdin.read()

lines = data.splitlines()
ans = 0
num_dict = defaultdict(int)
for line in lines:
   _, b = map(int, line.split())
   num_dict[b] += 1   

for line in lines:
    a, _ = map(int, line.split())
    ans += a * num_dict[a]
print(ans)

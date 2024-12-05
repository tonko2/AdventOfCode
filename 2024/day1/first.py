import sys

data = sys.stdin.read()

lines = data.splitlines()
ans = 0
a_list = []
b_list = []
for line in lines:
   a, b = map(int, line.split())
   a_list.append(a)
   b_list.append(b)
a_list.sort()
b_list.sort()
for i in range(len(a_list)):
    ans += abs(a_list[i] - b_list[i])
print(ans)

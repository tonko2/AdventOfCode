import sys
from collections import defaultdict

data = sys.stdin.read()
lines = data.splitlines()


def check(mappings, updates):
    index = dict()
    for i, x in enumerate(updates):
        index[x] = i
    for i, x in enumerate(updates):
        for v in mappings[x]:
            if not v in index:
                continue
            if i > index[v]:
                return False
    return True

def reorder(mappings, updates):
    res = []
    for i, x in enumerate(updates):
        index = 0
        while index < len(res):
            v = res[index]
            if not x in mappings[v]:
                break
            index += 1
        res = res[0:index] + [x] + res[index:]
            
    return res

mappings = defaultdict(list)
flag = False
ans = 0
for line in lines:
    if line == "":
        flag = True
        continue
    if not flag:
        a, b = map(int, line.split('|'))
        mappings[a].append(b)        
    else:
        updates = list(map(int, line.split(',')))
        if not check(mappings, updates):
            updates = reorder(mappings, updates)
            ans += updates[len(updates) // 2]

print(ans)
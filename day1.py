from collections import Counter

with open("input/1.txt") as inpt:
    lines = [ln.split() for ln in inpt.readlines()]

lft, rgt = zip(*lines)

lft = sorted(map(int, lft))
rgt = sorted(map(int, rgt))

print(sum(abs(x - y) for x, y in zip(lft, rgt)))

rgt_counter = Counter(rgt)

print(sum(x * rgt_counter[x] for x in lft))

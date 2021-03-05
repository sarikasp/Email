import sys, re

d = {}
for j in zip(*[re.split("\W+", open(sys.argv[1], 'r', encoding="utf-8").read().lower())[i:] for i in range(int(sys.argv[2]))]):
    d[j] = d.get(j, 0) + 1
    [print("".join(k)+""+str(d.get(k))+"\n")for k in sorted(d) if d.get(k) == int(sys.argv[3]) and re.search("^\w{"+sys.argv[4] + "}(.+)? \w {"+sys.argv[5]+"}$", "".join(k))]



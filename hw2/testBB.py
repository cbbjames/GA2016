import sys

cntn=open(sys.argv[1]).readlines()
all=[]
for L in cntn:
    L=L.split()
    a=L[1:]
    a=[int(i) for i in a]
    all.append(a)

print(all)
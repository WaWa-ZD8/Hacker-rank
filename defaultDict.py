from collections import defaultdict

d = defaultdict(list)
n,m = list(map(int,(input().split())))

for i in range(n):
    d["A"].append(input())
    
for i in range(m):
    d["B"].append(input())

for char in d["B"]:
    indices = [(i+1) for i, x in enumerate(d["A"]) if x == char]
    if indices:
        print(" ".join(map(str, indices)))
    else:
        print("-1")

    
    
        
    
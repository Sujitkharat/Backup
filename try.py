import sys
from collections import defaultdict
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")

def solve(parent,source,dist,graph,arr):
    if dist==0:
        arr[0]+=1
        return
    for i in graph[source]:
        if i !=parent:
            solve(source,i,dist-1,graph,arr)
    return arr[0]
n,d = input().split()
arr= [0]
graph = defaultdict(list)
for i in range(int(n)-1):
    x,y = input().split()
    graph[x].append(y)
    graph[y].append(x)
print(solve('1','1',int(d),graph,arr))


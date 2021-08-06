import sys
from collections import defaultdict
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")

def josephus(arr,k,index):
    if len(arr) == 1:
        return arr[0]
    remove = (index+k)%len(arr)
    arr.pop(remove)
    return josephus(arr,k,remove)
n, k = map(int, input().split())
arr = [int(x) for x in range(1,n+1)]
print(josephus(arr,k-1,0))


import sys
from collections import defaultdict
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")

def solve(a,b,c,n):
    m = {}
    if n==a or n==b or n==c:return n
    return solve(a,b,c,n-1)+solve(a,b,c,n-2)+solve(a,b,c,n-3)

for _ in range(int(input())):
    a,b,c,n = [int(x) for x in input().split()]
    print(solve(a,b,c,n))

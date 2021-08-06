import sys
from collections import defaultdict
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")

def ratinmaze(mat,n):
    pass


n = int(input())
mat = [[int(x) for x in input().split()]for y in range(n)]
ratinmaze(mat,n)
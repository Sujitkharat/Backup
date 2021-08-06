import sys
from collections import defaultdict
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")

def stair(slen):
    if slen<0:
        return 0
    if slen==0:
        return 1
    return stair(slen-1)+stair(slen-2)+stair(slen-3)

slen = int(input())
print(stair(slen))

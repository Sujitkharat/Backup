import sys
from collections import defaultdict
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")


def check(B):
    Uni = {")":"(","]":"[","}":"{"}
    ans = []
    for j in B:
        if j==")" or j=="]" or j=="}":
            if len(ans)==0:return False
            v = ans.pop()
            if v!=Uni[j]:
                return False
        else:
            ans.append(j)
    return len(ans)==0

for k in range(int(input())):
    B = input()
    print("YES") if check(B) else print("NO")
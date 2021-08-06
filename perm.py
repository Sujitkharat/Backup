import sys
from collections import defaultdict
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")

def permute(a, l, r):
    if l==r:
        b = "".join(a)
        print(b)
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack

# Driver program to test the above function
string = "123"
n = len(string)
a = list(string)
permute(a, 0, n-1)
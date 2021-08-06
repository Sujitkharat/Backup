import sys
from collections import defaultdict
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")

def powerset(arr,index,output):
    if len(arr)<=index:
        print(output)
        return
    powerset(arr,index+1,output)
    powerset(arr,index+1,output+[arr[index]])

arr = [int(x) for x in input().split()]
powerset(arr,0,[]) 

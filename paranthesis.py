import sys
from collections import defaultdict
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")

'''

def Allparenthesis(n):
    
    def balanced(ans, i, cnt):
        if i == len(ans): return cnt == 0
        if cnt < 0: return False
        if ans[i] == "(": return  balanced(ans, i + 1, cnt + 1)
        elif ans[i] == ")": return  balanced(ans, i + 1, cnt - 1)
        return balanced(ans, i + 1, cnt)

    def gen(n, opening,closing,ans):
        if len(ans)==n:
            if balanced(ans,0,0):
                print(ans)
            return
        gen(n,opening,closing,ans+opening)
        gen(n,opening,closing,ans+closing)
    gen(n*2,'(',')',"")

n = int(input())
Allparenthesis(n)

'''

def Allparenthesis(n):
    def gen(o_count,c_count,ans):
        if o_count==0 and c_count==0:
            print(ans)
            return
        if o_count != 0:
            gen(o_count-1, c_count,ans+"(")
        if c_count>o_count:
            gen(o_count,c_count-1,ans+")")
    
    gen(n,n,"")
n = int(input())
Allparenthesis(n)
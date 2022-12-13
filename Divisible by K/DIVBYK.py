import math
t=int(input())
for _ in range(t):
    (n,k)=map(int,input().split())
    x=list(map(int,input().split()))
    flag=0
    for i in range(n-1):
        for j in range(i+1,n):
            s=x[i:j+1]
            y=math.prod(s)
            if y%k==0:
                print("YES")
                flag=1
                break
        if flag==1:
            break
    if flag==0:
        print("NO")
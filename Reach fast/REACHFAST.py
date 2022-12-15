t=int(input())
for _ in range(t):
    (x,y,k)=map(int,input().split())
    x=abs(x-y)
    count=0
    if x%k!=0:
        count+=1
    print(int(x/k)+count)
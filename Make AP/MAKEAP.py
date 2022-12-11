t=int(input())
for _ in range(t):
    (a,b)=map(int,input().split())
    if a==b:
        print(a)
    elif (a+b)%2==0:
        print((a+b)//2)
    else:
        print(-1)
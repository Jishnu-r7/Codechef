t=int(input())
for _ in range(t):
    (a,b)=map(int,input().split())
    x=2**b
    for i in range(a):
        x=x//2
    print(x)
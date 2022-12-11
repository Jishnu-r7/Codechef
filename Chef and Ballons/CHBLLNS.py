t=int(input())
for i in range(t):
    x=list(map(int,input().split()))
    n=int(input())
    x.sort()
    if x[0]>=n:
        k=1+((n-1)*3)
    elif n>x[0] and n<=x[1]:
        k=1+(x[0]*3)+((n-x[0]-1)*2)
    else:
        k=(x[0]*3+(x[1]-x[0])*2+n-x[1])
    print(k)
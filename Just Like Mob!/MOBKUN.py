t=int(input())
for i in range(t):
    x=list(map(int,input().split()))
    
    n=x[3]%((x[0]*x[2])+x[1])
    if n==0 or n>((x[0]*x[2])+x[1]-(x[0]+x[1])):
        print("YES")
    else:
        print("NO")
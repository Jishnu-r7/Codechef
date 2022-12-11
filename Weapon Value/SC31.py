t=int(input())
for i in range (t):
    n=int(input())
    x=list(input())
    for j in range(n-1):
        y=input()
        for k in range(10):
            if x[k]==y[k]:
                x[k]='0'
            else:
                x[k]='1'
    print(x.count('1'))
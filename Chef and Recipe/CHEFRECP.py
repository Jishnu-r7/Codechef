import numpy as np
t=int(input())
for i in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    k=x[0]
    count=[]
    c=0
    flag=0
    y=unique(x)
    for j in range (n):
        if ((k==x[j]) and (x[j] in y) and (x[j+1]==x[j])):
            c+=1
        elif x[j] not in y:
            print("NO")
            flag=1    
            break
        elif (x[j+1]!=k):
            c+=1
            if c in count:
                print("NO")
                flag=1
                break
            count.append(c)
            y.remove(k)
            k=x[j+1]
    if flag==0:
        print("YES")
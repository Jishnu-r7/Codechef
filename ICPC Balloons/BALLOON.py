t=int(input())
for _ in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    y=[1,2,3,4,5,6,7]
    count=0
    for i in x:
        count+=1
        if i in y:
            y.remove(i)
        if y==[]:
            break
    print(count)
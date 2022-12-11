# cook your dish here
t=int(input())
for _ in range(t):
    (a,b)=map(int,input().split())
    if a-b>0:
        print("LOSS")
    elif a-b<0:
        print("PROFIT")
    else:
        print("NEUTRAL")
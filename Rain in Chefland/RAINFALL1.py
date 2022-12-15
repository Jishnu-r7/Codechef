t=int(input())
for _ in range(t):
    x=int(input())
    if x<3:
        print("LIGHT")
    elif x<7:
        print("MODERATE")
    else:
        print("HEAVY")
n = 5
cen = n//2+1 #centre
for x in range(1,n+1):
    for y in range(1,n+1):
        if(x==cen and y==cen):
            print("  ",end="")
        else:
            print("* ",end="")
    print()            
n = 5
cen = 1 #centre
for x in range(1,n+1):
    for y in range(1,n+1):
        if(x==y or y==cen ):
            print("* ",end="")
        else:
            print("  ",end="")
    print()            
inc = 1
char = 65
for x in range (5,0,-1):
    for y in range(x,0,-1):
        print(" ",end="")
    print(chr(char)*inc)
    char += 2
    inc += 2    
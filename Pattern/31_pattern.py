for i in range(5,0,-1):
    for j in range(5, 0, -1):
        if i >= j:
            print(j, end="")

        else:
            print(" ", end="")
    print()

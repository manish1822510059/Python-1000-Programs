for i in range(1, 6):
    for j in range(5, 0, -1):
        if i >= j:
            print(j--, end="")

        else:
            print(" ", end="")
    print()

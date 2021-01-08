for i in range(1, 6):
    for j in range(5, 0, -1):
        if i >= j:
            print("*", end="")

        else:
            print(" ", end="")
    print()

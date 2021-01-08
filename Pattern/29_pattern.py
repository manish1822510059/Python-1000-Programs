for i in range(1, 6):
    for j in range(5, 0, -1):
        if i >= j:
            print(chr(j+64), end="")

        else:
            print(" ", end="")
    print()

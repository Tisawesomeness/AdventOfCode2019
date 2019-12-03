with open("D1.txt", "r") as f:
    print(sum( (int(x) // 3 - 2 for x in f) ))

def consume(fuel):
    n = int(fuel) // 3 - 2
    if n <= 0:
        return 0
    return n + consume(n)
with open("D1.txt", "r") as f:
    print(sum( (consume(int(x)) for x in f) ))

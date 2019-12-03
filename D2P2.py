with open("D2.txt", "r") as f:
    p = [int(i) for i in f.read().split(",")]
# Brute force n and v
for n in range(100):
    for v in range(100):
        prog = p.copy() # Make sure program does not change between runs
        prog[1] = n
        prog[2] = v
        for i in range(0, len(prog), 4):
            if prog[i] == 99:
                break
            # Check for OOB
            if prog[i + 1] >= len(prog) or prog[i + 2] >= len(prog) or prog[i + 3] >= len(prog):
                break
            if prog[i] == 1:
                prog[prog[i + 3]] = prog[prog[i + 1]] + prog[prog[i + 2]]
            if prog[i] == 2:
                prog[prog[i + 3]] = prog[prog[i + 1]] * prog[prog[i + 2]]
        # Check for correct n and v
        if prog[0] == 19690720:
            print(100 * n + v)

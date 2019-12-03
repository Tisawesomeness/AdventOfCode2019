with open("D2.txt", "r") as f:
    prog = [int(i) for i in f.read().split(",")]
# Starting modifications
prog[1] = 12
prog[2] = 2
# Main program
for i in range(0, len(prog), 4):
    if prog[i] == 99: # Stop opcode
        break
    if prog[i] == 1: # Add opcode
        prog[prog[i + 3]] = prog[prog[i + 1]] + prog[prog[i + 2]]
    if prog[i] == 2: # Multiply opcode
        prog[prog[i + 3]] = prog[prog[i + 1]] * prog[prog[i + 2]]
print(prog[0])

import re
with open('input.txt','r') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
instructions = []
for line in lines:
    raw = line.split(" ")
    instr = raw[0]
    val = int(raw[1][1:])
    if (raw[1][0] == "-"):
        val*=-1
    instructions.append((instr,val))

#Part 1
index = 0
acc = 0
ran = []
while True:
    if(index in ran):
        print(acc)
        break
    ran.append(index)
    instr = instructions[index][0]
    val = instructions[index][1]
    if(instr == "acc"):
        acc+=val
    elif(instr == "jmp"):
        index+=val
        continue
    index += 1
    
    
#Part 2
    
def run(instructions):
    index = 0
    acc = 0
    ran = []
    while index < len(instructions):
        if(index in ran):
            return "Loop"
        ran.append(index)
        instr = instructions[index][0]
        val = instructions[index][1]
        if(instr == "acc"):
            acc+=val
        elif(instr == "jmp"):
            index+=val
            continue
        index += 1
    return acc
#Test all nop and JMP functions
for ind, instr in enumerate(instructions):
    if (instr[0] == "nop"):
        new = instructions.copy()
        new[ind] = ("jmp",new[ind][1])
        result = run(new)
        if (result != "Loop"):
            print(result)
    elif(instr[0] == "jmp"):
        new = instructions.copy()
        new[ind] = ("nop",new[ind][1])
        result = run(new)
        if (result != "Loop"):
            print(result)
        
        

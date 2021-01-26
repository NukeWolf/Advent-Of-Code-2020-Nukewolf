import math as m
with open('input.txt','r') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
instructions = []

for line in lines:
    raw = line.split(" = ")
    if("mem" in raw[0]):
        instr = int(raw[0][line.find("[")+1:line.find("]")])
        val = int(raw[1])
    else:
        instr = raw[0]
        val = raw[1]
    instructions.append((instr,val))
#print(instructions)

#Part 1
    
mem = [0]*100000
mask = None
for instr,val in instructions:
    if(instr == "mask"):
        mask = val
    else:
        binary = list(bin(val)[2:].zfill(36))
        for ind,bit in enumerate(mask):
            if(bit != "X"):
                binary[ind] = bit
        mem[instr] = int("".join(binary),2)
print(sum(mem))


#Part 2


def resolveFloat(binary,val):
    if(not "X" in binary):
        instr = "".join(binary)
        mem[instr] = val
        return
    ind = binary.index("X")
    new = binary.copy()
    new[ind] = "0"
    resolveFloat(new,val)
    
    new = binary.copy()
    new[ind] = "1"
    resolveFloat(new,val)

mem = {}
mask = None
for instr,val in instructions:
    if(instr == "mask"):
        mask = val
    else:
        binary = list(bin(instr)[2:].zfill(36))
        for ind,bit in enumerate(mask):
            if(bit == "X" or bit == "1"):
                binary[ind] = bit
        resolveFloat(binary,val)
count = 0
for val in mem:
    count+=mem[val]
print(count)
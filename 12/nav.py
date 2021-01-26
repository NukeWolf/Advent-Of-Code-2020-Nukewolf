import math as m
with open('input.txt','r') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
instructions = []

for line in lines:
    instr = line[0]
    val = line[1:]
    instructions.append((instr,int(val)))

#Part 1
    
x = 0
y = 0
rot = 0

for instr,val in instructions:
    if(instr == "E"):
        x+=val
    elif(instr == "W"):
        x-=val
    elif(instr == "N"):
        y+=val
    elif(instr == "S"):
        y-=val
    elif(instr == "L"):
        rot+=val
    elif(instr == "R"):
        rot-=val
    elif(instr == "F"):
        x+= m.cos(m.radians(rot))*val
        y+= m.sin(m.radians(rot))*val
print(x+y)

x = 0
y = 0
rot = 0
wx = 10
wy = 1

for instr,val in instructions:
    if(instr == "E"):
        wx+=val
    elif(instr == "W"):
        wx-=val
    elif(instr == "N"):
        wy+=val
    elif(instr == "S"):
        wy-=val
    elif(instr == "L"):
        for i in range(int(val/90)):
            newX = wy*-1
            newY = wx
            wx = newX
            wy = newY
    elif(instr == "R"):
        for i in range(int(val/90)):
            newX = wy
            newY = wx*-1
            wx = newX
            wy = newY
    elif(instr == "F"):
        x += wx*val
        y += wy*val
print(abs(x)+abs(y))

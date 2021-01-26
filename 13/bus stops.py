with open('input.txt','r') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]

current = int(lines[0])
buses = lines[1].split(',')

#Part 1
#Accidently looked for max difference instead of mininunum 
difference = []
ids = []

for bus in buses:
    if (bus == 'x'):
        continue
    if(current % int(bus) == 0):
        difference.append(0)
        ids.append(bus)
    dif = int(bus)-(current % int(bus))
    difference.append(dif)
    ids.append(int(bus))
Max = min(difference)
for index,dif in enumerate(difference):
    if (dif == Max):
        print(dif)
        print(ids[index])
        print(dif*ids[index])
        
        
#Part 2
        

offsets = []
for ind,bus in enumerate(buses):
    if (bus == 'x'):
        continue
    offsets.append((ind,int(bus)))
print(offsets)

#Done manually for now

timestamp = 0
index = 0
increase = 1
#This works lmao. Basically, once it finds 2 number with a common multiple, it changes the increase to that common multiple
while True:
    timestamp+=increase
    offset = offsets[index][0]
    bus = offsets[index][1]
    if((timestamp + offset) % bus == 0):
        index+=1
        increase*=bus
    if (index == len(offsets)):
        print(timestamp)
        break
        
    
    

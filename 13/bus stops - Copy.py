with open('test.txt','r') as f:
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
offsets = [ (ind-4,bus) for ind,bus in offsets]
print(offsets)

def confirmValid(timestamp):
    for offset,bus in offsets:
        if((timestamp + offset) % bus != 0):
            return False
    return True

timestamp = 0
while True:
    if(timestamp%10000000 == 0):
        print(timestamp)
    timestamp += 59
    if(confirmValid(timestamp)):
        print(timestamp)
        break
    

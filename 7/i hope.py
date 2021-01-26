import re
with open('input.txt','r') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]


#Part 1
# Make sure to subtract 1 from the answer to not include the original shiny gold bag in the set.

keys = ["shiny gold"]
count = 1
while True:
    for line in lines:
        raw = line.split(" bags contain ")
        color = raw[0]
        val = raw[1]
        for key in keys:
            if(key in val):
                keys.append(color)
    keys = set(keys)
    if(len(keys) == count):
        break
    count = len(keys)
    keys = list(keys)
print(len(keys))


#Part 2
bagkey = {}
for line in lines:
    raw = line.split(" bags contain ")
    #Parent color
    top = raw[0]
    bagkey[top] = []
    #The children
    bot = raw[1].split(",")
    #Check if it is no other bags
    if("no other bags"  in line):
        continue
    #For each child
    for val in bot:
        #Split into 4 values to get count of bags and color
        fields = val.strip().split(" ")
        #print(fields)
        num = int(fields[0])
        color = fields[1]+" "+fields[2]
        bagkey[top].append({'color':color,'num':num})

def findNumBags(color):
    info = bagkey[color]
    if info == []:
        return 0
    bagTotal = 0
    for bags in info:
        bagTotal += bags['num'] * (findNumBags(bags['color']) + 1)
    return bagTotal
    
#Again, Subtract by 1, to not include the original shiny gold bag
print(findNumBags("shiny gold"))


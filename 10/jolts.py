with open('input.txt','r') as f:
    lines = f.readlines()
adapters = [int(x.strip()) for x in lines]
#Need to include the wall jolts at 0 and the phone adapters joltage
adapters = [0] + sorted(adapters) + [(max(adapters) + 3)]
print(adapters)

#Part 1
jolt1 = 0
jolt3 = 0
for ind,adapter in enumerate(adapters):
    if (ind == len(adapters)-1):
        break
    difference = adapters[ind+1]-adapter
    print(difference)
    if(difference == 3):
        jolt3+=1
    if(difference == 1):
        jolt1+=1
print(adapters)
print(jolt3*jolt1)

#Part 2
memoize = [None]*len(adapters)

def findPath(index):
    if(index == len(adapters)-1):
        return 1
    if(not memoize[index] == None):
        return memoize[index]
    nextPaths = adapters[index+1:index+4]
    currentVal = adapters[index]
    pathNum = 0
    for ind,path in enumerate(nextPaths):
        if(currentVal+3 >= path):
            pathNum += findPath(index+ind+1)
    memoize[index] = pathNum
    return pathNum

print(findPath(0))
print(memoize)

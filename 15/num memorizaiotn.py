puzzleIn = "1,0,18,10,19,6"

nums = puzzleIn.split(",")
nums = [int(x) for x in nums]
nums = [x for x in reversed(nums)]
#Part 1

count = 0
while len(nums) < 2020:
    count+=1
    if (count%10000 == 0):
        print(count)
    current = nums[0]
    try:
        ind = nums[1:].index(current)
        nums.insert(0,ind+1)
    except:
        nums.insert(0,0)
print(len(nums))


#Part 2
nums = puzzleIn.split(",")
nums = [int(x) for x in nums]

key = {}
count = 1
lastSpoken = 0
#Setup
for num in nums[:-1]:
    key[num] = count
    count+=1
lastSpoken = nums[-1]
    
#Actual lets go
while count<30000000:
    try:
        last = key[lastSpoken]
        key[lastSpoken] = count
        lastSpoken = count-last  
    except:
        key[lastSpoken] = count
        lastSpoken = 0
    count+=1
    if(count%1000000 == 0):
        print(count)
print(lastSpoken)
    

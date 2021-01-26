import re
import itertools
with open('input.txt','r') as f:
    lines = f.readlines()
nums = [int(x.strip()) for x in lines]
#Part 1
PREAMBLE = 25

def testSample(sample,num):
    for x,y in itertools.product(sample,repeat=2):
        if(x+y == num and x != y):
            return True
    return False

for count, num in enumerate(nums):
    if(count<PREAMBLE):
        continue
    #STUPID OFF BY ONE SUBSTRTING ERROR
    sample = nums[count-PREAMBLE:count]
    if (not testSample(sample,num)):
        print(num)
        break
    
    
    
#Part 2
invalid = 23278925

for index1 in range(len(nums)):
    for index2 in range(index1,len(nums)):
        vals = nums[index1:index2+1]
        if(sum(vals) == invalid):
            print(sorted(vals)[0] + sorted(vals)[-1])
        elif(sum(vals) > invalid):
            break
    
    
    
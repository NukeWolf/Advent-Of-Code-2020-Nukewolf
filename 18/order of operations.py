import re
with open('input.txt','r') as f:
    lines = f.readlines()
lines = [x.strip().replace(" ","") for x in lines]
#print(lines)

#Part 1
def findEndParen(string):
    current = 1
    for ind,val in enumerate(string):
        if(val == "("):
            current +=1
        elif(val == ")"):
            current -=1
        if(current == 0):
            return ind
def findFirstParen(string):
    current = 1
    for ind,val in enumerate(string[::-1]):
        if(val == ")"):
            current +=1
        elif(val == "("):
            current -=1
        if(current == 0):
            return len(string) - ind - 1
def solveExpression(string):
    result = 0
    skip = -1
    operation = "+"
    for ind,val in enumerate(string):
        if(ind <= skip):
            continue
        if(val.isnumeric()):
            if(operation == "+"):
                result += int(val)
            else:
                result *= int(val)
        elif(val == "+" or val == "*"):
            operation = val
        elif(val == "("):
            start = ind
            end = start + 1 + findEndParen(string[start+1:])
            skip = end
            if(operation == "+"):
                result += solveExpression(string[start+1:end])
            else:
                result *= solveExpression(string[start+1:end])
    return result
count = 0
for line in lines:
    res = solveExpression(line)
    count+= res 
print(count)

def insert_str(string, str_to_insert, index):
    return string[:index] + str_to_insert + string[index:]



#Part 2

newLines = []
for line in lines:
    index = 0
    while (index < len(line)):
        if (line[index] == "+"):
            #Check what is before
            if(line[index+1].isnumeric()):
                line = insert_str(line,")",index+2)
            if(line[index+1]=="("):
                end = index + 3 + findEndParen(line[index+2:])
                line = insert_str(line,")",end)
            if(line[index-1].isnumeric()):
                line = insert_str(line,"(",index-1)
            if(line[index-1]==")"):
                beginning = findFirstParen(line[:index-1])
                line = insert_str(line,"(",beginning)
            index+=1
        index+=1
        #print(line)
        
        #input()
    newLines.append(line)
count = 0
for line in newLines:
    res = solveExpression(line)
    print(res)
    count+= res 
print(count)
    
            
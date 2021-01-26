from pprint import pprint
import itertools
with open('input.txt','r') as f:
    lines = f.read().split('\n\n')
rawRules = lines[0].splitlines()
rules = {}
for rawRule in rawRules:
    key = rawRule.split(": ")[0]
    rule = rawRule.split(": ")[1]
    pipes = rule.split(" | ")
    newPipes = []
    for pipe in pipes:
        newPipes.append(pipe.split(" "))
    rules[key] = newPipes
#print(rules["8"])

def evalRule(rule):
    rule = rules[rule]
    if(rule[0][0] == '"b"'):
        return ["b"]
    if(rule[0][0] == '"a"'):
        return ["a"]
    vals = []
    for pipe in rule:
        pipeVals = []
        newPipeVals = []
        for ruleVal in pipe:
            pipeVals.append(evalRule(ruleVal))
        if (len(pipeVals) == 1):
            vals.append(pipeVals[0])
        elif (len(pipeVals) == 2):
            for first,last in itertools.product(pipeVals[0],pipeVals[1]):
                newPipeVals.append(''.join(first)+''.join(last))
            vals.append(newPipeVals)
        elif (len(pipeVals) == 3):
            for first,second,last in itertools.product(pipeVals[0],pipeVals[1],pipeVals[2]):
                newPipeVals.append(''.join(first)+''.join(second)+''.join(last))
            vals.append(newPipeVals)
    return [item for val in vals for item in val]

#matches = evalRule("0")
#pprint(matches)
messages = lines[1].splitlines()
lengths = [len(message) for message in messages]
print(max(lengths))
count = 0
#for message in messages:
#    if(message in matches):
#        count+=1
#print(count)
    
    
#Part 2

match42 = evalRule("42")
match31 = evalRule("31")


def newMessageCheck(message):
    match31Check = False
    match31Count = 0
    match42Count = 0
    if(not message[:8] in match42 or not message[-8:] in match31):
        return False
    for x in range(0,len(message),8):
        chunk = message[x:x+8]
        if(not match31Check):             
            if(chunk in match42):
                match42Count+=1
            else:
                match31Check = True
        if(match31Check):
            if(chunk in match31):
                match31Count+=1
            if(not chunk in match31 or match31Count>=match42Count):
                return False
        
            
    
    return True

count = 0
for message in messages:
    if(newMessageCheck(message)):
        count+=1
print(count)
print(len(messages))
            
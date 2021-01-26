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

def evalRule(rule,lastRule,count):
    #print(rule)
    if(rule == lastRule):
        print(count)
        count += 1
    else:
        count = 1
    ruleNum = rule
    rule = rules[rule]
    if(rule[0][0] == '"b"'):
        return ["b"]
    if(rule[0][0] == '"a"'):
        return ["a"]
    vals = []
    for pipe in rule:
        if(count>=1 and (lastRule in pipe)):
            print(lastRule)
            continue
        pipeVals = []
        newPipeVals = []
        for ruleVal in pipe:
            pipeVals.append(evalRule(ruleVal,ruleNum,count))
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
matches = evalRule("0",None,0)
print(len(matches))
for match in matches:
    if(len(match) <= 35):
        pass
        #print(match)
    
#pprint(matches)
messages = lines[1].splitlines()
count = 0
for message in messages:
    if(message in matches):
        count+=1
print(count)
    
        
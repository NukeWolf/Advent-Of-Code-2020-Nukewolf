with open('input.txt','r') as f:
    raw = f.read().split('\n\n')

rules = {}
#Rules Handling
rawRules = raw[0].split("\n")
for rule in rawRules:
    rule.strip()
    key = rule.split(": ")[0]
    rawValues = rule.split(": ")[1]
    rawSets = rawValues.split(" or ")
    rules[key] = []
    for sett in rawSets:
        minMax = sett.split("-")
        rules[key].append((int(minMax[0]),int(minMax[1])))
#Nearby Ticket Setup
tickets = raw[2].strip().split("\n")[1:]
tickets = [[int(val) for val in ticket.split(",")] for ticket in tickets]

fullSet = []

for rule in rules:
    for minVal,maxVal in rules[rule]:
        fullSet.extend([x for x in range(minVal,maxVal+1)])
fullSet = list(set(fullSet))

#Part 1
error = 0
for ticket in tickets:
    for val in ticket:
        if(not val in fullSet):
            error+=val
print(error)

#Part 2

def checkTicket(ticket):
    for val in ticket:
        if(not val in fullSet):
            return False
    return True

filteredTickets = []
for ticket in tickets:
    if(checkTicket(ticket)):
        filteredTickets.append(ticket)
tickets = filteredTickets

maxRows = len(tickets)
maxCols = len(tickets[0])

potentialFields = [[] for x in range(maxCols)]

def checkCol(rule,col):
    for row in range(maxRows):
        val = tickets[row][col]
        inRange = False
        for minV,maxV in rules[rule]:
            if (minV <= val <= maxV):
                inRange = True
        if(not inRange):
            return False
    return True

for col in range(maxCols):
    for rule in rules:
        if (checkCol(rule,col)):
            potentialFields[col].append(rule)
for x in range(30):
    for fields in potentialFields:
        if (len(fields) == 1):
            remove = fields[0]
            for fields in potentialFields:
                if (len(fields) != 1):
                    try:
                        fields.remove(remove)
                    except:
                        pass
#My Ticket
myTicket = raw[1].split('\n')[1].split(",")
print(myTicket)
print(potentialFields)

count = 1
for index,field in enumerate(potentialFields):
    if('departure' in field[0]):
        count*= int(myTicket[index])
print(count)
        
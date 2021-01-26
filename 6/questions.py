with open('input.txt','r') as f:
    groups = f.read().split('\n\n')
    
#Part 1
count1 = 0
for group in groups:
    group = group.replace("\n","")
    s = set(group)
    count1+= len(s)
print(count1)

#Part 2
count2 = 0
for group in groups:
    people = group.strip().split("\n")
    key = people[0]
    print(people)
    for person in people:
        questions = person
        tempkey = ""
        for question in questions:
            if(question in key):
                tempkey +=question
        print(tempkey)
        key = tempkey
    count2 += len(key)
    print(len(key))
print(count2)
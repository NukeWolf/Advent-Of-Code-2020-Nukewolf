policies = []

with open('input.txt','r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        obj = {}
        parts = line.split(" ")
        
        minmax = parts[0].split("-")
        obj['min'] = int(minmax[0])
        obj['max'] = int(minmax[1])
        obj['char'] = parts[1][0]
        obj['pass'] = str(parts[2]).strip()
        policies.append(obj)
count1 = 0
count2 = 0
for obj in policies:
    if(obj['min'] <= obj['pass'].count(obj['char']) <= obj['max']):
        count1+=1
    try:
        if((obj['pass'][obj['min']-1] == obj['char']) != (obj['pass'][obj['max']-1] == obj['char'])):
            count2+=1
    except:
        print(obj)
print(count1,count2)




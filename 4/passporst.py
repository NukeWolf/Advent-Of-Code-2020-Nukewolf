import re

with open('input.txt','r') as f:
    passports = f.read().split('\n\n')
passports = [x.replace('\n',' ').strip() for x in passports]

print(len(passports))
#Part 1
valid = 0
for passport in passports:
    fields = passport.split(" ")
    if(len(fields) == 7):
        if(not ("cid" in passport)):
            valid += 1
    elif(len(fields) == 8):
        valid+=1
print(valid)
            
#Part 2
valid = 0
print(valid)
for passport in passports:
    fields = passport.split(" ")
    if(len(fields) <= 6):
        continue
    if(len(fields) == 7 and ("cid" in passport)):
        continue
    validTest = True
    for field in fields:
        key = field.split(":")[0]
        val = field.split(":")[1]
        if(key == 'byr'):
            validTest = validTest and (1920<= int(val) <= 2002)
        elif(key == 'iyr'):
            validTest = validTest and (2010<= int(val) <= 2020)
        elif(key == 'eyr'):
            validTest = validTest and (2020<= int(val) <= 2030)
        elif(key == 'hgt'):
            if("in" in val):
                validTest = validTest and (59<= int(val.replace("in","")) <= 76)
            else:
                validTest = validTest and (150<= int(val.replace("cm","")) <= 193)
        elif(key == 'hcl'):
            matches = re.search("^#[a-f0-9]{6}",val)
            validTest = validTest and (not matches == None)
        elif(key == 'ecl'):
            eyeColors = "amb blu brn gry grn hzl oth".split(" ")
            validTest = validTest and (val in eyeColors)
        elif(key == "pid"):
            validTest = validTest and (len(val) == 9)
    if(validTest):
        print(passport)
        valid +=1
print(valid)
            

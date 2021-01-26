import re
with open('input.txt','r') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]

product = []
for seat in lines:
    seat = re.sub("[FL]","0",seat)
    seat = re.sub("[BR]","1",seat)
    product.append(int(seat[0:7],2)*8 + int(seat[7:10],2))
print(sorted(product))
for x in range(802):
    if(not x in product):
        print(x)
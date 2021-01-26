f = open("input.txt",'r')
lines = [x for x in f]

for x in lines:
    for y in lines:
        x = int(x)
        y = int(y)
        if(x+y==2020):
            print(x*y)
            
for x in lines:
    for y in lines:
        for z in lines:
            x = int(x)
            y = int(y)
            z = int(z)
            if(x+y+z==2020):
                print(x*y*z)

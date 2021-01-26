
with open('input.txt','r') as f:
    lines = f.readlines()
lines = [x.strip()*90 for x in lines]

maxRows = len(lines)
maxCol = len(lines[0])
#Part 1
count1 = 0
col = 0

for row in range(0,maxRows,1):
    if(lines[row][col] == "#"):
        count1+=1
    col+=3
    
    
print(count1)

#Part 2
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
result = 1
for slope in slopes:
    count1 = 0
    col = 0
    for row in range(0,maxRows,slope[1]):
        if(lines[row][col] == "#"):
            count1+=1
        col+=slope[0]
    result*=count1
print(result)
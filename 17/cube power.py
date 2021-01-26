import itertools
import copy
import pprint
with open('input.txt','r') as f:
    lines = f.readlines()
grid = [[y for y in x.strip()]  for x in lines]
gridKey = {}

def setVal(row,col,z,val,grid):
    try:
        grid[row]
    except:
        grid[row] = {}
    try:
        grid[row][col]
    except:
        grid[row][col] = {}
    if (val == "#"):
        grid[row][col][z] = True
    else:
        grid[row][col][z] = False

for row,line in enumerate(grid):
    for col,val in enumerate(line):
        z = 0
        setVal(str(row),str(col),"0",val,gridKey)

pprint.pprint(gridKey)
newGrid = copy.deepcopy(gridKey)
for row in gridKey:
        for col in gridKey[row]:
            for z in gridKey[row][col]:
                row = int(row)
                col = int(col)
                z = int(z)
                for x,y,mz in itertools.product([-1,0,1],repeat=3):
                    if (x == 0 and y == 0 and mz == 0):
                        continue
                    testRow = str(row+x)
                    testCol = str(col+y)
                    testZ = str(z + mz)
                    try:
                        gridKey[testRow][testCol][testZ]
                    except:
                        setVal(testRow,testCol,testZ,".",newGrid)
                row = str(row)
                col = str(col)
gridKey = newGrid
pprint.pprint(gridKey)

count = 0
while count <= 5:
    newGrid = copy.deepcopy(gridKey)
    for row in gridKey:
        for col in gridKey[row]:
            for z in gridKey[row][col]:
                current = gridKey[row][col][z]
                row = int(row)
                col = int(col)
                z = int(z)
                occupied = 0
                for x,y,mz in itertools.product([-1,0,1],repeat=3):
                    if (x == 0 and y == 0 and mz == 0):
                        continue
                    testRow = str(row+x)
                    testCol = str(col+y)
                    testZ = str(z + mz)
                    try:
                        if(gridKey[testRow][testCol][testZ]):
                            occupied += 1
                    except:
                        setVal(testRow,testCol,testZ,".",newGrid)
                row = str(row)
                col = str(col)
                z = str(z)
                if (current and not(occupied == 2 or occupied == 3)):
                    setVal(row,col,z,".",newGrid)
                if(not current and occupied == 3):
                    setVal(row,col,z,"#",newGrid)
                
                    
    gridKey = newGrid

    count+=1

count = 0
for row in gridKey:
        for col in gridKey[row]:
            for z in gridKey[row][col]:
                if(gridKey[row][col][z]):
                    count += 1

print(count)
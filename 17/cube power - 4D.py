import itertools
import copy
import pprint
with open('input.txt','r') as f:
    lines = f.readlines()
grid = [[y for y in x.strip()]  for x in lines]
gridKey = {}

def setVal(row,col,z,w,val,grid):
    try:
        grid[row]
    except:
        grid[row] = {}
    try:
        grid[row][col]
    except:
        grid[row][col] = {}
    try:
        grid[row][col][z]
    except:
        grid[row][col][z] = {}
    if (val == "#"):
        grid[row][col][z][w] = True
    else:
        grid[row][col][z][w] = False

for row,line in enumerate(grid):
    for col,val in enumerate(line):
        z = 0
        setVal(str(row),str(col),"0","0",val,gridKey)

newGrid = copy.deepcopy(gridKey)
for row in gridKey:
        for col in gridKey[row]:
            for z in gridKey[row][col]:
                for w in gridKey[row][col][z]:
                    row = int(row)
                    col = int(col)
                    z = int(z)
                    w = int(w)
                    for x,y,mz,mw in itertools.product([-1,0,1],repeat=4):
                        if (x == 0 and y == 0 and mz == 0 and mw == 0):
                            continue
                        testRow = str(row+x)
                        testCol = str(col+y)
                        testZ = str(z + mz)
                        testW = str(w + mw)
                        try:
                            gridKey[testRow][testCol][testZ][testW]
                        except:
                            setVal(testRow,testCol,testZ,testW,".",newGrid)
                    row = str(row)
                    col = str(col)
                    z = str(z)
gridKey = newGrid
pprint.pprint(gridKey)

count = 0
while count <= 5:
    print(count)
    newGrid = copy.deepcopy(gridKey)
    for row in gridKey:
        for col in gridKey[row]:
            for z in gridKey[row][col]:
                for w in gridKey[row][col][z]:
                    current = gridKey[row][col][z][w]
                    row = int(row)
                    col = int(col)
                    z = int(z)
                    w = int(w)
                    occupied = 0
                    for x,y,mz,mw in itertools.product([-1,0,1],repeat=4):
                        if (x == 0 and y == 0 and mz == 0 and mw == 0):
                            continue
                        testRow = str(row+x)
                        testCol = str(col+y)
                        testZ = str(z + mz)
                        testW = str(w + mw)
                        try:
                            if(gridKey[testRow][testCol][testZ][testW]):
                                occupied += 1
                        except:
                            setVal(testRow,testCol,testZ,testW,".",newGrid)
                    row = str(row)
                    col = str(col)
                    z = str(z)
                    w = str(w)
                    if (current and not(occupied == 2 or occupied == 3)):
                        setVal(row,col,z,w,".",newGrid)
                    if(not current and occupied == 3):
                        setVal(row,col,z,w,"#",newGrid)
                
                    
    gridKey = newGrid
    count+=1

count = 0
for row in gridKey:
        for col in gridKey[row]:
            for z in gridKey[row][col]:
                for w in gridKey[row][col][z]:
                    if(gridKey[row][col][z][w]):
                        count += 1

print(count)
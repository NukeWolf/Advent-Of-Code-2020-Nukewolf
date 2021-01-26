import itertools
with open('input.txt','r') as f:
    lines = f.readlines()
grid = [[y for y in x.strip()]  for x in lines]

maxRows = len(grid)
maxCols = len(grid[0])

def printGrid(grid):
    grid = ["".join(x) for x in grid]
    print(grid)
    

change = True
while change:
    change = False
    #Issue- 2D array is not copying, deep copy is needed
    newGrid = [row[:] for row in grid]
    for row in range(0,maxRows):
        for col in range(0,maxCols):
            current = grid[row][col]
            if(current == "."):
                continue
            occupied = 0
            for x,y in itertools.product([-1,0,1],repeat=2):
                if (x == 0 and y == 0):
                    continue
                testRow = row+x
                testCol = col+y
                if(not (0 <= testRow < maxRows) or not (0 <= testCol < maxCols)):
                    continue
                if(grid[testRow][testCol] == "#"):
                    occupied +=1
            if(occupied == 0 and current == "L"):
                newGrid[row][col] = "#"
                change = True
            if(occupied >= 4 and current == "#"):
                newGrid[row][col] = "L"
                change = True
    #printGrid(grid)
    grid = newGrid
    
count = 0
for row in grid:
    for val in row:
        if(val == "#"):
            count+=1
print(count)


#Part 2
grid = [[y for y in x.strip()]  for x in lines]

occupiedGrid = [[[] for i in range(maxCols)] for j in range(maxRows)]
# Pre-Determines where each seat needs to check.
for row in range(0,maxRows):
    for col in range(0,maxCols):
        current = grid[row][col]
        if(current == "."):
            continue
        for mx,my in itertools.product([-1,0,1],repeat=2):
            if (mx == 0 and my == 0):
                continue
            index = 0
            while True:
                index+=1
                testRow = row + (mx*index)
                testCol = col + (my*index)
                if(not (0 <= testRow < maxRows) or not (0 <= testCol < maxCols)):
                    break
                if(grid[testRow][testCol] == "#" or grid[testRow][testCol] == "L"):
                    occupiedGrid[row][col].append((testRow,testCol))
                    break                
    
print(occupiedGrid[0][0])
iterations = 0
change = True
while change:
    iterations+=1
    if(iterations%100 == 0):
        print(iterations)
    change = False
    #Issue- 2D array is not copying, deep copy is needed
    newGrid = [row[:] for row in grid]
    for row in range(0,maxRows):
        for col in range(0,maxCols):
            current = grid[row][col]
            if(current == "."):
                continue
            occupied = 0
            for testRow,testCol in occupiedGrid[row][col]:
                if(grid[testRow][testCol] == "#"):
                    occupied +=1
            if(occupied == 0 and current == "L"):
                newGrid[row][col] = "#"
                change = True
            if(occupied >= 5 and current == "#"):
                newGrid[row][col] = "L"
                change = True
    #printGrid(grid)
    grid = newGrid
    #printGrid(grid)
    #input()
count = 0
for row in grid:
    for val in row:
        if(val == "#"):
            count+=1
print(count)


    
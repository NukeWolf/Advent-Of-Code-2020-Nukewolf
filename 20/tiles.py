from pprint import pprint
import itertools

with open('input.txt','r') as f:
    rawTiles = f.read().split('\n\n')[:-1]
def flipXImg(image):
    newImage = image.copy()
    newImage.reverse()
    return newImage
def flipYImg(image):
    newImage = []
    for row in image:
        newImage.append(row[::-1])
    return newImage
def rotateRightImg(image):
    newImage = [[val for val in row] for row in image]
    newImage = list(zip(*newImage[::-1]))
    newImage = [''.join(row) for row in newImage]
    return newImage


class Tile:
    def __init__(self,ID,tile):
        #Init
        self.id = ID.split(" ")[1][:4]
        self.image = tile
        #Node Properties
        self.N = None
        self.S = None
        self.W = None
        self.E = None
        self.resolved = False
        #Possible Images
        self.possibleImages = [self.image]
        self.possibleImages.append(flipXImg(self.image))
        self.possibleImages.append(flipYImg(self.image))
        self.possibleImages.append(flipYImg(flipXImg(self.image)))
        newImages = []
        for image in self.possibleImages:
            newImages.append(rotateRightImg(image))
        self.possibleImages.extend(newImages)
        
        #Only Using Borders
        self.processTile(tile)
        self.possibleTiles = [self.original]
        self.possibleTiles.append(self.flipX(self.original))
        self.possibleTiles.append(self.flipY(self.original))
        self.possibleTiles.append(self.flipY(self.flipX(self.original)))
        newTiles = []
        for tile in self.possibleTiles:
            newTiles.append(self.rotateRight(tile))
        self.possibleTiles.extend(newTiles)
    def processTile(self,tile):
        tileSides = {}
        tileSides["N"] = tile[0]
        tileSides["S"] = tile[-1]
        tileSides["W"] = ""
        tileSides["E"] = ""
        for row in tile:
            tileSides["W"] += row[0]
            tileSides["E"] += row[-1]
        self.original = tileSides
    def flipX(self,tileSides):
        newTileSides = {}
        newTileSides["S"] = tileSides["N"]
        newTileSides["N"] = tileSides["S"]
        newTileSides["E"] = tileSides["E"][::-1]
        newTileSides["W"] = tileSides["W"][::-1]
        return newTileSides
    def flipY(self,tileSides):
        newTileSides = {}
        newTileSides["E"] = tileSides["W"]
        newTileSides["W"] = tileSides["E"]
        newTileSides["N"] = tileSides["N"][::-1]
        newTileSides["S"] = tileSides["S"][::-1]
        return newTileSides
    def rotateRight(self,tileSides):
        newTileSides = {}
        newTileSides["E"] = tileSides["N"]
        newTileSides["W"] = tileSides["S"]
        newTileSides["N"] = tileSides["W"][::-1]
        newTileSides["S"] = tileSides["E"][::-1]
        return newTileSides
    def checkTile(self,tile,direction):
        comparisonVal = tile.original[direction]
        #Flip the direction, because the North side of the tile connects with the
        #South side of another tile
        if(direction == "N"):
            direction = "S"
        elif(direction == "S"):
            direction = "N"
        elif(direction == "E"):
            direction = "W"
        elif(direction == "W"):
            direction = "E"
        #Check if any possible tiles have this configuration.
        for index,tileCheck in enumerate(self.possibleTiles):
            if(tileCheck[direction] == comparisonVal):
                #Set orientation
                self.original = tileCheck
                self.image = self.possibleImages[index]
                
                return True
        return False
    def setNode(self,direction,tile):
        if(direction == "N"):
            self.N = tile
        elif(direction == "S"):
            self.S = tile
        elif(direction == "E"):
            self.E = tile
        elif(direction == "W"):
            self.W = tile
    def getNodes(self):
        nodes = []
        nodes.append(self.N)
        nodes.append(self.E)
        nodes.append(self.S)
        nodes.append(self.W)
        return nodes
    def getFinalImage(self):
        newImage = self.image.copy()
        newImage = newImage[1:]
        newImage = newImage[:-1]
        newImage = [row[:-1] for row in newImage]
        newImage = [row[1:] for row in newImage]
        return newImage
tiles = []

for rawTile in rawTiles:
    vals = rawTile.split("\n")
    tiles.append(Tile(vals[0],vals[1:]))
#Part 2
#Resolve tile node pointer by recursion, along with final orientation of the tile
def resolveTile(tile):
    for side in tile.original:
        collisions = 0
        for tileCheck in tiles:
            if (tile.id == tileCheck.id):
                continue
            if(tileCheck.checkTile(tile,side)):
                tile.setNode(side,tileCheck)
                collisions += 1
        if(collisions == 2):
            print("COLLISION")
    tile.resolved = True
    nodes = tile.getNodes()
    for node in nodes:
        if (node == None or node.resolved):
            continue
        resolveTile(node)
resolveTile(tiles[0])        

#Locate Header Tile
topleft = None
for tile in tiles:
    if(tile.N == None and tile.W == None):
        topleft = tile

#Recursively Parse through Image into 2D array
finalPic = []
global row
row = []
def parsePicture(tile):
    global row
    row.append(tile.getFinalImage())
    if(tile.E != None):
        parsePicture(tile.E)
    if(tile.W == None):
        finalPic.append(row.copy())
        row = []
    if(tile.S != None and tile.W == None):
        parsePicture(tile.S)
parsePicture(topleft)

#Parse 2d array of images into one image 2d array
finalParse = []
for row in finalPic:
    for height in range(len(row[0])):
        line = ''
        for col in row:
            line += col[height]
        finalParse.append(line)
pprint(finalPic[0][0])
pprint(finalPic[0][1])
pprint(finalPic[1][1])
pprint(finalParse)


#Process Sea Monster into array of tuples to check relative to checking point.
with open('sea_monster.txt','r') as f:
    array = f.read().split('\n')
seaMonsterCheck = []
for x,row in enumerate(array):
    for y,val in enumerate(row):
        if(val == "#"):
            seaMonsterCheck.append((x,y))
seaMonsterHeight = len(array)
seaMonsterWidth = len(array[0])
pictureHeight = len(finalParse)
pictureWidth = len(finalParse[0])
pprint(seaMonsterCheck)

def checkCoords(x,y,image):
    for checkx,checky in seaMonsterCheck:
        if(image[x+checkx][y+checky] != "#"):
            return False
    return True

#Possible orientatinos of the final parse
possibleImages = [finalParse]
possibleImages.append(flipXImg(finalParse))
possibleImages.append(flipYImg(finalParse))
possibleImages.append(flipYImg(flipXImg(finalParse)))
newImages = []
for image in possibleImages:
    newImages.append(rotateRightImg(image))
possibleImages.extend(newImages)


for image in possibleImages:
    monsterCount = 0
    for x,y in itertools.product(range(pictureHeight-seaMonsterHeight+1),range(pictureWidth-seaMonsterWidth+1)):
        if(checkCoords(x,y,image)):
            monsterCount += 1
    print(monsterCount)

count = 0
for row in finalParse:
    for val in row:
        if(val == "#"):
            count+=1
print(count)
#pprint(possibleImages)
#Part 1
#total = 1
#for tile in tiles:
#    possibleSides = 0
#    for side in tile.original:
#        for tileCheck in tiles:
#            if (tile.id == tileCheck.id):
#                continue
#            if(tileCheck.checkTile(tile,side)):
#                possibleSides +=1
#    if(possibleSides == 2):
#        total*=int(tile.id)
#print(total)

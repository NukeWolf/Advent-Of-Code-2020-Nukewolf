with open('input.txt','r') as f:
    rawDecks = f.read().split('\n\n')

#Part 1

deck1 = [int(x) for x in rawDecks[0].strip().split('\n')[1:]]
deck2 = [int(x) for x in rawDecks[1].strip().split('\n')[1:]]

while(not (len(deck1) == 0 or len(deck2) == 0)):
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)
    newCards = [card1,card2]
    newCards.sort(reverse=True)
    if(card1>card2):
        deck1.extend(newCards)
    else:
        deck2.extend(newCards)
print(deck1)
print(deck2)

count = 0
for ind,x in enumerate(reversed(deck2)):
    count += x*(ind+1)
print(count)


#Part 2
deck1 = [int(x) for x in rawDecks[0].strip().split('\n')[1:]]
deck2 = [int(x) for x in rawDecks[1].strip().split('\n')[1:]]

def areEqual(arr1,arr2):
    
    # If lengths of array are not
    # equal means array are not equal
    if (len(arr1) != len(arr2)):
        return False
    # Linearly compare elements
    for i in range(len(arr1)):
        if (arr1[i] != arr2[i]):
            return False
 
    # If all elements were same.
    return True
 

realGameStates = []
#Returns True if Player 1 (deck1) won
def resolveGame(deck1,deck2):
    for decks in realGameStates:
        checkDeck1,checkDeck2 = decks['decks']
        if(areEqual(checkDeck1,deck1) and areEqual(checkDeck2,deck2)):
            #print('saved time')
            return decks['result']
    state = {}
    state['decks'] = (deck1.copy(),deck2.copy())
    gameStates = []
    while(not (len(deck1) == 0 or len(deck2) == 0)):
        for checkDeck1,checkDeck2 in gameStates:
            if(areEqual(checkDeck1,deck1) and areEqual(checkDeck2,deck2)):
                state['result'] = True
                realGameStates.append(state)
                return True
        gameStates.append((deck1.copy(),deck2.copy()))
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if(len(deck1) >= card1 and len(deck2) >= card2):
            if(resolveGame(deck1.copy()[:card1],deck2.copy()[:card2])):
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
        else:
            newCards = [card1,card2]
            newCards.sort(reverse=True)
            if(card1>card2):
                deck1.extend(newCards)
            else:
                deck2.extend(newCards)
        if(deck1==first):
            print(deck1,deck2)
        #input()
    state['result'] = (len(deck1) != 0)
    realGameStates.append(state)
    return (len(deck1) != 0)
first = deck1

#resolveGame(deck1,deck2)
print(deck1)
print(deck2)
finalArr = [34, 4, 15, 13, 29, 5, 33, 26, 50, 39, 45, 6, 32, 12, 30, 1, 47, 19, 41, 8, 18, 9, 10, 2, 49, 16, 28, 7, 43, 38, 21, 20, 48, 37, 25, 14, 22, 3, 42, 17, 27, 11, 46, 36, 44, 24, 40, 31, 35, 23]
count = 0
for ind,x in enumerate(reversed(finalArr)):
    count += x*(ind+1)
print(count)
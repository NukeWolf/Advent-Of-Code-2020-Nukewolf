with open('input.txt','r') as f:
    lines = f.read().strip().split('\n')
allergenList = []
for food in lines:
    foods = {}
    split = food.split(' (contains ')
    foods['ingredients'] = split[0].split(' ')
    allergy = split[1][:-1].split(', ')
    foods['allergens'] = allergy
    allergenList.append(foods)

allergies = []
for food in allergenList:
    for allergen in food['allergens']:
        allergies.append(allergen)
allergies = list(set(allergies))
print(allergies)


initialList = {}
for allergy in allergies:
    possibleIngredients = None
    for food in allergenList:
        if (allergy in food['allergens']):
            if(possibleIngredients == None):
                possibleIngredients = food['ingredients']
                continue
            newPossibleList = []
            for ingredient in possibleIngredients:
                if ingredient in food['ingredients']:
                    newPossibleList.append(ingredient)
            possibleIngredients = newPossibleList
    initialList[allergy] = possibleIngredients
print(initialList)


for x in range(30):
    for allergen in initialList:
        if (len(initialList[allergen]) == 1):
            remove = initialList[allergen][0]
            for allergen in initialList:
                if (len(initialList[allergen]) != 1):
                    try:
                        initialList[allergen].remove(remove)
                    except:
                        pass

combinedAllergens = [initialList[allergen][0] for allergen in initialList]
print(combinedAllergens)

count = 0
for food in allergenList:
    for ingredient in food['ingredients']:
        if (not ingredient in combinedAllergens):
            count+=1
print(count)
sortedAllergensByEnglishName = [initialList[allergen][0] for allergen in sorted(initialList)]

print(','.join(sortedAllergensByEnglishName))
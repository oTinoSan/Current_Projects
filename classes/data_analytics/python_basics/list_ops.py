myFlower1 = input()
myFlower2 = input()
myFlower3 = input()

yourFlower1 = input()
yourFlower2 = input()

theirFlower = input()

# Define myList containing myFlower1, myFlower2, and myFlower3 in that order
myList = [myFlower1, myFlower2, myFlower3]
print(myList)

# Define yourList containing yourFlower1 and yourFlower2 in that order
yourList = [yourFlower1, yourFlower2]
print(yourList)

# Define ourList by concatenating myList and yourList
ourList = myList + yourList
print(ourList)

# Append theirFlower to the end of ourList
ourList.append(theirFlower)
print(ourList)

# Replace myFlower2 in ourList with theirFlower
ourList[1] = theirFlower
print(ourList)

# Remove the third element of ourList
ourList.pop(2)
print(ourList)

"""
Example input:
rose
peony
lily
rose
daisy
aster

Example output:
['rose', 'peony', 'lily']
['rose', 'daisy']
['rose', 'peony', 'lily', 'rose', 'daisy']
['rose', 'peony', 'lily', 'rose', 'daisy', 'aster']
['rose', 'aster', 'lily', 'rose', 'daisy', 'aster']
['rose', 'aster', 'rose', 'daisy', 'aster']
"""
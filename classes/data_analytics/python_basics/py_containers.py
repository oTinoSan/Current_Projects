################
# named tuples #
################

# Import the namedtuple class
from collections import namedtuple

# Create named tuple type Species with field names 'name', 'order', 'length', and 'legs'
Species = namedtuple('Species', ['name', 'order', 'length', 'legs'])

# Create an object of type Species with name = 'robin', order = 'passeriformes', length = 0.25, and legs = 2
robin = Species('robin', 'passeriformes', 0.25, 2)

# Print the legs element of the robin object
print(robin.legs)
print(robin)

##################
# lists and sets #
##################

# Create a list
practiceList = [34, 8, 113]

# Create the set newSet
newSet = {34, 29}

# Convert practiceList to a set
exampleSet = set(practiceList)
print(sorted(exampleSet))

# Remove 8 from the set 
exampleSet.remove(8)
print(sorted(exampleSet))

# Find the intersection of exampleSet and newSet
exampleSetIntersection = exampleSet.intersection(newSet)
print(sorted(exampleSetIntersection))

##########################
# modifying dictionaries #
##########################

# Create a dictionary with indexes 'robin', 'hornet', and 'tuna', and values 0.25, 0.05, and 1
exampleDict = {'robin' : 0.25, 'hornet' : 0.05, 'tuna' : 1}
print(exampleDict)

# Modify the value of the element with key 'tuna' to 1.03
exampleDict['tuna'] = 1.03
print(exampleDict)

# Remove element with key 'hornet'
del exampleDict['hornet']
print(exampleDict)
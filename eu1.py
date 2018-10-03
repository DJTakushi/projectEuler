myList = []
primaryCounter=0
product=0
while (primaryCounter<1000):
	myList.append(primaryCounter)
	primaryCounter = primaryCounter + 3

primaryCounter = 0
secondaryCounter=0
while (primaryCounter<1000):
	if primaryCounter % 3 != 0:
		myList.append(primaryCounter)
	primaryCounter = primaryCounter + 5

for item in myList:
	product = product + item
	#print("item = ", item, ", product = ",product)

print("product = ", product)

myList2 = []
primaryCounter = 0
product2 = 0
while (primaryCounter<1000):
	if (primaryCounter % 3 == 0) or (primaryCounter % 5 == 0):
		product2 = product2 + primaryCounter
	primaryCounter = primaryCounter + 1

print("product2 = ", product2)
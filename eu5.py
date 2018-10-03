#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

primeList = [2]

def getBiggest(input):
	product = 1
	for num in range(1,input+1):
		product = product * num
		#print("times ", num, " ->", product) #debugging
	return product

def TESTgetBiggest(input):
	print("getBiggest(",input,") = ", getBiggest(input))

def primecheck(input): #requires all lower prime numbers being tested earlier
	if input in primeList:	#already listed?
		return input
	for prime in primeList: #divisible by known prime?
		if input % prime == 0: #not prime
			return prime
	#divisible by unknown prime (try dividing by smaller stuff, 
	if(input != 1):	#OMG NEW PRIME!!!
		primeList.append(input)
		return input
	else:#was only divisible by itself
		return 0

def getPrimeList(inputList):#takes ASCENDING LIST
	returnList = []
	for num in inputList:
		if primecheck(num) == num:
			returnList.append(num)
	return returnList

def TESTgetPrimeList(length):
	inputList = (range(1,length+1))
	print(getPrimeList(inputList))

def getProduct(inputList):
	product = 1
	for num in inputList:
		product = product * num
	return product

TESTgetBiggest(10)
TESTgetBiggest(20)
TESTgetPrimeList(20)
myProduct = getProduct(getPrimeList((range(1,20+1))))
iterations = getBiggest(20)
print(iterations/myProduct)
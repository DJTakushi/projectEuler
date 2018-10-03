import math
primeList = [2]

def primecheck(input): #requires all lower prime numbers being tested earlier
	#already listed?
	if input in primeList:
		return input
	#divisible by known prime?
	for prime in primeList:
		if input % prime == 0: #not prime
			return prime
	#divisible by unknown prime (try dividing by smaller stuff, b
	if(input != 1):	#OMG NEW PRIME!!!
		primeList.append(input)
		#print("!",input)
		return input
	else:
		return 0

def LpPF(input):
	divisor = 1
	LpPFlist = []
	cutoff = math.sqrt(input)
	while divisor < cutoff:
		if (primecheck(divisor) == divisor):
			print("checking division by ", divisor)
			if input % divisor == 0:
				LpPFlist.append(divisor)
				print("added ", divisor)
		divisor = divisor + 2
	print(LpPFlist)

#LpPF(13195)
LpPF(600851475143) #returns 71, 839, 1471, 6857, but it takes too long
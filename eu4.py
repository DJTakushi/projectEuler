#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def solve():
	divisableBy = 0
	for num in (list(reversed(range(biggestProduct(3))))):
		if isPalindrome(num) == 1:
			divisableBy = factorableUnderDigits(num, 3)
			if divisableBy != 0:
				print("num = ", num, " divisable_by", divisableBy)
				return num
	print("EPIC FAILURE")

def isPalindrome(input): #checks if input is palindrome
	inStr = str(input)
	for num in range(len(inStr)):
		if inStr[num] != inStr[len(inStr)-1-num]:
			return 0
	return 1
	#biggestChar = inStr[len(inStr)-1]
	#smallestChar = inStr[0]
	#if biggestChar == smallestChar:
	#	return 1
	#else:
	#	return 0

def factorableUnderDigits(subject, digits):
	bf = biggestFactor(digits)
	for factorA in (list(reversed(range(bf)))):
		if subject % factorA == 0:
			return factorA
		if subject / factorA > bf:
			return 0
	return 0

def biggestFactor(digits):
	BFN = 0
	for num in range(digits):
		BFN = 9*(10**(num)) + BFN
	return BFN

def biggestProduct(digits):
	return(biggestFactor(digits)**2)

def TESTbiggestFactor():
	for num in range(1,6):
		print("digits = ", num, ", biggestFactor = ", biggestFactor(num))

def TESTisPalindrome():
	for num in (list(reversed(range(1000)))):
		if(isPalindrome(num)):
			print(num)

def TESTfactorableUnderDigits(subject, digits):
	print("subject = ",subject,"digits = ",digits,factorableUnderDigits(subject,digits))

def TESTbiggestProduct(digits):
	print("digits = ", digits, " biggestProduct = ", biggestProduct(digits))


#TESTbiggestFactor()
#TESTisPalindrome()
#TESTfactorableUnderDigits(99,2)
#TESTfactorableUnderDigits(111,2)
#TESTfactorableUnderDigits(99999,3)
#TESTbiggestProduct(1)
#TESTbiggestProduct(2)
#TESTbiggestProduct(3)
#TESTbiggestProduct(4)
#TESTbiggestProduct(5)
#TESTbiggestProduct(6)
print (solve())


#print(list(reversed(range(10))))
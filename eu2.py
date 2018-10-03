f1=1
f2=2
fsum = 0
while f2 <= 4000000:
	if (f2 %2 ==0):
		fsum = fsum + f2
		print(fsum)
	temp = f2
	f2 = f1 + f2
	f1 = temp

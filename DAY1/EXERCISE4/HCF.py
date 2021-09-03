try:
	a,b=[int(x) for x in input("Enter 2 space separated numbers : ").split()]
	HCF=1
	for i in range(min(a,b),1,-1):
		if a%i==0 and b%i==0:
			HCF=i
			break
	print(HCF)
except Exception as e:
	print("The following Exception has occured : ")
	print(e)
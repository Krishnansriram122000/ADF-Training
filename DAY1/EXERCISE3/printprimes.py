import time
try:
	primelist=[2]
	upperbound=100
	for i in range(3,upperbound):
		for j in range(2,i):
			if i%j==0:
				break
		else:
			primelist.append(i)
	for i in primelist:
		print(i)
		time.sleep(5)
except Exception as e:
	print("The following Exception has occured : ")
	print(e)

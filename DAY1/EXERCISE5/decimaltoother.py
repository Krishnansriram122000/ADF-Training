def dectox(num,boh):
	try:
		hexlist=['A','B','C','D','E','F']
		stri=''
		while(num>0):
			r=num%boh
			num=num//boh
			if r<10:
				stri+=str(r)
			else:
				stri+=hexlist[r-10]
		print(stri[::-1])
		return stri[::-1]
	except Exception as e:
		print("The following Exception has occured : ")
		print(e)

a=int(input())
binary=dectox(a,2)
octal=dectox(a,8)
hexa=dectox(a,16)

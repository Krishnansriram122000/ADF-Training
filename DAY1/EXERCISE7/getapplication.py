try:
	name=input("Name : ")
	age=int(input('age : '))
	gender=input('gender : ')
	salary=int(input('salary : '))
	state=input('state : ')
	city=input('city : ')
except Exception as e:
	print("The following Exception has occured : ")
	print(e)

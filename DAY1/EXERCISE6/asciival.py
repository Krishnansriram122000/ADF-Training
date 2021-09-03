try:
	char=input("Enter a character: ")
	if len(char)!=1:
		print("Please Enter a single character")
		exit()
	print("The ascii  vallue of the character is " + str(ord(char))) 
except Exception as e:
	print("The following Exception has occured : ")
	print(e)
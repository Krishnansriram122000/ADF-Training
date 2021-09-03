try:
	infile_lines=open('Book1.csv').read().split('\n')

	headings=infile_lines[0].split(',')
	listofrecords=[]
	for i,line in enumerate(infile_lines[1:len(infile_lines)-1]):
		newdict={}
		newline=line.split(',')
		for j,heading in enumerate(headings):
			try:
				newdict[headings[j]]=newline[j]
			except IndexError:
				pass
		listofrecords.append(newdict)

	for record in listofrecords:
		print(record)
except Exception as e:
	print("The following Exception has occured : ")
	print(e)
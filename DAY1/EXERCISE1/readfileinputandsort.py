try:
	words=open('prog1in.txt','r+').read().split()
	words=[x for x in set(words)]
	word_lenths=[len(word) for word in words]
	#words=sorted(words,key=len)
	for i in range(len(words)-1):
		for j in range(len(words)-i-1):
			if word_lenths[j]>word_lenths[j+1]:
				word_lenths[j],word_lenths[j+1]=word_lenths[j+1],word_lenths[j]
				words[j],words[j+1]=words[j+1],words[j]

	outpufile=open('prog1out.txt','w+')
	for i in words:
		outpufile.write(i+"  :  "+str(len(i))+"\n")
	print(words)
except Exception as e:
	print("The following Exception has occured : ")
	print(e)

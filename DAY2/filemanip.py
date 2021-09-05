import sys
import os

infile=open(sys.argv[1],'r+').read()
wordsinfile=infile.split()
count_to=0
count_ing=0
for word in wordsinfile:
	count_to+= 1 if word[:2]=="to" else 0
for word in wordsinfile:
	count_ing+= 1 if word[-3:]=="ing" else 0

print("Words that starts with 'to' : "+str(count_to))
print("Words that end with 'ing' : "+str(count_ing))

countdic={}
maxcount=0
maxword=''
for word in wordsinfile:
	if word in countdic:
		countdic[word]+=1
	else:
		countdic[word]=1
	if countdic[word]>maxcount:
		maxcount=countdic[word]
		maxword=word
print("The words that appears maximum is: "+maxword+".\nAnd its count is: "+str(maxcount))

#print(countdic)
print("The palindromes present in the list are: ")
for word in wordsinfile:
	if len(word)!=1:
		word1=word[::-1]
		if word==word1:
			print(word)

uniqlst=[]
for word in wordsinfile:
	if word not in uniqlst:
		uniqlst.append(word)
print("The unique words in the file are: ")
print("\t".join(uniqlst))


fdictionary={}
for i,word in enumerate(wordsinfile):
	fdictionary[i+1]=word

print("The dictionary with word number is: ")
print(fdictionary)

outfilename='outfile'
outfileextension='.txt'
counterval=1
while os.path.isfile(outfilename+outfileextension):
	outfilename='outfile'+str(counterval)
	counterval+=1

outfile=open(outfilename+outfileextension,'w+')
outfile.write("The input file contents separated by vowels: \n")
stri=''
vowel=['a','e','i','o','u','A','E','I','O','U']
for i in infile:
	if i in vowel:
		outfile.write(stri+" ")
		stri=''
	else:
		stri+=i

outfile.write("\n\n\n")

outfile.write("Each word's third letter capitalised: \n")
stri=''
for word in wordsinfile:
	if len(word)>2:
		val=word
		val=val[:2]+val[2].upper()+val[3:]
		stri+=val+" "
	else:
		stri+=word+" "

outfile.write(stri+"\n\n\n")

outfile.write("Every fifth word capitalised: \n")
stri=''
for i,word in enumerate(wordsinfile):
	if (i+1)%5==0:
		stri+=word.upper()+" "
	else:
		stri+=word+" "
	

outfile.write(stri+"\n\n\n")

outfile.write("Spaces replaced by '-' : \n")
stri=''
for i in infile:
	if i==' ':
		stri+='-'
	else:
		stri+=i

outfile.write(stri+"\n\n\n")

outfile.write("New line replaced by ';' : \n")
stri=''
for i in infile:
	if i=="\n":
		stri+=';'
	else:
		stri+=i

outfile.write(stri+"\n")
outfile.close()









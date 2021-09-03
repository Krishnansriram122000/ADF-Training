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
print(maxword,maxcount)

for word in wordsinfile:
	mid=len(word)
	if mid%2==0 and word[:mid]==word[mid:]:
		print(word)
	elif mid%2==1 and word[:mid]==word[mid+1:]:
		print(word)

uniqlst=[]

for word in wordsinfile:
	if word not in uniqlst:
		uniqlst.append(word)
print(uniqlst)

"""

word dict f in q

"""
fdictionary={}
for i,word in enumerate(wordsinfile):
	fdictionary[i+1]=word


stri=''
vowel=['a','e','i','o','u','A','E','I','O','U']
outfile=open('outfile.txt','w+')
for i in infile:
	if i in vowel:
		outfile.write(stri+"\t")
		stri=''
	else:
		stri+=i

for word in wordsinfile:
	if len(word)>2:
		word[2].upper()

for i,word in enumerate(wordsinfile):
	if i==5:
		word.upper()

stri=''
for i in infile:
	if i==' ':
		stri+='-'
	else:
		stri+=i

stri=''
for i in infile:
	if i=="\n":
		stri+=';'
	else:
		stri+=i

outfilename='outfile'
counterval=0
while not os.path.isfile(outfilename+'.txt'):
	outfilename+=counterval
	counterval+=1

fileout=open(outfilename,'w+')
"""

output with unique file name


"""








import logging
import sys

class fileio:
	def __init__(self,filename):
		self.__filename=filename
		self.__filedata=''
		self.__filehandler=None
		logging.basicConfig(filename="log.txt",
							filemode='a+',
							format='%(asctime)s %(levelname)s - %(message)s',
							datefmt='%Y-%m-%d %H:%M:%S')
		contents=open('external.config').read()
		self.__config=eval(contents)
		logging.warning(self.__config["username"]+" has accessed the file "+self.__filename)

	def readf(self):
		self.__filehandler =open(self.__filename,'r+')
		self.__filedata=self.__filehandler.read()
		self.__filehandler.close()
		self.__filehandler=None
		logging.warning('Read data from Input file')
		return self.__filedata

	def writef(self,data_to_be_written):
		self.__filehandler =open("outfile.txt",'a+')
		self.__filehandler.write(data_to_be_written)
		self.__filehandler.close()
		self.__filehandler=None
		logging.warning('Written data to Output file')
		return 200

	def readout(self):
		self.__filehandler =open("outfile.txt",'r+')
		self.__filedata=self.__filehandler.read()
		self.__filehandler.close()
		self.__filehandler=None
		logging.warning('Read data from Output file')
		return self.__filedata

	def clearoutfile(self):
		self.__filehandler=open("outfile.txt",'w')
		self.__filehandler.write(" ")
		self.__filehandler.close()
		logging.warning('Empty Output file')
		return 200

class fileoperations(fileio):
	def __init__(self,filename):
		super().__init__(filename)

	def contentsofinputfile(self):
		print(self.readf())

	def contentsofoutfile(self):
		print(self.readout())

	def splitonvowels(self):
		self.clearoutfile()
		infile=self.readf()
		mainstring=''
		stri=''
		vowel=['a','e','i','o','u','A','E','I','O','U']
		for i in infile:
			if i in vowel:
				mainstring+=stri+" "
				stri=''
			else:
				stri+=i
		mainstring+=stri
		self.writef(mainstring +"\n")		
		print(self.contentsofoutfile())

	def thirdlettercapitalise(self):
		self.clearoutfile()
		wordsinfile=self.readf().split()
		stri=''
		for word in wordsinfile:
			if len(word)>2:
				val=word
				val=val[:2]+val[2].upper()+val[3:]
				stri+=val+" "
			else:
				stri+=word+" "
		self.writef(stri+"\n\n\n")
		print(self.contentsofoutfile())

	def fifthwordcap(self):
		self.clearoutfile()
		wordsinfile=self.readf().split()
		stri=''
		for i,word in enumerate(wordsinfile):
			if (i+1)%5==0:
				stri+=word.upper()+" "
			else:
				stri+=word+" "
		self.writef("\n"+stri+"\n\n\n")
		print(self.contentsofoutfile())

fileop=fileoperations(sys.argv[1])
fileop.contentsofinputfile()
fileop.splitonvowels()
fileop.thirdlettercapitalise()
fileop.fifthwordcap()









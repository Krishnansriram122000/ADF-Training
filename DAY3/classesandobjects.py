"""
The Program to read input from file and manipulate strings and write it to output.
"""

import logging
import sys


class FileIo:
    """
    class to read and write to files
    """

    def __init__(self, filename):
        self.__filename = filename
        self.__filedata = ''
        self.__filehandler = None
        logging.basicConfig(filename="log.txt",
                            filemode='a+',
                            format='%(asctime)s %(levelname)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            level=1)
        with open('external.config', encoding='utf-8') as input_file:
            contents = input_file.read()
            self.__config = eval(contents)
            logging.info(self.__config["username"] + " has accessed the file " + self.__filename)
            input_file.close()

    def readf(self):
        """
        Read input file
        :return: inputfile contents as string
        """
        with open(self.__filename, 'r+', encoding='utf-8') as input_file:
            self.__filehandler = input_file
            self.__filedata = self.__filehandler.read()
            self.__filehandler.close()
            self.__filehandler = None
            logging.info('Read data from Input file')
            input_file.close()
        return self.__filedata

    def writef(self, data_to_be_written):
        """
        Write the parsed data to output file
        :param data_to_be_written: data to be written into the file
        :return: True
        """
        with open("outfile.txt", 'a+', encoding='utf-8') as input_file:
            self.__filehandler = input_file
            self.__filehandler.write(data_to_be_written)
            self.__filehandler.close()
            self.__filehandler = None
            logging.info('Written data to Output file')
            input_file.close()
        return True

    def readout(self):
        """
        Reads output file
        :return: Output file contents as string
        """
        with open("outfile.txt", 'r+', encoding='utf-8') as input_file:
            self.__filehandler = input_file
            self.__filedata = self.__filehandler.read()
            self.__filehandler.close()
            self.__filehandler = None
            logging.info('Read data from Output file')
            input_file.close()
        return self.__filedata

    def clearoutfile(self):
        """
        Clears the output file
        :return: True
        """
        with open("outfile.txt", 'w', encoding='utf-8') as input_file:
            self.__filehandler = input_file
            self.__filehandler.write(" ")
            self.__filehandler.close()
            logging.info('Empty Output file')
            input_file.close()
        return True


class FileOperations(FileIo):
    """
    Class to do operations on file
    Inherited from FileIo class
    """
    def __init__(self, filename):
        FileIo.__init__(self, filename)

    def contentsofinputfile(self):
        """
        Print contents of input file
        :return: True
        """
        print(self.readf())
        return True

    def contentsofoutfile(self):
        """
        Print contents of output file
        :return: True
        """
        print(self.readout())
        return True

    def splitonvowels(self):
        """
        Split words based on vowels
        :return: True
        """
        self.clearoutfile()
        infile = self.readf()
        mainstring = ''
        stri = ''
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in infile:
            if i in vowel:
                mainstring += stri + " "
                stri = ''
            else:
                stri += i
        mainstring += stri
        self.writef(mainstring + "\n")
        print(self.contentsofoutfile())
        return True

    def thirdlettercapitalise(self):
        """
        Capitalises third letter of every word
        :return: True
        """
        self.clearoutfile()
        wordsinfile = self.readf().split()
        stri = ''
        for word in wordsinfile:
            if len(word) > 2:
                val = word
                val = val[:2] + val[2].upper() + val[3:]
                stri += val + " "
            else:
                stri += word + " "
        self.writef(stri + "\n\n\n")
        print(self.contentsofoutfile())
        return True

    def fifthwordcap(self):
        """
        Capitalise every 5th word
        :return: True
        """
        self.clearoutfile()
        wordsinfile = self.readf().split()
        stri = ''
        for i, word in enumerate(wordsinfile):
            if (i + 1) % 5 == 0:
                stri += word.upper() + " "
            else:
                stri += word + " "
        self.writef("\n" + stri + "\n\n\n")
        print(self.contentsofoutfile())
        return True


if __name__ == "__main__":
    FileOperation = FileOperations(sys.argv[1])
    FileOperation.contentsofinputfile()
    FileOperation.splitonvowels()
    FileOperation.thirdlettercapitalise()
    FileOperation.fifthwordcap()

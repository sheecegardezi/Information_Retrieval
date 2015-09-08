'''
Created on Aug 30, 2015

@author: Sheece Gardezi
It read the excel file contain text from quran. It updates a lexicon list with new words. Adds the surah no, ayat no and juz number, it has apperaded in.
It search all the three translations by 
'''
from openpyxl import load_workbook
from openpyxl import Workbook
import pickle
import time

QURAN_FILE_NAME="pathDir"

#read data from the translations
quran_workbook = load_workbook(filename = QURAN_FILE_NAME)
worksheet_translation= { quran_workbook['TranslationByYusuf'],quran_workbook['TranslationByPicktall'],quran_workbook['TranslationByShaakir']}

quran_list=[]
lexicon_list=[]



def get_data():

	juz_no=0
	saurate_no=1
	ayat_no=2
	ayat=3
	
	#reading data into a lsit
	for translation in worksheet_translation:
		for row in translation.rows:
			quran_list.append((row[juz_no].value,row[saurate_no].value,row[ayat_no].value,row[ayat].value))
    #writing list to a file 
	with open('quran.txt', 'wb') as f:
		pickle.dump(quran_list, f)
	
def main():
	#read list from file
	with open('quran.txt', 'rb') as file:
		quran_list = pickle.load(file)
	
start_time = time.clock()
main()
print time.clock() - start_time, "seconds"

#print( datafile)
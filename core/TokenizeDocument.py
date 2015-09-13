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
from future.backports.misc import count
import unicodedata



def get_data():

    #writing list to a file 
	with open('quran.txt', 'wb') as f:
		pickle.dump([], f)
	
def save_token():	
	quran_list=[]
	#read list from file
	with open('quran.txt', 'rb') as file:
		quran_list = pickle.load(file)
	return quran_list

def make_lexicon_list(quran):
	print(2)

'''
Created on Aug 30, 2015

@author: Sheece Gardezi
Read/Write data structure to a file
'''
import pickle

def write_dataStruct_to_file(fileName,data):

#writing list to a file 
	with open(fileName, 'wb') as data_file:
		pickle.dump(data, data_file)
	
def read_dataStruct_from_file(fileName):	
	
#read list from file
	with open(fileName, 'rb') as data_file:
		data = pickle.load(data_file)
	return data

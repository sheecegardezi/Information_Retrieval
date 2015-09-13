'''
Created on Aug 20, 2015

@author: Sheece Gardezi

implementation of Edit Distance - Dynamic Programming
'''

from sortedcontainers import  SortedDict
from core import Contants
import os


def applyFilters(word):
    word = removeStopChar(word)
    word=word.lower()
    word=ignoreStopWords(word)
    
    return word

def ignoreStopWords(word):
    if word not in Contants.STOP_WORDS:
        return word
    return ''

def removeStopChar(word):
    word = word.translate(None, '!@#$&*-:.,"()<>^''+|\/_`\'[]?0123456789;=%~{}')
    return word


def termIndex():
    sortTepDic=SortedDict()
    #Structure for each term
#   sortTepDic['term']=({'DocId1':['Pos1','Pos2'],'DocId2':['Pos1','Pos2']},'termFreq','DocFreq')

    for root, dirs, files in os.walk(Contants.DATA_DIRECTORY_NAME, topdown=True):
        for name in files:
            file_name=os.path.join(root, name)
    #         'r' when the file will only be read
    #         'w' for only writing (an existing file with the same name will be erased)
    #         'a' opens the file for appending; any data written to the file is automatically added to the end. 
    #         'r+' opens the file for both reading and writing.
    
            mode='r'
            file_object = open(file_name, mode) 
            DocId=os.path.split(file_name)[1]
            
            wordPos=0
            for word in file_object.read().split():
               
                wordPos=wordPos+1 #increment word location
                lamma = applyFilters(word)
                
                if lamma:
                    if lamma not in sortTepDic:
                        sortTepDic[lamma]=[{DocId:[wordPos]},1,1] #add a new term
                        

                    else:

                        sortTepDic[lamma][1]=sortTepDic[lamma][1]+1 #increment the term frequency
                        
                        if DocId in sortTepDic[lamma][0]:
                            sortTepDic[lamma][0][DocId].append(wordPos) #add new word position for the existing document
                        else:
                            sortTepDic[lamma][0][DocId]=[wordPos] #add a new document ID and he word position
                            sortTepDic[lamma][2]=sortTepDic[lamma][2]+1 #increment the document frequecy
    
    #covert lists to tuples                    
    for key in sortTepDic.keys():
        for DocId in sortTepDic[key][0]: 
            sortTepDic[key][0][DocId]=tuple(sortTepDic[key][0][DocId])
        sortTepDic[key]=tuple(sortTepDic[key])
                        
    return sortTepDic

                    
                
sortTempDic=termIndex()
print(sortTempDic)

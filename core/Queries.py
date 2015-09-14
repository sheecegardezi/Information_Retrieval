'''
Created on Sep 13, 2015

@author: Sheece Gardezi
'''
from core import Index
from core import Data
from core import Contants
from core import Permuterm
from numpy import abs

def boolean_queries(query):
    #preprocessing
    posting=Data.read_dataStruct_from_file(Contants.POSTING_LIST_FILE_NAME)
    
    setlist=[]
    for word in query.split():         
        word=Index.applyFilters(word)
         
        if word in posting:
            setlist.append(set(posting[word]))
        
    answer=set.intersection(*setlist)
    
    return list(answer)

def boolean_queries_implement_using_lists(query):
    #preprocessing
    posting=Data.read_dataStruct_from_file(Contants.POSTING_LIST_FILE_NAME)
    
    p=[]
    for word in query.split():
         
        word=Index.applyFilters(word)
         
        if word in posting:
            p.append(posting[word])

    index1=0
    index2=0
    p1=p[0][index1]
    p2=p[1][index2]
     
    answer=[]
     
    while True:
        try:
             
            if p1 == p2:
                answer.append(p1)
                index1=index1+1
                index2=index2+1
                 
                p1=p[0][index1]
                p2=p[1][index2]
            elif p1<p2:
                index1=index1+1
                p1=p[0][index1]
            else:
                index2=index2+1
                p2=p[1][index2]
         
        except IndexError:
            break
    
    return answer

def boolean_queries_with_proximity(query,proximity):
    #preprocessing
    posting=Data.read_dataStruct_from_file(Contants.POSTING_LIST_FILE_NAME)    
    wordsIndex=Data.read_dataStruct_from_file(Contants.WORD_INDEX_FILE_NAME)
    
    setlist=[]
    for word in query.split():         
        word=Index.applyFilters(word)         
        if word in posting:            
            setlist.append(set(posting[word]))
        
    wordList= [ Index.applyFilters(word) for word in query.split() if Index.applyFilters(word) in posting]
    DocIDList=list(set.intersection(*setlist))
    
    answer=[]
    
    for word1 in wordList:
        wordList.remove(word1)
        for word2 in wordList:
            for DocID in DocIDList:
                for PosID1 in wordsIndex[word1][0][DocID]: 
                    for PosID2 in wordsIndex[word2][0][DocID]:
                        if abs(PosID1-PosID2)<=proximity:
                            if DocID not in answer:
                                answer.append(DocID)
        
    return list(answer)

def wlidCard_queries_using_permuterm_index(query):
    
    posting=Data.read_dataStruct_from_file(Contants.POSTING_LIST_FILE_NAME)
    
    query=Permuterm.standardize_wildcard_query(query)
    DocList=[]
   
    for word in posting:
        permutermIndexes=Permuterm.create_permuterm_indexes(word)
        for permuterm in permutermIndexes:        
            if query in permuterm:
                DocList= DocList+ posting[word]
                break
                
    return set(DocList)
# example usage
# query='four dell'
# proximity=700
# print boolean_queries(query)
# print boolean_queries_implement_using_lists(query)
# print boolean_queries_with_proximity(query,proximity)
# query='bi*sh'
# print wlidCard_queries_using_permuterm_index(query)
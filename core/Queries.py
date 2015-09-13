'''
Created on Sep 13, 2015

@author: Sheece Gardezi
'''
from core import Index
from core import Data
from core import Contants

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

# example usage
# query='four dell'
# print boolean_queries(query)
# print boolean_queries_implement_using_lists(query)
'''
Created on Sep 14, 2015

@author: Sheece Gardezi
'''
from core import Index
from core import Data
from core import Contants
from collections import Counter


def rotate_string(word,n):
    return word[n:] + word[:n]

def create_permuterm_indexes(word):
    
    permutermIndexes=[]
    for i in range(-1,len(word)):
        permutermIndexes.append(rotate_string(word+'$',i))
    return   set(permutermIndexes)

# input in the form query=de*l
# output list of doumunts of occurance of word
def standardize_wildcard_query(query):
    query=query+'$'
    for i in range(-1,len(query)):
        word=rotate_string(query,i)
        if word[len(word)-1]=='*':
            return word[:len(word)-1]
    

'''
Created on Sep 13, 2015

@author: Sheece Gardezi
'''
from core import Index
from core import Data
from core import Contants
from core import BinaryTree

if __name__ == '__main__':
    Index.createTermIndex()
     
    indexedWords=Data.read_dataStruct_from_file(Contants.WORD_INDEX_FILE_NAME)
    lexicons=Data.read_dataStruct_from_file(Contants.LEXICON_FILE_NAME)
    posting=Data.read_dataStruct_from_file(Contants.POSTING_LIST_FILE_NAME)
    
    bt=BinaryTree.balancedTree(indexedWords)
    BinaryTree.DepthFirstSearchPrintNodes(bt)
    #print(posting)
    
    

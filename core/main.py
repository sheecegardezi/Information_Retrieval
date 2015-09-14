'''
Created on Sep 13, 2015

@author: Sheece Gardezi
'''
from core import Index
from core import Data
from core import Contants
from core import BinaryTree
from core import Queries

if __name__ == '__main__':
#     Index.createTermIndex()
     
    indexedWords=Data.read_dataStruct_from_file(Contants.WORD_INDEX_FILE_NAME)
    lexicons=Data.read_dataStruct_from_file(Contants.LEXICON_FILE_NAME)
    posting=Data.read_dataStruct_from_file(Contants.POSTING_LIST_FILE_NAME)
    
    bt=BinaryTree.balancedTree(indexedWords)
#     BinaryTree.DepthFirstSearchPrintNodes(bt)
    #print(posting)
    
    # example usage
    query='four dell'
    proximity=700
    print Queries.boolean_queries(query)
    print Queries.boolean_queries_implement_using_lists(query)
    print Queries.boolean_queries_with_proximity(query,proximity)
    query='bi*sh'
    print Queries.wlidCard_queries_using_permuterm_index(query)
    Queries.trailing_wildCard_queries_using_tree('del*')
    
    

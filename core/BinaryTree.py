'''
Created on Sep 14, 2015

@author: Sheece Gardezi
'''
import random
from time import time
from core import Data
from core import Contants

class BinaryNode:

    def __init__(self,value=None,data=None):
        """Create a binary node"""
        self.value=value
        self.data=data
        self.left=None
        self.right=None
    def add(self,value,data):
        """Adds a new node to the binary tree containing this value"""
        if value <=self.value:
            if self.left:
                self.left.add(value,data)
            else:
                self.left=BinaryNode(value,data)
        else:
            if self.right:
                self.right.add(value,data)
            else:
                self.right=BinaryNode(value,data)
    def delete(self):
        """
        Remove value of self from the binary tree.
        Works in conjecture with the remove method in the Binary Tree
        """
        
        if self.left == self.right == None:
            return None
        if self.left == None:
            return self.right
        if self.right == None:
            return self.left
        
        child =self.left
        grandchild = child.right
        if grandchild:
            while grandchild.right:
                child = grandchild
                grandchild = child.right
            self.value = grandchild.value
            child.right = grandchild.left
        else:
            self.left = child.left
            self.value = child.value
        return self


class BinaryTree:
    
    def __init__(self):
        """Create an empty binary tree"""
        self.root =None
    
    def add(self,value,data):
        """Insert a value in the proper location in the binary tree"""
        if self.root is None:
            self.root = BinaryNode(value,data)
        else:
            self.root.add(value,data)
    def contains(self,target):
        """Check weather the binary tree contains the target value"""
        node = self.root
        while node:
            if target==node.value:
                return True
            if target<node.value:
                node = node.left
            else:
                node=node.right
        return False
    def remove(self, value):
        """Remove value from the tree"""
        if self.root:
            self.root = self.removeFromParent(self.root, value)
    def removeFromParent(self, parent ,value):
        """Remove value from tree rooted at parent"""
        if parent is None:
            return None
        if value ==parent.value:
            return parent.delete()
        elif value<parent.value:
            parent.left = self.removeFromParent(parent.left,value)
        else:
            parent.right=self.removeFromParent(parent.right,value)
        
        return parent
        
def balancedTree(ordered):
    """Create balanced binary tree from ordered collection """
    bt = BinaryTree()
    addRange(bt,ordered,0,len(ordered)-1)
    return bt

def addRange(bt,ordered,low,high):
    """Add range to th binary tree in a away that it remains balanced"""
    if low <= high:
        mid = (low+high)/2
        
        bt.add(ordered.iloc[mid],ordered[ordered.iloc[mid]])
        addRange(bt,ordered,low,mid-1)
        addRange(bt,ordered,mid+1,high)
        

def DepthFirstSearchPrintNodes(bt):
    que=[]
    
    counter=1  
    print counter, bt.root.value
    if bt.root.left:
        que.append(bt.root.left)
    if bt.root.left:
        que.append(bt.root.right)
    while que:
        node=que.pop()
        counter = counter+1
        if node:
            print counter,node.value
            if node.right:
                que.append(node.left)
            if node.left:
                que.append(node.right)
    
def test_balanced_tree():
    wordsIndex=Data.read_dataStruct_from_file(Contants.WORD_INDEX_FILE_NAME)
    #print len(wordsIndex)
    #input a sorted dictionary 
    #bt=balancedTree(wordsIndex)
    #DepthFirstSearchPrintNodes(bt)
        
#test_balanced_tree()

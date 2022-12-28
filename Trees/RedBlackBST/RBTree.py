# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:08:17 2021

@author: User
"""
import random

RED=True
BLACK=False

class Node(object):
    def __init__(self,val=None,right=None,left=None,color=None):
        self.val=val
        self.right=right
        self.left = left
        self.color=color
        # add size later



class RBTree(object):
    def __init__(self):
        self.root=None
    
    def insert(self,x):
        self.root=self.insert_op(self.root,x)
        self.root.color=BLACK
        
    def insert_op(self,root,x):
        
        if root == None : return Node(val=x,color=RED)
            
        if root.val > x:
            root.left = self.insert_op(root.left, x)
        elif root.val < x :
            root.right = self.insert_op(root.right,x)
        else:
            root.val=x
        
        # check if it is read
        if self.isRed(root.right) and not self.isRed(root.left) : root=self.rotateLeft(root) 
        if self.isRed(root.left) and self.isRed(root.left.left) : root=self.rotateRight(root)
        if self.isRed(root.left) and self.isRed(root.right) : self.flipColors(root)
            
        
        return root
        
    def isRed(self,node):
        if node == None: return False
        return node.color == RED 
    
    def find(self,x):
        bo=self.find_op(self.root,x)
        return bo
    
    def find_op(self,root,x): # this
        
        if root == None: return False
            
        if root.val > x:
            bo=self.find_op(root.left, x)
        elif root.val < x :
            bo=self.find_op(root.right,x)
        else: # root.val== x
            return True
            
        return bo
    
    def minimum(self,root,min_val):
        if root.left == None: return root
        
        min_node=self.minimum(root.left,root.val)
        
        return min_node
    
    def deleteMin(self,root):
        if root.left == None: return root.right
        
        root.left=self.deleteMin(root.left)
        
        return root
        
        
    def  delete(self,root,x):
        
        if root == None : return None
        
        if root.val > x:
            root.left = self.delete(root.left, x)
        elif root.val < x :
            root.right = self.delete(root.right,x)
        else:
            if root.right == None : return root.left
            if root.left == None : return root.right
            
            #reach nodes
            t=root
            root=self.minimum(t.right,t.right.val)
            # perform swap
            temp=t.val
            t.val=root.val
            root.val=temp
            #
            t.right=self.deleteMin(t.right)
            root=t
            
            '''
            #another method of hibbard deletion by pointers
            t=root
            root=self.minimum(t.right,t.right.val)
            root.right=self.deleteMin(t.right)
            print(root.val,t.val)
            root.left=t.left
            '''
        return root
        
    def rotateLeft(self,node):
        x=node.right
        node.right=x.left
        x.left=node
        x.color=node.color
        node.color = RED
        return x
    
    def rotateRight(self,node):
        x=node.left
        node.left=x.right
        x.right=node
        x.color=node.color
        node.color=RED
        #node.color = RED
        return x
    
    def flipColors(self,node):
        node.color=not node.color
        node.left.color= not node.left.color
        node.right.color= not node.right.color
     
    def display(self):
        self.printTree(self.root)
        
    def printTree(self,node, level=0):
        if node != None:
            self.printTree(node.left, level + 1)
            print(' ' * 4 * level + '->', node.val)
            self.printTree(node.right, level + 1)
    
tree=RBTree()
'''
tree.root=Node(2)

tree.root.right=Node(3)

tree.root.left=Node(1)

tree.root.left.right=Node(9)

tree.insert(3)

tree.insert(14)

tree.insert(13)
#tree.insert(tree.root,14)
tree.insert(15)
tree.insert(18)
tree.insert(20)
tree.insert(12)
#tree.delete(tree.root,9)

#print(tree.find(tree.root,9))
tree.printTree(tree.root)
'''

for _ in range(1000):
    tree.insert(random.randint(0, 10000))
tree.display()
print(tree.find(9948))
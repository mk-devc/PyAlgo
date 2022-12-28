# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 09:07:25 2021

@author: User
"""


class Node(object):
    def __init__(self,val=None,right=None,left=None):
        self.val=val
        self.right=right
        self.left = left
        
    


class Tree(object):
    def __init__(self):
        self.root=None
        
    def insert(self,root,x):
        
        if root == None : return Node(x)
            
        if root.val > x:
            root.left = self.insert(root.left, x)
        elif root.val < x :
            root.right = self.insert(root.right,x)
        else:
            root.val=x
            
        return root
        
    
    def find(self,root,x): # this
        
        if root == None: return False
            
        if root.val > x:
            bo=self.find(root.left, x)
        elif root.val < x :
            bo=self.find(root.right,x)
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
            t=root
            root=self.minimum(t.right,t.right.val)
            root.right=self.deleteMin(t.right)
            print(root.val,t.val)
            root.left=t.left
            '''
        return root
        
    
    
    
tree=Tree()

tree.root=Node(10)

tree.root.right=Node(15)

tree.root.left=Node(7)

tree.root.left.right=Node(9)

tree.insert(tree.root,3)

tree.delete(tree.root,9)

print(tree.find(tree.root,9))





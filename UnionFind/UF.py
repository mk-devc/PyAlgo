# -*- coding: utf-8 -*-
"""
@author: Mohan

Note:
This is the quick union find implementation in python
"""

class UnionFind():
    def __init__(self,size,id=[],sz=[]):
        '''
        Parameters
        ----------
        size : Int
            The size of the array needed for the quick union find data structure. 0 will 
            return an error
        id : Int, optional
            Given Id of each component. The default is [].
        sz : Int, optional
            Size of each group or components. The default is [].
        
        Returns
        -------
        None.

        '''
        
        if size <= 0:
            raise ValueError("Size specified must be more than 0.")
            
        self.size=size
        self.noComponents=size
        self.sz=sz
        self.id=id
        
        for i in range(size):
            self.id.append(i)
            self.sz.append(1)
            
            
    def find(self,p):
        '''
        Parameters
        ----------
        p : Int
            Component that is of number p.

        Returns
        -------
        Root of the group which p belongs to.

        '''
        # iterates till it find the root which loops on itself.
        root = p
        while root != self.id[root]:
            root=self.id[root]
        
        # performing path compression
        # replaces all of the undirected values in the array straight to the root.
        while p != root:
            next = self.id[p]
            self.id[p]=root
            p=next
            
        return root
    
    def connected(self,p,q):
        '''
        

        Parameters
        ----------
        p : Int
            Component of type integer p.
        q : Int
            Component of type integer q.

        Returns bool
        -------
        Checks if the components or sets are from the same group or are connected.

        '''
        return self.find(p) == self.find(q)
    
    
    def componentSize(self,p):
        '''
        Parameters
        ----------
        p : Int
            Element in the group or a component.

        Returns
        -------
        size of the group or componet that has the member p .

        '''
        return self.sz(self.find(p))
    
    def components(self):
        '''
        Returns
        -------
        Number of components in the set.

        '''
        
        return self.noComponents 
    
    
    def union(self,p,q):
        '''
        Parameters
        ----------
        p : Int
            The element of component p.
        q : Int
            The element of component q.

        Returns
        -------
        Union 2 sets of groups with smaller merging with bigger group.

        '''
        root1 = self.find(p)
        root2 = self.find(q)
        
        # both are from the same group hence the same root
        if root1 == root2 : return
        
        if self.sz[root1] <  self.sz[root2]:
            self.sz[root2] +=  self.sz[root1]
            self.id[root1] = root2
        else:
            self.sz[root1] +=  self.sz[root2]
            self.id[root2] = root1
            
        self.noComponents-=1
        
    def display(self):
        '''
        Returns
        -------
        Display array of union find sets.

        '''
        print(self.id)
            


uf=UnionFind(10)
uf.union(1,2)
uf.union(3,4)
uf.union(5,6)
uf.union(7,8)
uf.union(0,9)
uf.union(1,9)
uf.union(1,3)

uf.display()

print(uf.find(9))

uf.display()

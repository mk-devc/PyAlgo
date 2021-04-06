# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 01:41:04 2021

@author: Mohan

Implementation of BinarySearch
"""


class BinarySearch(object):
    def __init__(self):
        pass
    
    def insert(self,arr,val):
        
        # O(n) complexity
        hi=len(arr)-1
        lo=0
        return self.insert_op(arr,lo,hi,val)
        
    def insert_op(self,arr,lo,hi,val):
        
        if hi < lo:
            aux=arr[lo:]
            res=arr[:lo]+[val]+aux
            return res
        
        mid=int((lo+hi)/2)

        
        if arr[mid] > val :
           bo = self.insert_op(arr,lo,mid-1,val)
        elif arr[mid] < val :
           bo = self.insert_op(arr,mid+1,hi,val)
        else:
            aux=arr[mid+1:]
            res=arr[:mid+1]+[val]+aux
            return res
        
        return bo
    
    
    def find(self,arr,x):
        hi=len(arr)-1
        lo=0
        return self.find_op(arr,lo,hi,x)
        
        
    def find_op(self, arr,lo,hi,x):
        
        
        if hi < lo:
            return None
        
        mid=int((lo+hi)/2)

        
        if arr[mid] > x :
           bo = self.find_op(arr,lo,mid-1,x)
        elif arr[mid] < x :
           bo = self.find_op(arr,mid+1,hi,x)
        else:
            return mid
        
        return bo
    
    def interpolation_insert(self,arr,val):
        # O(n) complexity
        hi=len(arr)-1
        lo=0
        return self.interpolation_insert_op(arr, lo, hi, val)
    
    def interpolation_insert_op(self,arr,lo,hi,val):
        
        if hi <= lo:
            aux=arr[lo:]
            res=arr[:lo]+[val]+aux
            return res
        
        pos = lo + int((val-arr[lo])*(hi-lo) / (arr[hi]-arr[lo]))

        if pos > hi: return arr+[val]
        
        if pos < lo: return [val]+arr
        
        if arr[pos]>val:
            bo=self.interpolation_insert_op(arr, lo, pos-1, val)
        elif arr[pos]<val:
            bo=self.interpolation_insert_op(arr, pos+1, hi, val)
        else:
            aux=arr[pos+1:]
            res=arr[:pos+1]+[val]+aux
            return res
    
        return bo

    
    def interpolation_find(self,arr,x):
        hi=len(arr)-1
        lo=0
        return self.interpolation_find_op(arr,lo,hi,x)
        
    def interpolation_find_op(self,arr,lo,hi,x):
        
        if hi < lo:
            return None
        
        pos = lo + int((x-arr[lo])*(hi-lo) / (arr[hi]-arr[lo]))

        
        if arr[pos]>x:
            bo=self.interpolation_find_op(arr, lo, pos-1, x)
        elif arr[pos]<x:
            bo=self.interpolation_find_op(arr, pos+1, hi, x)
        else:
            return pos
    
        return bo
    
        
    
    
        

        
        
k=[ 2, 3, 4, 10, 40 ]
bs=BinarySearch()
print(bs.interpolation_insert(k,39))



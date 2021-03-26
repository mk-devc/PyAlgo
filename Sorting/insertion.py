# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 01:07:32 2021

@author: User

Implementation of insertion sort
1. performing a swap with the initial and the next index
2. performing switching if needed that will sort the left part of the array


Special properties of using insertion sort:
    
    
"""

class Insertion:
    def __init__(self):
        pass
    
    def sort(self,arr):
        l=len(arr)
        for x in range(1,l):
            for y in range(x-1,-1,-1):
                print(y,x)
                if arr[y]>arr[x]:
                    self.swap(arr,y,x)
                    x=y
                else:
                    break
            
                    
                    
    def swap(self,arr,idx,minIdx):
        temp=arr[idx]
        arr[idx]=arr[minIdx]
        arr[minIdx]=temp
        
                
            
x=[-3,7,8,9,6,100,-1,-1000]    

s=Insertion()
s.sort(x) 

print(x)
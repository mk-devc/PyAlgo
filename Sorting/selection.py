# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 00:09:22 2021

@author: User

Selection sort implementation
1. find the min iterating the rest of the array and swap with the inital start
2. once done it will find the minimum and the initial point will move forward a step and move forward

Complexity is O(n^2)
"""


class Selection():
    
    def __init__(self):
        pass
        
    def sort(self,arr):
        l=len(arr)

        for x in range(l):
            for y in range(x+1,l):
                if arr[x] > arr[y]:
                    self.swap(arr,x,y)
                    
                
                
        
    def swap(self, arr, i , minIndex):
        temp=arr[i]
        arr[i]=arr[minIndex]
        arr[minIndex]=temp
        
        
        

x=[3,7,6,8,9,100,1]    

s=Selection()
s.sort(x) 

print(x)
        
        
        
        


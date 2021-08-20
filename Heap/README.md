# Priority Queue

Operations that are involved in PQ are to remove the largest or the smallest item from the tree like structure in the array. This is an important algorithm that will be used for graphs later on.


Methods in Maximum Priority Queue are as follows.

```

class MaXPQ:
    constructor() # to create empty pq.
    
    constructor(key) # to create pq with given keys, performing the swimming as we will see in a bit.
    
    insert(key) # insert key to pq
    
    delMax() # delete largest key in the pq
    
    isEmpty() # check if empty
    
    max() # return max value
    
    size() # return size

 ```
 
 
 # Binary Heap
 
A node with links to the left and right of binary tree represents a binary tree. Binary as it is only able to have 2 childs.  A binary heap is a heap data structure that takes the form of a binary tree. Binary heaps are a common way of implementing priority queues.

A binary heap is defined as a binary tree with two additional constraints:

Shape property: a binary heap is a complete binary tree; that is, all levels of the tree, except possibly the last one (deepest) are fully filled, and, if the last level of the tree is not complete, the nodes of that level will be filled from left to right( always begins from the left ) when adding more nodes .

Heap property: the key stored in each node is either greater than or equal to (≥) or less than or equal to (≤) the keys in the node's children, according to some total order.  -- Wikipedia

Here we see that it is a heap-ordered binary tree
 
 ![Alt Text](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmiro.medium.com%2Fmax%2F478%2F1*Tyb1cOw3b6jp1cRmuslJAg.png&f=1&nofb=1)
 
 ![Alt Text](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Max-Heap.svg/330px-Max-Heap.svg.png)

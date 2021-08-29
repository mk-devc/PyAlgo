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
 
 The above is a representation of the tree, however the data structure that is used to represent this tree is an array. Accessing the child and the parents are done by using a mathematical formula.
 
 ![Alt Text](https://miro.medium.com/max/600/1*MtegLKi_gNCdhVhX3GcGaA.png)
 
 For the array representation we begin at indices 1 althought we can start from indices 0.
 
 ### Binary Heap properties
 
 Binary Heap Properties are as follows:
 
 1. The largest key is either array[1] ( at index 1 or 0 ), root of binary tree.
 2. Use indices to move through the tree. Parent node at k(current index) is k//2( for python ) and children node is 2k and 2k+1


### Promoting and Demotion In a Heap

Promoting in a heap is requires if the heap order is violated and needed, the is when for example in a max heap a childs keys becomes larger compared to the parents key. To return back to the heap condition, we perform a swap operation up the tree using the formula given to achieve the heap order. 

Take a look at the english chart to compare its numerical values. For reference in later examples to convert english letters to alpabets.

![Alt text](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2F1.bp.blogspot.com%2F-uv9mTK8z6Uw%2FVZ26jhtUwWI%2FAAAAAAAABZw%2Fw-lw3JiGiCw%2Fs1600%2FSG.png&f=1&nofb=1)

An example is shown below. As we can see at T we violate the heap condition as P is smaller compared to T. We swap T with its parent P, however the heap order is still not achieved as the parent S is smaller compared to T. Hence, we perform another swap. It is after this the heap order is satisifed. Node will keep swaping till the parent is more than or equal to the parent.


![Alt Text](https://algs4.cs.princeton.edu/24pq/images/swim.png)

This operation is also known as swim operation. Here is the pseudocode.

```
# k presents the current node in the tree.
heap=[7,6,5,....]
# swap operation
function swap(parent,child):
          temp=heap[parent]
          heap[parent]=heap[child]
          heap[child]=temp

function swim(k):
        while k > 1 and heap[k//2] < heap[k]:
                swap(k//2,k)
                # update current node
                k=k//2
```

Demotion in a heap is when a parent is much lesser that the child and requires the heap order to be restored. So for this we swap the parent with the child until heap order is achieved. This operation is known as the sink operation and is normally performed when we delete the max element from the heap or if there were an element insert randomly across the heap array. 

Here we see that H is smaller compared to S and P( refer to english numeric table above ). We then swap H with S as S is larger( you could not use P as if you were to swap it, will be smaller compared to S ).However, after this we see that H is smaller compared to N and G. We then take the maximum child and swap with H, in this case would be N swap with H in the array. We then achieve heap order.



![Alt Text](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftechlarry.github.io%2FAlgorithm%2FPrinceton%2Ffigures%2FDemotionInAHeap.png&f=1&nofb=1)

Peusodcode for the sink operation is a below.

```
heap=[7,6,5,....]

# k is the position of current node
function sink(k,n):
        
        while 2*k <= n:
            j=2*k
            if j < N and heap[j]<heap[j+1]: j+=1
            if not heap[k] < heap[j]: break
            swap(k,j)
            # update current node position
            k=j
            
```

### Insertion Into and Removing an element in a Heap

As we follow the complete tree, we insert it at the most left of the heap tree. The basic idea is that we add to the end of the array. However, in most cases, adding to the back of the array will cause the heap order to be violated and hence we need to perform the swim operation to obtain the heap order.

Below is an example on how this works.

![alt text](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1600%2F1*SCeVkQIvd1ezcbDUaCPTeg.png&f=1&nofb=1)

Below is pseudocode explaining this steps. Complexity takes about at most 1+logN compares.

```
function insert(key):
        
        heap.add(key)
        n=heap.length-1
        swim(n)
```

For removing the element we could use to delete the maximum for the max heap. Takes 2Log(N) compares. As the diagram above illustrates we remove T from the maximum and we swap the last node in the array to the top of the tree or index 1 or 0 of the heap array. Once we have swapped it we perform the sink operation to achieve heap order.

Pseudocode for delMax operation is as below.

```
# N represents the last element in heap array
funtion delMax():
     max=heap[1]
     swap(1,N)
     sink(1)
     # to prevent loitering
     heap.pop(N)
     N-=1
     return max

```

| Algorithm   | Complexity for insert | Complexity for deleting maximum | Complexity Max |
| ------------| --------------------- | --------------------------------| ---------------|
| Binary Heap |        Log(N)         |               log(N)            |        1       |


# Performing Heapify

When we have an array that is ordered at random heapifying it will be a good idea inorder to achieve the heap order. This is done by accessing each parent to perform a sink operation if heap order is not satifsified in that sub heap tree.


First we use the last index and we half it as the formula states to access its parent. From there we perform the sink operation so at 11//2 will give us 5. From there we check if the sink operation is needed. In this case, it does. So at position 5 we move to the next parent by decreasing k which is 5 by 1 which is another parent at 4. We then repeat and perform sink operation till we reach the root and all sub heaps are in the heap order causing the whole heap array to be in heap order.

![alt text](https://algs4.cs.princeton.edu/24pq/images/heapsort-trace.png)

```
heap=[7,6,5,....]
function heapify():
        k=n//2
        # iterate through each parent.
        while k >=1:
            sink(heap,k,n)
```

It is recommend to use immutable objects to ease operations for debugging and such for keys. For converting the above to min heap all we have to do is use the more than equal (>=) to replace all its less than equal (<=) syntax.

In python we do not have to worry as we have resizing arrays. Looking deeper into lower level languages such as Java we would need to create a vector class that will resize the array into a larger array. A sample code is shown as below

```java
public final class Vector { 
 private final int N;
 private final double[] data;
 public Vector(double[] data) {
    this.N = data.length;
    this.data = new double[N];
    for (int i = 0; i < N; i++)
        this.data[i] = data[i];
    }
 …
}
```

# Indexed Priority Queue

# Binomial Heap


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
function sink(k,N):
        # here we use for index 1 will be the root
        while 2*k <= N:
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

For removing the element we could use to delete the maximum for the max heap. Takes 2Log(N) compares. As the diagram above illustrates we remove T from the maximum and we swap the last node in the array to the top of the tree or index 1 or 0 of the heap array. Once we have swapped it we perform the sink operation to achieve heap order. An example could be seen above in the heap operations image.

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
| Binary Heap |        Log(N)         |               Log(N)            |        1       |


# Performing Heapify

When we have an array that is ordered at random heapifying it will be a good idea inorder to achieve the heap order. This is done by accessing each parent to perform a sink operation if heap order is not satifsified in that sub heap tree. 

Take a look at the example below, first we use the last index and we half it as the formula states to access its parent. From there we perform the sink operation so at 11//2 will give us 5. From there we check if the sink operation is needed. In this case, it does. So at position 5 we move to the next parent by decreasing k which is 5 by 1 which is another parent at 4. We then repeat and perform sink operation till we reach the root and all sub heaps are in the heap order causing the whole heap array to be in heap order.

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

Index Priority Queue almost operates like normal PQ, the only difference is that it allows quick updates and deletions to key values pairs. This is done by performing a two way mapping, that is using its index values to its keys and its keys to index values. As we know, indexing requires the use of hashtable inorder to achieve this. Examples below we will assume we will be dealing with a min heap.

Methods in IPQ as follows:

```
# for the key k that we want to update, we need to obtain its key index 
ki=map[k]

class IPQ:
    constructor():
        #create PQ structure 
        
    delete(ki):
        # obtain key index to delete from PQ
        
    contains(ki):
        # checks if key is present in PQ
        
    peekMinKeyIndex():
        # return root of IPQ
    
    pollMinKey():
        # delete and return min value from PQ
    
    insert():
        # add key into PQ
        
    update():
        # change key value of a node to the IPQ
        
    decreaseKey():
        # add lesser values of key compared to previous key 
        
    increaseKey():
        # add larger values of key comapred to previous key

```
   
Now lets take a look of an example IPQ. On the right we have a table with names and key index values. These key index values represent the indexes in the array vals and pm(position map). So for instance the value of the name George is at index 6 of the array vals, the value 2.

Keep in mind the heap array is still present, its just an additional 3 arrays that will aid with the indexing of the key values and its key index.

We then try to find the position of the key in the heap array. So for instance, we would like to find out where Dylan is in the heap array. Looking at the key index table we get a value 3, we then look at 3 in the array pm and find that it is located at position 7 in the heap array.

For the im(inverse map) array, it is used to check the key index( ki ) in the key table and finally the name of the key value. The indexes for the im array is also reverse where the index represents the index in the heap array for the array of key indexes.


![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/ipq_example.PNG) 

## Insertion in Indexed PQ

Insertion are like regular heap pq, where we add the the end of the array or in the tree structure visualization from the bottom left and we later perform the sink function. The only difference here is that we need to do extra by keep the track of the pm and im array.



![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/ipq_insert.PNG)

Below we can see that pm changes as we are swaping the nodes with its position in the heap array. Hence at ki( key index of the key index table ) is now located at its new position in the heap array. So, at ki 12 and 11 we swap its values.

Same goes for im, however, keep in mind that the index of im represents the position in the heap array. So at position 5 and 12 we swap it, the ki value when performing the swim operation.We perform this till the heap order is satisifed.

![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/ipq_insert_1.PNG)

![!alt_text](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/ipq_insert_2.PNG)

```
# sz represents the size, here we give an example of 12
sz=12
function insert(ki,value):
    values[ki]=value
    # inserting to the end of the heap array
    pm[ki]=sz
    im[sz]=ki
    # similar to swim method in binary heaps but will keep track to perform swap in im and pm array
    swim(sz)
    sz=sz+1
    

function swim(i):
    p=(i-1)//2
    while  i >0 and less(i,p):
        swap(i,p)
        i=p
        p=(i-1)//2

funtion swap(i,j):
        # swapping key of table in pm array by obtaining ki first in im array, then 
        # access the ki that is indexed to the position in the heap array to swap
        pm[im[i]]=j
        pm[im[j]]=i
        
        # swapping ki based on 
        tmp=im[i]
        im[i]=im[j]
        im[j]=tmp
        
function less(i,j):
        return values[pm[im[j]]] > values[pm[im[i]]]
```

We could do the same for the sink function.

```
function sink(i):
    while true:
        # here +1 and +2 cause we start from index 0
        left=2*i+1
        right=2*i+2
        smallest=left
        
    if right < sz and less(right,left):
        smallest=right
    # left will act as the first child to check if we reach the end of the tree like structure
    # once we reach the end we ensure that the i variable is always smaller than its children
    # since its a min heap
    
    if left >=sz or less(i,smallest):
        break
    # as the function used above     
    swap(smallest,i)
    i=smallest
```
## Polling and Removing Elements 


Polling which is the removal of the root value performs similar in binary heap. However to remove an element rather than scanning the whole heap array. We used the key index table to find its position in the heap array. We then perform the usual of swapping the node with the end node, nulling the end node. The newly swapped node from the end will either need be sinked down  or swimed up the heap array.

Here is an example for polling. The image below shows that the array value at position 0 and 12 have already been swapped with each other.

![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/ipq_polling.PNG)

We then perform the swap in the im and pm array as shown. Note that the vals array does not change as the value is already been indexed to the ki table.

![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/ipq_polling_1.PNG)

We later remove the value by replacing the value based on the last position in the array( in this case it's 12 ). We obtain the key index in the heap array and from the im array and we replace it with -1 and using the value we got before we replace the im array with -1 and sub the vals array with a null.

![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/ipq_polling_2.PNG)

We have then successfully remove the last key value. The rest that is left is to, rectify the heap violation by performing a sink operation on the root.

![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/ipq_polling_3.PNG)

Now, the heap order is statisfied.

![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/ipq_polling_4.PNG)


Here is an example for Removing. As we can see that we would like to remove the value Laura from the Key Index table. We look up the pm array which its index is the key index table and the value in the array are the index in the heap array( poistion in the heap array). Laura here has a position index at the red node.

![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/ipq_removal.PNG)

We swap it with the last value in the heap array (in the tree like struture repsented in an array form), with this we will need to keep track of the pm array and the im array.
As you can see in the image below we swap the position in the heap array at index 1 based on the ki index 2 in the pm array with position in the heap array 11 with ki of 11 in the pm array. Same could be said for the im array only that the index of im array is the position in the heap array which is 1 with a value of 2 which represents the ki value in the key index (ki) table. This is swap with im array with index 11 which is the position in the heap array with a value of 11 and that is the key index table.

![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/ipq_removal_1.PNG)

Once the swapping is done we null the last value of the last element which is the value we would like to eliminate. Replace the vals array with null and the other pm and im array with -1 ( since we cant have an index with -1)

![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/ipq_removal_2.PNG)

After we have remove the element the heap order is not satisfied. Hence we will need to perform a sink operation as this is a mean heap. The value 11 is much larger compared to 5 ( at the purple ball ) and we will need to perform a sink operation to statisfy the heap order. This is done till the both children is smaller compared to the parent.

![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/ipq_removal_3.PNG)

```
function remove(ki):
    i=pm[ki]
    # swap fromt the previous pseudocode
    swap(i,sz)
    # sz is the length, so we -1 from it to access the array
    sz=sz-1
    # use from the previous functions above
    sink(i)
    swim(i)
    # delete to remove excess unwanted memory being pointed by variables
    values[ki]=null
    pm[ki]=-1
    im[sz]=-1
```



## Updating 

Updates value of a key in the binary heap by making use of the key index table. It is efficient as it works as a look up rather than scanning through the whole array. The figure below we see that we would like to change the key Carly to a value 1. As we can see, the heap order is not statisfied ( min heap ) as the parent with a value of 5 is larger compared to value of 1. Here we perform the siwim function, while keeping track of the im and pm array till the heap order is satisfied.

![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/ipq_updating_1.PNG)

The heap order is statisfied and the im and pm array are being kept track off.

![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/ipq_updating_2.PNG)



```
function update(ki,value):
    # get position in heap array
    i=pm[ki]
    # assign new value base on key index table
    values[ki]=value
    # perform sink or either swim on that position in the heap array
    sink(i)
    swim(i)
```

## Increase & Decrease Key

Application in Djikstra and Prims were able to update a given key to make the value either smaller or larger. If the non minimum or non maximum value is given, we proceed to reject it.

Let take a look at increase key function.

```
function increaseKey(ki,value):
    if less(values[ki],value):
        values[ki]=value
        sink(pm[ki])
        
```

The decrease key works the same the only difference is that we change the position arguements in the less function and sink to swim as this in a min heap.

```
function decreaseKey(ki,value):
    if less(value,values[ki]):
        values[ki]=value
        swim(pm[ki])
        
```


# Binomial Heap

A binomial heap is implemented as a set of binomial trees (compare with a binary heap, which has a shape of a single binary tree), which are defined recursively as follows:

1.A binomial tree of order 0 is a single node
2.A binomial tree of order k has a root node whose children are roots of binomial trees of orders k-1, k-2, ..., 2, 1, 0 (in this order). -- Wikipedia

Here we take a look at 2 distinctions, one is **binomial tree** and **binomial heap**. A binomial tree is a tree a which has a root of a node with children. A binomial heap consist of many binomial trees.


## Binomial Trees and it's structure

A binomial tree B<sub>k</sub> is detailed as below:

1. B<sub>0</sub> is one node
2. B<sub>k</sub> is a pair of or a combination of 2 B<sub>k-1</sub> where the root of one becomes the left most child of the other. This only happens when we have k>=1 only as B<sub>0</sub> only has 1 node.
3. With the above said, when combining them we will have a min heap property. So the root with the smallest value tree will be the root and the left most child will be the tree witht the larger root


![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Binomial_Trees.svg/1024px-Binomial_Trees.svg.png)

From the image we can see that B<sub>1</sub> has 2 B<sub>0</sub> and some goes for B<sub>3</sub> which has 2 B<sub>2</sub>.

Here we can see the structural properties of the Binomial trees.

1. There are 2^k nodes for a tree.
2. The height of the tree is k
3. There are exactly <sup>k</sup>C<sub>i</sub> nodes at depth i =0,1,2,...k. Check out [permutation and combinatons](https://www.mathsisfun.com/combinatorics/combinations-permutations.html) to see what's it about. This is why it's called binomial heap due to the binomial coefficient or also known as pascal triangle.
4. The root degree has degree k which is largest compared to the other node is the tree. Root is numbered from left child to right child by k-1 , k-2...0. Which means child at k-1 has a degree of k-1. for subtree B<sub>k-1</sub>.




## Binomial Heap and it's structure

Binomial heap is collection of binomial trees that fits the following properties:

1. No 2 or more binomial trees in the root list ( link of trees connected by the root of each binomial tree ) have the same degree.
2. Each node has a key
3. Each satisifies the min heap property in this case.
4. Degree of each root in the root list in connected in increasing order.


![binomial heap](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.yiQNnCcdGIkCmpPWhMT-kwHaCg%26pid%3DApi&f=1)

We can see the nodes connected in the straight link from the root pointer represents the root list. The degree of the roots are connected in increasing order. Same goes for the children in the root list.

## Binomial Heap Representation

Each node N has the variables given.

1. a variable that stores its key
2. a variable d that stores the degree n
3. pointer P[N] points to parent of N
4. pointer Child[N] points to left most child
5. Pointer sibling[N] or next[N] that point to the right sibling of N



![bh1](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/bh1.PNG)

We can see that from the image given how the variables in the node is represented. Take a look at the pseudocode for the Node class use to create the node object.

```
class Node:
    function(key=None,val=None):
        self.degree=0
        self.child=self.next=self.parent=None
        self.key=key
        self.val=val
        
```

## Binomial Heap Find Minimum 

This operation is straight forward as we look at the root list to identify the needed minimum value. This function returns a pointer to the minimum root node.

```
function binomial_min_key(h):
        y=None
        x=self.head # from the binomial class
        min=x
        x=x.next
        min_prev=x
        while x != None:
            if x.key < min.key:
                min=x
                min_prev=prev
            prev=x
            x=x.next
        return min,min_prev
        
        
```  

Complexity takes about O(log(n))

## Binomial Heap Union

The image below show the process of uniting the 2 binomial heaps together, we would need 2 phases and that is the merging of the binomial heaps and union of the binomial heaps.
Merging is when we concatenate the 2 binomial heap together in sorted degree order ( increasing order ). In order for this to be done, we need the aid of the helper methods which is link which will take the root of the lesser key value to be the root and the key which is larger to be the left child.

Here we look at a few cases such that is needed when union takes place.

Case 1: When degree of x(cur as shown in the pseudocode) is not equal to the next degree we just move to the next node.We do not need to do anything as we only need to unite those of the same degree
Case 2:When x is the first of three roots of equal degree, that is, when degree[x]=degree[x.next]=degree[x.next.next]. Here we move the pointers forward by one position down like in case 1, we then perform a case 3 and 4 ( look below for furhter explanation on case 3 and case 4 )

For both case 3 and 4 occurs when the first 2 degree are the same, degree[x]=degree[x.next]!=degree[x.next.next] the only difference between case 3 and case 4 is that which key gets chosen to be the root. Of course the lesser one.

Case 3:  With Case we link x with x.next, in this case x.key <= x.next.key so we make x the parent and x.next the left child.
Case 4:  The opposite of case 3, where x.next.key is the smaller key and x.key is the larger key we make x.next.key the root while making x.key the left child 

Take a look at the image below on how performing union on 2 binomial heaps.

![bh_union](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/bh_merge_union.PNG)
![bh_union](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/bh_merge_union_1.PNG)

Uniting 2 binomial heap is used as a subroutine in most other operations. This procedure repeatedly links binomial trees whose roots have the same degree. Here we first take at the link implementation were x becomes the parent and
```
function binomial_link(y,x):
        #y becomes the child and x is the soon to be parent
        y.parent=x
        y.next=x.child
        x.child=y
        x.degree+=1
     
     
```

This pseudocode unites both binomial heaps together and will return the resulting heap. Before performing the function union we do the merge of the 2 binomial heap. This is done to become a singly linked list root list in sorted degree increasing order. There wil only be about about 2 trees with the same degree but not more in this case as one of the properties of the binomial heaps is each tree has a unique degree and it is not similar to the other in the binomial tree. If this is not the case then we might not be dealing with a binomial heap.



```

function binomial_merge_root(h1,h2):
        if not h1:
            return h2
        if not h2:
            return h2
        h=none    
        if h1.degree < h2.degree:
            h=h1
            h1=h1.next
        else:
            h=h2
            h2=h2.next
         t=h #
         while h1 != None and h2 !=None:
                if h1.degree < h2.degree:
                    t.next=h1
                    h1=h1.next
                else:
                    t.next=h2
                    h2=h2.next
                t.next
                
         if h2 == None:
                t.next=h1
         else:
                t.next=h2
                
         return h
```
 
 
Here we perform the union operaton after the merge has been done. 

```
function binomial_union(h1,h2):
        h=Node()
        head=binomial_merge_root(h1,h2)
        h1,h2=None,None # free memory
        if head == None:
            return head
        
        prev=None
        cur=head
        next=cur.next
        
        while cur.next !=None:
                if (cur.degree != next.degree) or ( next.next != None and next.next.degree == cur.degree):
                    #  Here we have 3 cases, we would want combine both when 
                    #  1. 2 trees together have the same degree and the next pointer to the later tree has a different degree and its not a None we break to the 
                    #     to the other condition to perform merge
                    #  2. 2 trees together have the same degree and the next pointer to the later tree has a same degree we move the pointer to reach to the end 
                    #     till the degree next to the later of the 2 trees has a different degree then we go to next condition to merge.
                    #  3. if 2 adjacent trees have different degree and the next degree has a different degree we proceed to skip by moving the nodes.
                    prev=cur
                    cur=next
                    
                elif cur.key <= next.key:
                    # we perform the linking
                    cur.next=next.next
                    biomial_link(next,cur)
                else:
                    if prev == None:
                        h = next
                    else:
                        prev.next=next
                        binomial_link(cur,next)
                        cur=next
                        
                
                next=cur.next
        
```

## Binomial Heap Creation and Insertion

Here it is simple to create a node. The psudocode below takes care of the rest. Insertion we create the node and then insert into the root list and order them by their degree in increasing order.


```
function binomial_insert(h,x):
     h1=BinomialHeap()
     
     x.parent=None
     x.child=None
     x.degree=0
     
     h1.head=x
     
     h=self.union(h,h1)
     
     return h    
     
```

# Extracting node with Minimum Key

Extracting the minimum from the root is as good as removing the root of the smallest node from the root list. Following the property of as above, left roots are B<sub>k-1<sub> , B<sub>k-2</sub>,...B<sub>0</sub> . We would now want to combine the children of the extracted min node to the root list, however we need to reaarange them in increasing order of its degree as it is one of the properties of the binomial heap( refer above ).
    
The image below explains how this works.
    
![Extracting Minimum Key](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/extracting_key.PNG)
    
 Here is a pseudocode on the reversing the child list. We use the previous finding min that returns the pointer to the minimum root node.
    
```
 function binomial_extract_min():
    min_key,min_prev=self.binomial_min_key()
    
    reverse_linklist_head=self.binomial_reverse_link_list(min_key.child)
    
    min_prev.next=None
    min_key.child=None
    
    h1=BinomialHeap()
    
    h1=self.binomial_union(self.h,reverse_linklist_head)
    
    return min_key
    
function binomial_reverse_link_list(h):
        # h is the pointer to the first left child of the node
        if h == None: return None
        # tail here is the most right hand side of the node of the link list that has been reversed and detached
        # this will seen with an example below
        tail=None
        next=h
        h.parent=None
    
        #   h next                     tail-> None  
        #    \  \  
        #     o->o->o->o->None
        #
        #tail  (h)     (next)                       
        #   \    \        \  
        #   None<--o       o---->o---->o---->None 
        #
        #       tail  (next,h)                     
        #         \       \  
        #   None<--o       o---->o---->o---->None 
        #
        #      tail     (h)   next                 
        #         \       \     \
        #   None<--o       o---->o---->o---->None 
        #
        #             (tail,h) next                 
        #                 \     \
        #   None<--o<------o     o---->o---->None 
        #
        #             (tail) (h,next)                 
        #                 \     \
        #   None<--o<------o     o---->o---->None 
        #
        #  This occurs till we reach the end of the list were the next pointer points to None and we straight away connect that pointer to the previous tail.
        #  We return the head of the pointer of the reversed link list the tail points to the next node of the reversed link list from the head.
        #
        #
        
        while h.next != None:
            # we move the next pointer
            next=h.next
            # pointing the net node to the previous node
            h.next=tail
            # now we make the the previous node the tail
            tail=h
            # make the next node the head
            h=next
            # remove the new head parent link
            h.parent=None
        h.next=tail
        return h
                        
```

# Decreasing Key
    
Decreasing the key is exactly like how you do it for a normal binary heap. First we check if the value is more than the key value in the current node. If it is, we break out of the function as the value is larger.
    
```
function binomial_decreasing_key(h,x,k):
         if k > x.key:
                print("key is larger than the current key value")
                return
         x.key=k
         # use y to point to where x is pointing    
         y=x
         # point to x parent to find if parent is lesser than child
         z=y.parent
         # iterqate 
         while z != None and y.key < z.key:
                    self.swap(y,z)
                    # after bubbling up we point to the current position and z to its current position parents
                    y=z
                    z=y.parent

                                           
 function swap(y,z):
         temp=y.key
         y.key=z.key
         z.key=temp  
                                           
         # swap the other values to
         temp=y.degree
         y.degree=z.degree
         z.degree=temp
                                           
# Deleting Key in 

# Fibonacci Heap

Fibonnaci Heaps differ from Binomial Heaps as follows:

1. Fibonnaci heaps are not neccesarily binomial, they can have more than 2 children.
2. Siblings ( or next base on the code above) are linked both ways like a doubly linked list.
3. There is a pointer min which will always point to the minimum key value.
4. The root degress are not unique ( unlike binomial which requires to be unique)
5. There is a special attribute that mantains total number of nodes in the fibonacci heap.
6. Nodes can be marked.

We will visit in more detail regarding this points. We first take a look at an example below. 

![alt text](https://cdn.programiz.com/cdn/farfuture/WgeXgB_o4_0qX5Iv2msbC1zcYn1s3Ay7ypgfac4CmMo/mtime:1585306008/sites/tutorial2program/files/fibonacci-heap.png)

If we look at the strucutre and point 1. It actually uses a circularly doubly link list as below.

Advantage compared to using Binomial Heaps are as follows.

1. A node can be removed from a circularly double link list pretty fast at a complexity of O(1).
2. Given such 2 list can be concatenated at O(1) time.
3. 

![alt text](https://cdn.programiz.com/sites/tutorial2program/files/fibonacci-heap-structure.png)

With this in mind let take a look at how the nodes are composed like with the pseudocode below.

```
class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            # left and right are used for doubly link list, child is a single link list as shown in the image above
            self.parent = self.child = self.left = self.right = None
            # number of connections or children
            self.degree = 0
            self.mark = False

```


## Operations in Fibonacci Heap


## Needed Helper Functions in Fibonnaci Heap Operations


 ```
# Helper function
                    
function heap_link(y,x):
        # this links the to the root list by removing y which is parent and attaching children to the root list
        self.remove_from_root_list(y)  
        # doubly link list to itself
        y.left = y.right = y
        # 
        self.merge_with_child_list(x,y)
        x.degree+=1
        y.parent=x
        y.mark=False
                    
                    
                
                    
function remove_from_root_list(self,y):
        # remove y from root list
        if y == self.root_head:
            self.root_head=y.right
        
        # basically skipping the connection , 0---1---2 becomes 0---2 , 1
        node.left.right=node.right
        node.right.left=left
        
function merge_with_child_list(self,parent,node):
        if parent.child == None:
            # child is the variable node for the parent 
            parent.child=node        
        else:
            #like inserting between the child root list
            # here we do it for the node 
            #   parent
            #      |
            #   child <-> ( node needed to be inserted ) <-> (previous children root list node )
            # we start with pointing in the node
            node.right=parent.child.right
            node.left=parent.child
            # then we do it for the parent
            parent.child.right.left = node
            parent.child.right = node
                

function merge_with_root_list(self,node):
        # if none it will be the root head
        if self.root_head == None:
            self.root_head=node
        else:
        # 1<--->3 , insert 2 , 1<--->2<--->3
           node.right=self.root_head.right
           node.left=self.root_head
           self.root_head.right.left=node
           self.root_head.right=node

                    
                    
function remove_from_child_list(parent,node):
        if parent.child  == parent.child.right:
                # release the only child
                parent.child=None
        elif parent.child ==node:
                # the node we would like to remove, let the next child be the direct child to the parent
                #   1                      1
                #   |          -->         |
                #   2<--->3           2<-->3
                parent.child=node.right
                node.right.parent=parent
        
        
        # skipping the middle node which is removing it
        # 1<---->2<---->3  --> 1<---->3
        # if we take a look at the figure above we can see that it will be carried out the same
        #         1
        #         |
        # None<-->3
        node.left.right=node.right
        node.right.left=node.left
                              
```



### Creation  and Insertion

To insert with first have to create a singleton tree, which is the creation step, to insert this singleton tree we add to left of min pointer. The pseduocode below explains it.

![Fib Insert](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/fib_insert.PNG)


```
# Basic representation of the overall FH (Fibonacci Heap)
class FibonnacciHeap(object):
       def __init__():
        self.root_list,self.min_node=None,None
        self.total_nodes=0
```

```
# merge to the left of the min value in the root list

function insert(key,value):
    # creation of singleton node
    n=self.Node(key,value)
    n.left=n.right=n
    n.parent=None
    n.child=None
    n.mark=False
    
    # if Node is present 
    if self.root_head==None:
        self.root_head=n
    else:
        self.merge_with_root_list(n)
        
    if n.key < min_node.key:
        self.min_node=n
    self.total_nodes+=1
    
    return n
   
```  





### Union of Fibonacci Heap

Here we concatenate 2 fibonacci heap where root list are circularly doubly link list. Take a look at the pseudocode below.


```
# concatenate the fb heaps with its root list like usual
# since its a fibonacci heap keep in mind that we have doubly link list

function merge_fh(h1,h2):
    h2.root_head.left.right=h1.root_head
    h1.root_head.left=h2.root_head.left
    h1.root_head.left.right=h2.root_head
    h2.root_head.left=h1.root_head.left
    
    
    if h1.min_node > h2.min_node:
        h1.min_node=h2.min_node
        
    h1.total_nodes=h1.total_node+h2.total_nodes
    
    return h1
```

### Delete Minimum In Fibonacci Heap

Here there are 2 things we will do, 

1. Delete the min and concatenate its children into root list.
2. Consolidate trees so that no two roots have the same degree.


![Extract Min](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/fib_extract_min.PNG)
![Extract Min 2](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/fib_extract_min_2.PNG)

```
function iterate(self,head):
    # if we return back to the head due to it being doubly linked list we break out of it
    # mean while we collect its children and return it in the form a generator like (mutiple returns) using the yield keyword
    node = stop= head 
    flag=False
    
    while node != stop and flag == False:
        if node == stop:
            flag=True
        yield node
        
        node=node.right
        
```    

``` 

function extract_min(h):
        z= h.min_node
        
        if z != None:
            if z.child != None:
                # here we attach child to the root list
                children=[ x for x in self.iterate(z.child)]
                
                # place left and right marker
                left_ptr=h.min_node.left
                right_ptr=h.min_node.right
                
                # remove the min but keep the min_node pointer pointing to it
                left_ptr.right=right_ptr
                right_ptr.left=left_ptr
                
                for x in range(len(children)):
                
                    children[x].right=right_ptr
                    right_ptr.left=children[x]
                    children[x].left=left_ptr
                    left_ptr.right=children[x]
                    
                    left_ptr=children[x]
                    
                    # null the parents out
                    children[x].parent=None
                    
                self.min_node=h.root_head
                
                if z==z.right:
                    h.min_node=h.root_head = None
                else:
                    min_node=z.right
                    self.consolidate()
                
                

function consolidate():
        base=1.1618 <--- Golden ratio
        A = [None] * int(math.log(self.total_nodes,base) +1 ) # can also be done with log(self.total_nodes)*2 which is usnig natural log
        nodes = [w for w in self.iterate(self.root_head)]
        
        for x in range(0,len(nodes)):
            w=nodes[x]            
            d=w.degree
            
            while A[d] != None:
                y=A[d]
                
                if x.key > y.key:
                    # swap with x and y to ensure x is always the parent and y is the child
                    # to write lesser code and more systematic
                    temp=x
                    x=y
                    y=temp
                    
                self.heap_link(y,x)
                A[d]=None
                d+=1
            A[d]=x
            
            # finding new min node
            # we iterate through A
            for x in range(0,len(A)):
                if A[x] != None:
                    # check their key is smaller than the min_node key
                    if A[x].key < self.min_node.key:
                        self.min_node =A[x]
                    
                    

 ```
 ## Decrease Key and Delete Key in Fibonacci Heap
 
Base on the pseudocode The decrease key is done by rejecting anything more than the given key of the node. The mark attributes in the nodes are used to achieve dessired time bounds. 


For node x say for example somethings have occured such as :

1.



As soon as the second 
 
 ![Fib Decrease Key](https://github.com/MK-1729/PyAlgo/blob/main/Heap/img/fib_decrease_key.PNG)
 
 ```
 function decrease_key(x,k):
        # k is the value to be updated in the node, must be lower since it's min heap order
        if k > x.key:
            return None
        
        x.key=k
        
        y=x.parent
        
        if y != None and x.key > y.key:
            self.cut(x,y)
            self.cascading_cut(y)    
            
        if x.key < self.min_node.key:
            self.min_node=x
 
 
 function cut(x,y):
        # y is the parent , xi is the child
        self.remove_from_child_list(y,x)
        y.degree-=1
        self.merge_with_root_list(x)
        x.parent=None
        x.mark=False
        
        
 function cascading_cut(self,y):
        z=y.parent
        if z != None:
            if y.mark==False:
                y.mark=True
            else:
                self.cut(y,z)
                self.cascading_cut(z)
        
 
 ```
 
 
 ## Summary of the Fibonacci Heap and its Complexity
 
 To find out why decrease key only takes O(1) complexity we look at the change in potential. 
 
 We define the potential function as sigma = num.roots+2*(num.marked_nodes)
 
Operation  | Complexity
------------ | -------------
Decrease-Key | O(1)
Insert | O(1)
Extract_Min | O(log(N))


A great video to find out more about [Binomial Heaps](https://www.youtube.com/watch?v=FMAG0aunrmM&ab_channel=FoundationsofDataScience) and [Fibonacci Heaps](https://www.youtube.com/watch?v=fRpsjKCfQjE&ab_channel=FoundationsofDataScience). Check out more about the [Amortized Complexity Analysis](https://www.youtube.com/watch?v=fRpsjKCfQjE&ab_channel=FoundationsofDataScience) of the fibonnacci heap.

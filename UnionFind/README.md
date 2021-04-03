# Union Find

To put it basically, if there is a set of objects we would like to perform 2 operations. Union and Find are the methods that are key to this algorithm.

Say for example as below shows a list of points that are 'connected' togehter,

```
union(4,3)
union(5,4)
union(7,5)
union(2,1)
connected(7,3) # return true
connected(7,1) # return false

3---4        1---2     0
    |
    5
     \
    |  \
     ---7     
``` 
 
Here we can see that if we were to call the union command on 3 and 4 it will connect 3 and 4 together. Using connected we get to see if the components are connected together.
 
 
Here we assume the connections have certain properties. 
 
1. It is reflexive, meaning if 0 can be connected to itself.
2. Symmetric, 5 can be connected to 7 and vice versa.
3. Transitive, 3 is connected to 4 then and 4 is connected to 5, then 3 is connected to 5. 

 When this relations are carried out we will have several connected components. Like the example above there is 3 connected components. 
 
 
 Note that Quick Finf and Quikc Union are data structures that are both focused on improving the operation.

## Quick Find Data Structure

### Eager Algorithm

1. The idea here is that if 2 items are in the same connected component they will have the same entry
2. Those with the same index and entry value is considered the root


When performing the union we will have to change one connected components entries to their respective roots of the desired connected component.This will take O(n^2)operations when interating through the whole array while performing the union.



```python
# initialize and array with it being reflective to itself for each index

id=[]
n=10
for id in range(n)
#


```


## Union Find Data Structure

Here as we saw earlier that this operation will be expensive. Hence we use the concepts of trees inorder to help reduce time complexity by only changing the child's parent index when connecting 2 connected components.


## Weighted Quick Union Find

Here we could join 2 trees base on the size of each tree.  Taking a smaller tree above and larger tree below beigining union will cause the tree to get taller which results in higher complexity. Instead we do the vice versa of it to ensure the depth of the tree are in certain cases not that long.

In short, to not put the large tree lower, this is done by keeping track of each size of the connected component. The smaller tree like connected component, will have the its root index contain the value of the root larger tree. This makes the tree flat.

```python
# modifications to the previous code is that we add an array to keep track of the size of the connected components of each index.
# connect which used the find method is still the same

# in the union function as stated below

j = self.find(p)
i = self.find(q)

if i == i : return
if sz[i] < sz[j] : self.id[i]=j; self.sz[j]+=self.sz[i];
else:  self.id[j]=i; self.sz[i]+=self.sz[j]
    
```
Here both Union and Find takes O(log(N)) complexity when performing its operation due to it having similar properties to a tree and the tree does not grow to deep and rather shallow.


## Path Compression

Set each index to have the root value index( id to be set to point to the root). This helps make the tree flat.

There are 2 ways we can implement this. One is by using the child to point to the grandparent. The other is by setting each examined node to point to the root.

```python
# in the find function
# p here is the value we intend to find in the given tree
# points till we find the same index and value whihc indicates root

root=p
while root != id[root]:
    id[i]=id[id[i]
    root=id[i]

## the 2nd implementation
## another while loop from the above

while id[p] ! == root:
    # get the index
    next = id[p]
    id[p]=root
    p = next

```

## Amoritzed Analysis

Performs almost but not so much similar to a linear operation of O(n) rather than O(n^2) for the earlier data structure. 




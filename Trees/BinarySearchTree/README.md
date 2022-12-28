# Binary Search Tree

Some given rules are as follows:

1. There are subtrees within a tree
2. Given the pivot at the highest or first level of the tree. The elements of the subtree that is located within the left of the pivot should be lesser than the pivot(root)
   and the right subtree is larger than the pivot.

Point to be taken is that a binary tree is different from binary search tree. The rules of the binary tree is that it mostly has 2 childs like it's name indicates.


Here we will cover operations such as traverse, search , insert , delete.

Traversing the tree is performed  is performed using 4 different ways. 3 steps is always needed and that is visit, move left and move right.

# Traversing the Binary Search Tree

## Preorder traversal

```
    visit
    traverse left
    traverse right
```

Purpose of why you would wanna use this is to make a complete duplicate of a binary tree structure in a 1d array.

## Inorder traversal

```
    traverse left
    visit
    traverse right
```

Purpose of using this could be to check if the bst is in order by ascending.

## Postorder traversal

```
    traverse left
    traverse right
    visit
```

Purpose of why you would wanna use this is to delete the parent node of the bst or delete a tree.

## Levelorder traversal

```
     # operations are performed recurisvely
     
     if child is empty exit 
     
     check left is not empty and add left to queue
     check right is not empty and add right to the queue
     
      parent is empty replace with child 
     
```     

# Ordered operations in BST

Finding minimum in the tree is straightforward as we try to traverse all the way to the left till it reaches the end. Vice versa applies to finding the maximum

```
function minimum(node,min_value):
   if node.left is null return node
   
   node_min<-minimum(node.left,root.val)
   
   return node_min
   
```
For maximum change it to node.right in the recursive function


# Inserting into the Binary Search Tree

If the key is present just replace it's value like a symbol table. If the key isnt there add a new node to the bst.

Steps taken in inserting into the binary search tree:


```

function put(node,key,val):
      if node is null -> create new Node
      cmp<-compare the key being inserted with the key being traversed
      
      if cmp < 0: # which indicates less than
         node.left <- put(node.left , key , val)
         
      else if cmp > 0:
         node.right = put(x.right,key,val)
         
      else:
         node.val=val
      return node
```     



# Searching in the Binary Search Tree

It is the same as insert implementation but only difference is that it returns a boolean. True if value is present , False if value is not present. 
Also this could be used to get the value of the key were searching.

Steps taken to search value of a key in a BST:


```

function get (node,key):
      if x is null -> return null
      cmp<-compare the key being inserted with the key being traversed
      
      if cmp < 0: # which indicates less than
         x=get(node.left , key)
         
      else if cmp > 0:
         x=get(node.right,key)
         
      else:
         x=val
      return x
```     
Applying the same function iteratively

```
function get(key):

   Node x = root;
   
   while x is not null:
      cmp<-compare the key being inserted with the key being traversed
      
      if cmp < 0:
         x=x.left
      else if cmp> 0:
         x=x.right
      else:
         return x.val
         
    # if nothing is found till the end return null
    return null
```

# Deleting a Node in a BST

## Deleting Minimum

First we approach in the form of ordered operations, lets say we start by deleting the minimum key value. We first traverse all the way to the left till we reach null and that is the minimum. We return its right link pointer node to let the previous parent node point of the minimum that was deleted to point to it. Then we update the link to the root of the node.

```
function deleteMin(node):
   if x.left is null: return x.right
   
   node.left=deleteMin(node.left)
   
   return node
   
```
## Hibbard Deletion

### Deleting with only no child
   


Implementing iteratively
Usually the best case for the trees is always symmetrical, typically its slightly symmetrical. The worse case is when the keys are in order and this causes the tree to be represented 
a long tree either to the left or to the right which makes is as good as a linked list structure. Search and inserting will be as good as sequential. When we randomized the worst case of tree height is 4.311 ln N by [Reed,2003].


In other note, quicksort has a direct correspondence with BST if the keys are not duplicated. A good pdf here sums it all : https://people.eecs.berkeley.edu/~jfc/cs174/lecs/lec3/lec3.pdf 







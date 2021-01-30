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


## Inorder traversal

```

    traverse left
    visit
    traverse right
```


## Postorder traversal

```

    traverse left
    traverse right
    visit
```


## Levelorder traversal

Coming soon




# Inserting into the Binary Search Tree

If the key is present just replace it's value like a symbol table. If the key isnt there add a new node to the bst.

Steps taken in inserting into the binary search tree:


```

function put(node,key,val):
      if x is null -> create new Node
      cmp<-compare the key being inserted with the key being traversed
      
      if cmp < 0: # which indicates less than
         node.left <- put(node.left , key , val)
         
      else if cmp < 0:
         x.right = put(x.right,key,val)
         
      else:
         x.val=val
      return x
```     












# Graphs

Graphs are networks that can be used to represent relations between elements. Image below shows that the number 1 to 4 which are the nodes represents the elements and the lines between elements represents the edges(relationship) between elements.

![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Graphs/Images/graph-1.PNG "Graph Example (credit geeksforgeeks")

# Data Structure of Graphs

There are three ways to store a graphs.

Data Strucutre   | Complexity(Memory)
-------------    | -------------
List             | O(E)
2D-Matrix        | O(V^2)
Adjacency Matrix | O(V+E)

As we can see from above that the list if=s more efficient in terms of storing in memory compared to the others but due to its lack of structure and other and disadvantages in processing other search functions 2D-Matrix and adjaceny matrix is often opted.

However, the matrix takes up more memory compared to Adjacency matrix. For less denser graphs comp

# Types of Graphs

## Undirected Graphs

Undirected graphs have no direction 

## Directed Graphs

## Weighted Graphs ( Both Directed & Directed)

Trees are also considered a type of graph. The types of trees are rooted trees and non-rooted tree.

## Directed Acyclic Graphs

## Bipartite Graph

This is a graph whose vertices can be split into 2 independent groups A and B such that every every edges connects between nodes in A and B.

Another way of putting is there exist 2 colors in the graph and there are no odd length cycle (eg. 3 edges between 3 undirected nodes).

Below is an example of a bipartite graph.

![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Graphs/Images/graph-2.PNG "Graph Example (credit geeksforgeeks")

Another similar example below


![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Graphs/Images/graph-3.PNG "Bipartite Graph Example (credit williamfiset")

# Complete Graph

A complete graph is a graph that has a unique edge for every single node. This graphs are considered the worst case of a graphs as certain graphs have

Take a look of an example below.

![alt text](https://github.com/MK-1729/PyAlgo/blob/main/Graphs/Images/graph-4.PNG "Bipartite Graph Example (credit williamfiset")

# Problems In Graphs

1.Shortest Path 

Sloved with either BFS, Djikstra,Bellman-Ford,Floud Warshall and other algorithms.

2.Does a connectivity exist ?

Here we could use a Union Find data structure. We could also use BFS or DFS to check if 2 points are connected( which will
require more processing due to traversing the whole graph to check if the connection exist.

3.Negative Cycle exits ? 

Using algorithms like Bellman-Ford and Floyd-Warshall 

4.Finding Briges ?

An edge where if removed will result in 2 component graphs. This is the same as the articulation problem.

5. Minimum Spaning Tree

A subset of edges that are connected in an edge weighted graph which connects all vertices together. This however is done with minimum total edge weight. Kruskal and Prims are a good way to slove this.

Application such as networks and transportation use this.

6. Network Flo

How much can we flow through a network or test it's point before the network breaks.Example, how many car could pass through this network tranportation.

Algorithms like Ford-Fulkerson,Edmonds-Karp and Dinic Algorithm could be used.


# Algorithms 

## DFS

An important Algorithm and also fundamental search algortihm for graphs. A fundamental algorthims that when modified becomes more useful and powerful.

A Depth First Search (DFS) algorithm starts from a vertex v, then it traverses to its adjacent vertex (say x) that has not been visited before and mark as "visited" and goes on with the adjacent vertex of x and so on.

If at any vertex, it encounters that all the adjacent vertices are visited, then it backtracks until it finds the first vertex having an adjacent vertex that has not been traversed before. Then, it traverses that vertex, continues with its adjacent vertices until it traverses all visited vertices and has to backtrack again. In this way, it will traverse all the vertices reachable from the initial vertex v. -- Tutorialspoint

![Alt Text](https://pencilprogrammer.com/wp-content/plugins/phastpress/phast.php?service=images&src=https%3A%2F%2Fpencilprogrammer.com%2Fwp-content%2Fuploads%2F2018%2F10%2Fdfs.gif&cacheMarker=1599019524-266231&token=19a58266925e19f1)

Watch a video explanation with animation [here.](https://www.youtube.com/watch?v=7fujbpJ0LB4&ab_channel=WilliamFiset)

Here is a psuedocode.

```
n = number of node in the graph
g = adjacency list of the graph

visited=[False,False,..]
# could also use a set as it is unqiue

# Here DFS makes use of recursion as it is easier to understand and write compared to iterative

function dfs(current):
  visited[current) = True
  
  for neighbor in g[current]:
      if g[neighbor] == False:
          dfs(neighbor)

start=0
dfs(start)

```
Finding Connected Components in a graph by performing a DFS and we tag each node with a component it belongs to. This also could be done using a Union Find data structure.

```

```

## BFS

Also another important algorithm. Most commonly used for finding the shortest path for unweighted graphs.

The Breadth First Search (BFS) traversal is an algorithm, which is used to visit all of the nodes of a given graph. In this traversal algorithm one node is selected and then all of the adjacent nodes are visited one by one. After completing all of the adjacent vertices, it moves further to check another vertex and checks its adjacent vertices again.

An important data structure that is needed to carry this out is using a queue. Where, the neighbouring nodes on each layer is added into the queue and pop of when done. The condition where we have no more nodes will signify that we have visited all the graph.

![Alt Text](https://pencilprogrammer.com/wp-content/uploads/2018/09/ezgif.com-optimize.gif)

For video animation and explanation check [this out](https://www.youtube.com/watch?v=oDqjPvD54Ss).

Here is a pseudocode on it.

```
n = number of node in the graph
g = adjacency list of the graph

visited=[False,False,..]
# could also use a set as it is unqiue

prev=[None,None...]
# here we let it be for tracking previous parent node although not needed for performing bfs

function bfs(current):
    q=queue data structure to perform enqeue and deque
    q.enqueue(cuurent)
    
    while != []: # not empty
        node=q.pop()
        
        for x in g[node]:
            if not in visited[x]:
                q.enqueue(x)
                visited[x]=True
                # here is to track the previous parent node
                prev[x]=node
                
    return prev

```

Here prev is not neccessary for performing bfs. However let expand the idea. Suppose we would like to track the path. This uses the data structure union find to achieve it.



```
function reconstructPath(s,e,prev):
  # s for start
  # e for end
  # prev is the tracked arrau union find data structure
  
  path=[] # array
  at=e
  while at != None:        
    path.insert(0,at)
    at = prev[at]
   
   # check if they belong to the same connected component or are equal
   if path[0] == s:
      return path
   return []
 ```    
   

## Complexity

Algorithms         | Complexity(Time)
-------------------|-----------------
Depth-First Search |  O(V+E)
Breath-First-Search|  O(V+E)

Here the DFS visits every vertex and check every edge to see if it has been visited the time complexity will be O(V+E) where V is the number of vertices and E is the number of edges.

## Working on Grids using DFS and BFS

## Modified Algorithms

## Topological Sort

A topsort is such that some event or object is required first before proceeding to the next event or object. An example would be taking prerequisites for certain classes. If you did took subject A and passed , you are eligble to take subject B. If you could take B then you could take C.

This gives an ordering to the nodes in the graph. It is important to note that topological sorting is not unqiue. An example would be that you require to take A and then D before you can take subject C as an alternative path.

```

A----->B----->C
v+             ^
 \           /
  \         /
   \       /
    \     /
     \   / 
       D
```

However graphs that have a cycle could not possibly have a toposort. This is due to because in a cycle there is no where to start and end as you will keep looping in the cycle. Only DAG( Directed Acyclic Graph ) are graphs that have no cycles in it.

There are 2 methods to see if a graph has cycles ones is we use normal dfs to detect if the graph has a cycle and the other is using Tarjan Strongly connected components inorder to find this cycles. Tarjan connected component will be explained later on. For now let's get an understanding on using the DFS method.

The way how it works using dfs is by checking for back edges. Here we get at the ***current*** path or recursion were currently taking. So based on the image below we could see if we start from vertex 0 and move to vertex 1 and then 2, we add them to a stack. However we hit vertex 0 again, we take the node and compare it to what we have in the stack. This indicates that we do have a cycle. Once performing backtracking it is neccesary to pop of the stack for a new path.


![Alt Text](https://media.geeksforgeeks.org/wp-content/uploads/cycle.png)

```
n = number of node in the graph
g = adjacency list of the graph

recurStack=[]
visited=[False,False,..]
# could also use a set as it is unqiue

prev=[None,None...]
# here we let it be for tracking previous parent node although not needed for performing bfs

function isCycle(v,visited,recurStack):
      
      visited[v]=True
      # stack operations are push and pop
      recStack.push(v)
      
      for x in g[v]:
          if visited[x] == False:
              




```


Algorithms         | Complexity(Time)
-------------------|-----------------
Topological Sort   |  O(V+E)



## Djikstra

## Prim

## Kruskal

## Floyd_Warshall

## Tarjan and Kosaraju Algorithm



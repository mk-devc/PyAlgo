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

6. Network Flow

How much can we flow through a network or test it's point before the network breaks.Example, how many car could pass through this network tranportation.

Algorithms like Ford-Fulkerson,Edmonds-Karp and Dinic Algorithm could be used.


# Algorithms 

## DFS

An important Algorithm and also fundamental search algortihm for graphs. A fundamental algorthims that when modified becomes more useful and powerful.

A Depth First Search (DFS) algorithm starts from a vertex v, then it traverses to its adjacent vertex (say x) that has not been visited before and mark as "visited" and goes on with the adjacent vertex of x and so on.

If at any vertex, it encounters that all the adjacent vertices are visited, then it backtracks until it finds the first vertex having an adjacent vertex that has not been traversed before. Then, it traverses that vertex, continues with its adjacent vertices until it traverses all visited vertices and has to backtrack again. In this way, it will traverse all the vertices reachable from the initial vertex v. -- Tutorialspoint

![Alt Text](https://www.codesdope.com/staticroot/images/algorithm/dfs.gif)

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

We could also perform DFS iteratively as below. Only by replacing the recursive stack with our own stack. The way this works by storing in the stack as in the recursive version we would go to the next level by accessing the node in the end of the stack when we pop it out. Once where done with that level. We would go on to the next item in stack on the same level( backtracking to access another path on the same level). Once were done with that level we back track again and the process continues.

```
n = number of node in the graph
g = adjacency list of the graph

visited=[False,False,..]
stack=[] # for dfs

while stack.length:
    s=stack[-1]
    stack.pop()
    
    if visited[s] == False:
        visited[s]=True
        
    for neighbor in g[s]:
        if visited[neighbor]==False:
            stack.add(neighbor)


```
Finding Connected Components in a graph by performing a DFS and we tag each node with a component it belongs to. This also could be done using a Union Find data structure.





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
v             ^
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

recurStack=[False,False,...]
visited=[False,False,..]
# could also use a set as it is unqiue

prev=[None,None...]
# here we let it be for tracking previous parent node although not needed for performing bfs

function isCycle(v,visited,recurStack):
      
      visited[v]=True
      # stack operations are push and pop
      recurStack[v]=True
      
      for neighbor in g[v]:
          if visited[neighbor] == False:
              if isCycle(neighbor,visited,recursStack) ==True:
                  return True
          elif recurStack[neighbor] == True:
                  return True
                  
                  
      recurStack[v]=False
      return False
```



Now once we have confirmed its a DAG graph. We perform toposort which is basically adding the order of nodes as you recursively on the return backwards. 



![Alt Text](https://thumbs.gfycat.com/GraveHastyAmericancrow-size_restricted.gif)



```
function toposort(v,visited,stack,g):
     visited[v]=True
     
     for neighbor in g[v]:
          if visited[neighbor] == False:
              toposort(neighbor,visited,stack,g)
              
     stack.add(v)


function topologicalsort(n,g):
    n = number of node in the graph
    g = adjacency list of the graph

    visited=[False,False,..]
    # could also use a set as it is unqiue
    stack=[]
    
    
    for i in range(n):
        if visited[i] == False:
            toposort(i,visited,stack,g)
    
    # reverse order to go from start to finish and not end to finish
    return stack[::-1]

```

Algorithms         | Complexity(Time)
-------------------|-----------------
Topological Sort   |  O(V+E)


## Single Source Shortest Path In DAG

Sloved pretty quick by using topological sorting to achieve an order and it will be then processed sequentially. Then later follows by relaxing each edge (updating to a better value or minimum value of the edge on that particular node).


![alt text](https://www.cpp.edu/~ftang/courses/CS241/notes/images/graph/bellman2.gif)

The above shows that we have a topo order of s-> A -> C -> B -> D -> t. We begin from node s to node t, finding its minimum weight along that path. Here we have an array dist for each node. This dist array stores the minimum cumulative sum of weight from starting node to the current node. In this array,we relabel our nodes from s to t as 0 to n-1.

By following the topo order we start at node s, we see that the 2 adjacent node are A and C. Hence in our distance array for minimum cumulative sum of weight from starting node to the current node, so we make array index 1 as 5 and array index 2 as -2. We then move on to node A based on the toposort, we find that only node B is its neighbour in the outward direction, Hence we update dist array index 3 to 1. We now move to node C and we then discover our neighbors are node A and node B. Here we find that the current cumulative sum of weight from the starting node to the current node A that was recorded previously with a value 5 from node s to A is alot more compared to node s to C and finally to A. Hence we substitute it with the new value 0 at index 1 in the dist array. Same goes for B as previously it was 6 from s-> A -> B, but at node C we find that a distance of -2+4=2 is lower compared to 6. So we substitute the value in the dist array at index 2.

Below is the pseduocode on how this works. We used topological sorting that was done earlier to obtain its ordering and perform SSSP relaxing method to get minimum distance from s to t.

```
# class edge is used to help store weights of the next node being pointed from the current node.
class Edge:
      constructor(from,to,weight):
          self.from=from
          self.to = to
          self.weight=weight
         
```  
Algorithm for single shortest path.

```
# return an array of order of nodes
# number of nodes in graph , g is adjacencylist
topsortOrder = topologicalsort(n,g)

dist = [None]*n

for i in range(n):
    
    nodeIdx=topsortOrder[i]
    
    if dist[nodeIdx] == None:
        adjEdges=g[nodeIdx]
        
        if adjEdges != None:
           for edge in adjEdges:
                newDist=dist[nodeIdx]+edge.weight
                if dist[edge.to] == None: dist[edge.to]=newDist
                else: dist[edge.to] = minimum( newDist, dist[edge.to])
        
return dist

```
Algorithm            | Complexity(Time) | Complexity(Space)
---------------------|------------------|------------------
SSSP Algortihm       |      O(V+E)      |    O(V)



## Djikstra

Djikstra is a single source short path algorithm for graphs. However, it cant handle negative value. There are 2 reasons why Djikstra can't handle negative values. The first is that, it calculates the distance wrongly. This is because djikstra algorithm assumes that anything that pops of the min heap is the least accumulative path distance to the node. So just imagine youve got a minimal path to the node you have already visited, then a negative value to that node has an even higher minimal path. This cant be done because the algorithm already assumes that the next path it creates from that node that is visited is already gonna be more than the following node to be visited next ( makes sense if its all positive, negative however suddenly out of no where a higher minimal path emerges , its like planning a flight to another country and in the middle of the flight you find a lot more cheaper flight to the country of your destination). We can view this in an example below. 

![djikstra](https://pencilprogrammer.com/wp-content/uploads/2020/12/Graph-with-negative-weighted-edge.png)

From the image above we can get 


Algorithms           | Complexity(Time)
---------------------|-----------------
Djikstra Algortihm   |  O(E+log(V))


# Bellman & Ford

It is also a single source shortest path algorithm just like SSSP and Djikstra. The only difference between Djikstra and this algorithm is that it can hanlde negative edges and negative cycles. Thats because each time you find a new weight, it will get lower than the visited node in djikstra, if there is a negative cycles you will keep getting a lower weights which you will not be able to find the shortest path. It has also a time complexity of O(EV) which is higher compared to Djikstra's greedy method with complexity O(E+log(V)). 

[check out about negative weights here.](https://www.javatpoint.com/negative-weight-edges)

Lets take a look at how bellman & ford works out here.


![bellford](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fkeshiim.github.io%2F2017%2F12%2F21%2Ftranslations-interviews%2Fbellman-ford.gif%3Fraw%3Dtrue&f=1&nofb=1)

As you can see there is a diamond like shape above that represents a negative cycle. However this does not affect the algorithm bellman & ford brings. The pattern it goes is from each edge list that is iterated with the total number of edges. The reason as we saw is to let the effect of the relaxation take place thoughout the whole graph. As we look into the graphs we can see that the first most left node which is the starting node with a cost of 0 when relaxed adss to 3 to the node its going to. That only happens in the first iteration as the other edges have a weight of infinity + infinity which is not less that the given shortest distance to that node which is infinity. As you see the graph on each iteration, it is clear that progressing in getting the relaxed weight in each iteration. There are some cases if the edges in the edge list or adjacency list is in an order such that at one iteration it is able to get all the shortest paths to each node. We will see this again clearly explanied with an example below.


Here we have an example to explained the number of iterations. So for this why is it that we need to iterate V-1 over the loop is that to processs the whole distance of the graph. Say for example we had graph below.


```
# weight here points to the next node since its in a straight line, last one will be empty, unless its a self loop.
         O----->O----->O----->O
   
IDX      1      2      3      4
weight    2     3      5      
cost     inf    inf    inf    inf
```

so for the first iteration with all the nodes being a distance to positive infinity, taking the minimum distance from node 1 to node with index 2 will be 2 since the node index 1 has a distance of 0+2. This is lower compared to positive infinity so we sub that into the array d. 

Lets say now it jumps to edge on node index 3 to node index 4, infinity+5 still gives infinity and it is more compared to just positive infinity. So hence it will still be infinity. This is why we need to iterate it over again cause the edge list or the adjacency list does not gurantee and order. For example 1 --> 2 --> 3 --> 4 is how the edge list is processed. Maybe certain graphs in that order you will get the shortest distance in the graph. However, this does not apply to all graphs.

```
# n here represents the number of nodes
# d here is the distance array to each vertice
# relax the edge V-1 times where V represents the number of vertices and V-1 is the number of edges in the graph

d=[null,null,.....]
g=graph represented in edge list form ( v, u , weight)
s=source vertex

function initialize_distance(d,n):
      for idx,x in enumerate(d):  d[idx]=inf

function bellmanford(g,s,e):
      d[s]=0
      
      for x in V-1:
          for edge in g.edges:
            # we relax each edge in the graph, this part since we do not visit the graph in a certain order negative weights could be used.
            if d[edge.from] + edge.cost < d[edge.to]:
                d[edge.to]=d[edge.from]+edge.cost
                
       
      for x in V-1:
          for edge in g.edges
              # if it is able to relax more this shows there is a negative cycle.
              if d[edge.from] + edge.cost < d[edge.to]:
                d[edge.to]=-infinity # to indicate that there is a negative cycle
                
```            
            
            

Algorithms           | Complexity(Time)
---------------------|-----------------
Bellman&Ford         |  O(EV)     
      



## Floyd_Warshall

Shortest path between all pairs of nodes. The complexity of the is O(V^3) that uses the concept of dynamic programming. The floyd warshall algorithm with this complexity is only recommeneded to be used on smaller graphs as the complexity proves that it isnt efficient in processing larger graphs. This algorithm is similar to Bellman & Ford where it is able to detect negative cycles in the graph. 

Optimal way to use floyd warshall is in a 2D matrix adjacency matrix like the one represented below. As we can see the diagonal is 0 cause there is no self loops. The part where it is marked as X or could be Infinity shows there is no connection between those 2 distinct nodes.

![2D Matrix](https://ds055uzetaobb.cloudfront.net/brioche/uploads/OgxYZ1fX2o-floyd-warshall-problem2.png?width=1200)


The idea behind floyd warshall is to build up all intermediate routes between nodes say i and j. This will give us the optimal path. We first might wanna have an an extra variable that holds the information of k ( which is the intermediate node between i and j ). In this way we get to store say from i to k a minimum path and then j to k with a minimum path. If the previous recorded path lets say i to k-1 and k-1 to j is lesser then we remain it. However, think about it having the excess variable in a 3 dimensional array is overkill as we can use i to k or k to j that will be stored in a 2d array with only i to j as the variable as k could either be i or j for ( k to j ) or j ( i to k), where the minimum from one node to another is stored in the 2D array adjacency list.



Here it is important that k is the most outer for loop. The reason here is that we need to let all the routes i to j pass through all possible k. The one in the inner loops get access the most which is j. The "for" loop for i and j acts to find routes to i and j.[Here is a great video with examples on how Floyd Warshall works.](https://www.youtube.com/watch?v=4OQeCuLYj-4&ab_channel=MichaelSambol)


```
n=size of adjacency matrix
dp=memo table for All Pairs Shortest Path
next=to construct path

function setup(m):
  
      dp = empty matrix n x n
      next= empty matrix n x n
      
      for i in range(n):
          for j in range(n):
              dp[i][j]=m[i][j]
              if m[i][j] != infinty:
                # here we would wanna direct itself to form the path, if infinity there is no path.
                next[i][j]=j
                
                
function floydWarshall(m):
      # m is the adjacency matrix
      # setting up the next and dp 2d array
      setup(m)
      
      for k in range(n):
        for i in range(n):
          for j in range(n):
              if dp[i][j]> dp[i][k]+dp[k][j]:
                 dp[i][j] =  dp[i][k]+dp[k][j]
                 next[i][j]=next[i][k]

      # negative cycle detection
      for k in range(n):
        for i in range(n):
          for j in range(n):
              if dp[i][j]> dp[i][k]+dp[k][j]:
                 dp[i][j] = -infinity
                 

     return dp # All pairs shortest path


```


We saw there was a next array there we could use it to trace back the shortest path taken.

```

function reconstructPath(start,end):
          # check if there is a path between the end and the start node
          if dp[start][end]==-infinity: return path
          
          at
      



Looking at this from a Dynamic Programming prespective the problem with all pairs shortest path is to find the minimum weight between 2 pairs of nodes. 

![fw](https://rosettacode.org/mw/images/9/92/Floyd_warshall_graph.gif)

Given dp is the memoization( computer scientist funny way of saying memorization, also known as a look up table to store things like a memo.) table.

The relation to the subproblem is min( 2->1->3,2->3), which is min(4-2,3)=2, so given this example we would wanna have a relation that is min(dp[i][j],dp[i][k]+dp[k][j]).


## Prim

## Kruskal


## Tarjan and Kosaraju Algorithm



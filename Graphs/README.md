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

An edge where if removed will result in 2 component graphs


# Algorithms 

## DFS

## BFS

## Djikstra

## Prim

## Kruskal

## Floyd_Warshall

## Tarjan and Kosaraju Algorithm



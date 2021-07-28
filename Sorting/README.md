# Sorting algorithms 

List of sorting algorithms is as from:

1. Merge Sort
2. Quick Sort
3. Shell Sort 
4. Insertion Sort
5. Insertion Sort with Binary Search
6. Tim Sort (Merge and Insertion Sort comvined )
7. Bubble Sort
8. Selection Sort
9. Cycle sort
10. Counting Sort
11. Heap Sort
12. Radix Sort
13. Pancake Sorting
14. Intro Sort( Quick Sort and Heap Sort )
15. Odd-Even Sort


# Bubble Sort


# Insertion Sort

Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part. ~ Geeks for Geeks

![alt text](https://blog.informaticalab.com/wp-content/uploads/2013/05/insertion-sort-example.gif)

The black boxes here represents the sorted half while the ones without any boxes or white represents the unsorted half. Here we compare the next position values to its previous
element in the array which belongs to the sorted part. If they previous element is more than the next element we swap them. This happens till we find that the previous value is lesser than the next or it meets the end of the array or both.

```
arr = [12, 11, 13, 5, 6]

i=1
l=len(arr)

while i < l:
      j=i-1
      k=i
      while arr[j] > arr[k] and j >=0:
            temp=arr[k]
            arr[k]=arr[j]
            arr[j]=temp
            k=j
            j-=1
            
      i+=1    
```
            
Complexity(Time) | Complexity(Space)
-------------    | -------------
O(N^2)           | O(1)
       

We could further improve this by performing a Binary Insertion Sort
 
 
 # Merge Sort
 <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Merge-sort-example-300px.gif/220px-Merge-sort-example-300px.gif" width="600" />


# Bucket Sort

AS the name states we place element into its respective buckets inorder to sort them. When place inside the bucket like for example a list of list, we sort them using insertion sort or other sorting algorithms. We then flatten it to form an array of elements that is sorted.

![alt text](https://upload.wikimedia.org/wikipedia/commons/6/61/Bucket_sort_1.png)


The image above we place each element in its bucket or array at that given array. We could use several hashing functions here. One of them, is we could use is a below
```
bucketsize=10
divider=ceil((maxvalue+1)/bucketsize)

# here we take the divisor to distribute the values uniformly across the array of list
j=floor(arr[i]/divider)
```

To store the values 
![alt text](https://upload.wikimedia.org/wikipedia/commons/3/39/Bucket_sort_2.png)

We perform sorting in each bucket. We later flattten them out into a 1d array with elements being sorted.

# Radix Sort

Radix sort is a non-comparative sorting algorithm. It avoids comparison by creating and distributing elements into buckets according to their radix( base 10 for numbers from 0 to 9). For elements with more than one significant digit, this bucketing process is repeated for each digit, while preserving the ordering of the prior step, until all digits have been considered. 

Here the algorithm goes through each position in the digit. For example, the number 92  which has 10's that is 2  or the 100's which is 9. Each position in this digit is assessed by each time across the whole array of numbers. The number of times it is assessed across it's position is determined by the largest number of digits in the array.
We store them in arrays ranging from 0 to 9 according to the base. Once done for one pass, we flatten them and the process repeats for the next leading digits


Most Radix sort for numbers are unable to handle negative values. Hence for this we use a method in [stackoverflow](
https://stackoverflow.com/questions/15306665/radix-sort-for-negative-integers/15306692#15306692)

# Counting Sort

Counting sort is an algorithm for sorting a collection of objects according to keys that are small positive integers; that is, it is an integer sorting algorithm. It operates by counting the number of objects that possess distinct key values, and applying prefix sum on those counts to determine the positions of each key value in the output sequence. Its running time is linear in the number of items and the difference between the maximum key value and the minimum key value, so it is only suitable for direct use in situations where the variation in keys is not significantly greater than the number of items. It is often used as a subroutine in radix sort, another sorting algorithm, which can handle larger keys more efficiently



```



Points to be noted: 
1. Counting sort is efficient if the range of input data is not significantly greater than the number of objects to be sorted. Consider the situation where the input sequence is between range 1 to 10K and the data is 10, 5, 10K, 5K. 
2. It is not a comparison based sorting. It running time complexity is O(n) with space proportional to the range of data. 
3. It is often used as a sub-routine to another sorting algorithm like radix sort. 
4. Counting sort uses a partial hashing to count the occurrence of the data object in O(1). 
5. Counting sort can be extended to work for negative inputs also.
6. 

Complexity(Time) | Complexity(Space)
-------------    | -------------
O(N+K)           | O(N)

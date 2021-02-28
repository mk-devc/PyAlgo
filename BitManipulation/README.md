# Bit Manipulation

To convert integer to binary number we use the python function bin() and we slice the inital first 2 digits.

Example:
```
bin(8)[2:] # prints '0b1000' ->slice to remove first 2 positions-> '1000'

```

Function to convert integer to binary recursively. As shown below

``` 

function toBinary(num):
    if num <=1:
       toBinary(num//2) # round down the division
       print num%2
       
```

# Bitwise Operations

![Credit: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/](https://github.com/MK-1729/PyAlgo/blob/main/BitManipulation/pic.PNG)



# Prefix Sum 
 
 An important concept to know, say we wanna add a list of numbers in an array. Example would be an array [1,2,3,4,5], when performing this addition from index 0 to index 3 , we add them like usual,1+2+3+4 to give the value 10. Now say we perform it at a larger range from 0 to 4. When doing this we would have to perform the operation (1+2+3+4) again then we add 5. A much better approach if we could store the prefix sums across a table to retrieve them. Below is a pseducode for the problem mentioned earlier.
 
 ```
 'function fillPrefixSum(arr,length,prefix_sum):
 
    # set first value in the prefix sum array to be the first value of the array
    # subsequently add them to get the values for the next index in the array till its filled
    prefix_sum[0] = arr[0]
    
    index <- 1
    
    for x in arr from index 1 to length:
        prefix_sum[index] <- prefix_sum[index-1] + arr[index]
        
    return prefix_sum
        
       
  arr = [1,2,3,4]
  prefix_sum=fillPrefixSum(arr,len(arr),[])
  # get from index 1 to 3
  
  result<-prefix_sum[3]-prefix[1]
```
    

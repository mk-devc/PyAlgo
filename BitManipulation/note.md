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




 

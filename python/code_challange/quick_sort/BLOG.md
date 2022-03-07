# Quick Sort

## Definition

Quicksort is a sorting algorithm that is based on divide and conquer where an array is divided into sub arrays be selecting a pivot element while dividing the array, the pivot element is in a way that elements less than are on the left and elements greater than that are on the right.

## Trace

### Sample Array

[8,4,23 ,42,16 ,15]

### Pass 1

In our array we select the last element to be out pivot which in this case in 15. We divide the array into two with 15 in the middle
[8 ,4 ,23, 15 ,42 ,16]

### Pass 2

We compare the values to the left if they are greater than if and if so move them to the right of 15 and if not leave them. We then compare the values to the right of 15 and move them appropriately. Though this process we create tow sub arrays one to the left of 15 and one to the right of 15
[ 8 ,4 ,15 ,23 ,42 ,16]

### Pass 3

We have successfully finished the first step of sorting. We can now sort the values of the two subarrays by use of last elements as new pivots elements appropriately.
[4,8,15 ,16,23,42]

### Pass 4

Since our array at this point is already sorted in ascending order, we can just return the array
[4, 8 ,15 ,16 ,23, 42]

## Efficiency

Time - 0(n log n)
Space – 0(n)

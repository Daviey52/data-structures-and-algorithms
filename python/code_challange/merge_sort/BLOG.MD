# Merge Sort

Merge sort can be defined as sorting algorithms using comparison based sorting by dividing and conquer. The idea is to break down the list into sub-list until each sub-list has max one element and merge all the sub-lists in reverse order to get the sorted sub-list and finally a single list which is sorted.

## Trace

Sample Array: [8,4,23,42,16,15]

## Pass 1

We divide the sample array into half(len/2):
[8,4,23 | 42 ,16, 15]

## Pass 2

We then divide the subdivision by half:
[8,4    23 | 42 16, 15 ]

## Pass 3

We still divide the subdivision further
[8    4   23 |   42   16   15]

## Pass 4

Now we start merging all the subdivisions with a solution to get the final solution
[4,8   23 | 16,42, 15 ]

## Pass 5

We continue with the merging of the subdivisions
[ 4,8 ,23 | 15,16,42]

## Pass 6

We complete the merging of the array and return the sorted array.
[4,8,15,16,23,42]

## Efficiency

Time:0(log n)
Space:0(n)

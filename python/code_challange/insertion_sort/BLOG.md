# Insertion Sort

This is an in-place comparison-base sorting algorithm. A sub-list is maintained which is always sorted. For instance, the lower part of an array is maintained to be sorted, an element which is to be ‘inserted’ in this sorted sub-list has to find it’s appropriate pace and then it has to be inserted there. The array is searched sequentially, and unsorted items are moved and inserted into the sorted sb-list.v

Trace
Sample Array: [8,4,23,42,16,15]

## Pass 1

[8,4,23,42,16,15]
During the first pass, we evaluate the value at index 0 and make no changes to the array since there are no current other comparison values

## Pass 2

[4,8,23,42,16,15]
During the second pass we compare values at index 0 and index 1. Since 8 is greater than 4, we move four to the left of 8(sort in ascending order). The other values remain the same.

## Pass 3

[4,8,23,42,16,15]
During the third pass we first evaluate values at index 1 and 2. Since 23 is greater than 8, no changes are made to the array.

## Pass 4

[4,8,23,42,16,15]
During the fourth pass, we first evaluate values at index 2 and 3. Since 42 is greater than 23, no changes are made to the array.

## Pass 5

[4,8,16,23,42,15]
During the fifth pass, we evaluate values at index 3 and 4. Since 16 is less that 42, we shift it to the left and compare it with value at index 2. Since 23 is greater than 16, we shift it to the left and compare it with value at index 1. Since 8 is less than 16, no more changes are made to the array.

## Pass 6

[4,8,15,16,23,42]
During the sixth pass, we evaluate values at index 4 and 5. Since 15 is less than 42, we shift it to the left. We then evaluate values at index 3 and 4, since 15 is less than 23, we shift it to the left. We the evaluate values at index 2 and 3. Since 15 is less than 16, we shift it to the left, We then evaluate values at index 1 and 2 and since 15 is larger than 8, no more changes occur to the array.

## Efficiency

### Time: 0(n^2)

Time will be linear depending on the length of array, or how random, reversed, or unique numbers it has.

### Space:0(1)

No additional space is being used. The array is sorted in place

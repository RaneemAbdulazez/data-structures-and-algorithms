# Challenge Summary
Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. See the following C implementation for details.
## Whiteboard Process
![Whiteboard](whiteboard.png)
## Approach & Efficiency
Big O(nlog(n))

## Solution
[code](merge_sort.py)


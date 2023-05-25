def heapify(Arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    # used to compare the element at the current node with 
    # its left child and right and determine if the child is larger.
    if left < n and Arr[left] > Arr[largest]:
        largest = left
    if right < n and Arr[right] > Arr[largest]:
        largest =right
    if i != largest:
        Arr[i], Arr[largest] = Arr[largest], Arr[i]
        heapify(Arr, n, largest)


Arr = [2,66,30,5,9,10]
n = len(Arr)

# Building a max-heap
for i in range(n//2-1, -1, -1):
    heapify(Arr, n, i) 

# Printing the max-heap result
for i in range(len(Arr)):
    print(Arr[i])
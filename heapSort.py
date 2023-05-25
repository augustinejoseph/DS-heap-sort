def heapify(Arr, n, i):
    left = 2*i +1
    right = 2*i +2
    largest = i
    if n > left and Arr[left] < Arr[largest]:
        largest = left
    if n > right and Arr[right ] < Arr[largest]:
        largest = right
    if i != largest:
        Arr[i], Arr[largest] = Arr[largest], Arr[i]
        heapify(Arr, n, i)


Arr = [2,66,30,5,9,10]
n = len(Arr)

# Heapify
for i in range(n, -1,-1):
    heapify(Arr, n, i)

# Printing the result
print("Heaped array is:")
for i in range(n):
    print(Arr[i])
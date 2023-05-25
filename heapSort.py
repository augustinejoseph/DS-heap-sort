# Heapify function
def heapify(Arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and Arr[left] > Arr[largest]:
        largest = left

    if right < n and Arr[right] > Arr[largest]:
        largest = right

    if largest != i:
        Arr[i], Arr[largest] = Arr[largest], Arr[i]
        heapify(Arr, n, largest)

# Heap sort
def heapSort(Arr):
    n = len(Arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(Arr, n, i)

    for i in range(n - 1, 0, -1):
        Arr[0], Arr[i] = Arr[i], Arr[0]
        heapify(Arr, i, 0)

Arr = [2, 66, 30, 5, 9, 10]
n = len(Arr)

heapSort(Arr)

# Printing the result
print("Sorted array:")
for i in range(n):
    print(Arr[i])

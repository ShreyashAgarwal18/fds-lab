def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp1)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        countingSort(arr, exp)
        exp *= 10
#quick sort
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

# Get user input for both sorting algorithms
user_input = input("Enter numbers separated by spaces for Radix Sort: ")
arr_radix = list(map(int, user_input.split()))

print("\nSorting using Radix Sort...")
radixSort(arr_radix)
print("Sorted array (Radix Sort):")
print(arr_radix)

user_input = input("\nEnter numbers separated by spaces for Quick Sort: ")
arr_quick = list(map(int, user_input.split()))


print("\nSorting using Quick Sort...")
quickSort(arr_quick, 0, len(arr_quick) - 1)
print("Sorted array (Quick Sort):")
print(arr_quick)

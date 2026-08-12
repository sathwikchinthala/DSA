def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


arr = list(map(int, input("Enter the elements: ").split()))

if arr == sorted(arr):
    print("Array is already sorted.")
else:
    print("Array is unsorted.")
    arr.sort()
    print("Array after sorting:", arr)

key = int(input("Enter the element to search: "))

result = binary_search(arr, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")

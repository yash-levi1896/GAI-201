# Binary search

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


Input = [1, 2, 3, 4, 5, 6]
target = 4

result = binary_search(Input, target)
print(result)  

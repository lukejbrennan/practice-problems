def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Choose a pivot element
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot
    
    # Recursively sort the left and right subarrays
    left = quick_sort(left)
    right = quick_sort(right)
    
    # Combine the sorted subarrays and pivot
    return left + middle + right

# Example usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = quick_sort(arr)
print(sorted_arr)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) //2 ] # choose pivot from the middle of the array
    left = [x for x in arr if x < pivot] # elements less than the pivot
    middle = [x for x in arr if x == pivot] # elements == to the pivot
    right = [x for x in arr if x > pivot] # elements greater than the pivot
    
    left = quick_sort(left)
    right = quick_sort(right)
    return left + middle + right



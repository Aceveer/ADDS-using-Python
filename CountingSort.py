def CountingSort(arr):
    # Find the maximum element in the array
    max_element = max(arr)
    
    # Create a list to store the count of each element
    count = [0] * (max_element + 1)
    
    # Count the occurrences of each element in the input array
    for num in arr:
        count[num] += 1
    
    # Update the count list to store the cumulative count of elements
    for i in range(1, max_element + 1):
        count[i] += count[i - 1]
    
    # Create a list to store the sorted result
    sorted_arr = [0] * len(arr)
    
    # Place the elements in their correct positions in the sorted array
    for num in arr:
        sorted_arr[count[num] - 1] = num
        count[num] -= 1
    
    return sorted_arr

# Test the CountingSort function
arr = [4, 2, 2, 8, 3, 3, 1]
print(CountingSort(arr))

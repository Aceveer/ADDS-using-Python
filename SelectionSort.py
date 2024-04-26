def SelectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if(arr[j] < arr[min]):
                min=j
        arr[i],arr[min] = arr[min],arr[i]
    return arr

arr = [1,5,3,8,2,9,7,6,0]

print(SelectionSort(arr))

# Selection Sort iterates through the array from the first element to the last.
# For each iteration, it considers the current element as the minimum.
# Then, it iterates through the rest of the array to find the minimum element.
# If it finds an element smaller than the current minimum, it swaps them.
# Finally, it returns the sorted array.
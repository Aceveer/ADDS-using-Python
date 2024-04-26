def BubbleSort(arr):
    for i in range(len(arr)): #Iterate through the array
        swapped = False # Flag to track if any swapping has been done in this iteration
        for j in range(0,len(arr)-i-1): # Inner loop iterates through the unsorted portion of the array
            if(arr[j]>arr[j+1]): # Check if the current element is greater than the next element
                arr[j],arr[j+1] = arr[j+1],arr[j] #Swap
                swapped = True # Set swapped flag to True indicating a swap has been performed
        if(swapped == False): # Check if no swaps were made in this iteration, indicating the array is sorted
            break
    return arr

arr = [1, 5, 3, 8, 2, 9, 7, 6, 0]
print(BubbleSort(arr))

def SelectionSort(arr):
    for i in range(len(arr)): #Run through the array
        min = i #Choose a starting point from the left
        for j in range(i+1,len(arr)): #Second Array to loop through the elements after and compare with min
            if(arr[j] < arr[min]): #Comparision
                min=j #As we keep going through the j-loop, we see what the smallest is and store it in min
        arr[i],arr[min] = arr[min],arr[i] #once we find the smallest in j-loop, we switch ith position with min position
    return arr

arr = [1,5,3,8,2,9,7,6,0]

print(SelectionSort(arr))

# Selection Sort iterates through the array from the first element to the last.
# For each iteration, it considers the current element as the minimum.
# Then, it iterates through the rest of the array to find the minimum element.
# If it finds an element smaller than the current minimum, it swaps them.
# Finally, it returns the sorted array.
def SelectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min],arr[i] = arr[i],arr[min]
    return arr
arr = [1,5,3,8,2,9,7,6,0]

print(SelectionSort(arr))

#Start from left
#Keep first element as min
#Search for element smaller than min and keep that as min
#Go till the end and replace value at position with min
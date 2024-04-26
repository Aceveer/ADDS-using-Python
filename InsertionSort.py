def InsertionSort(arr):
    for i in range(1,len(arr)): #Iterate through the array starting from 1st index
        j=i-1 #Store current index
        key = arr[i] #Store current value to compare
        while(j>=0 and key<arr[j]): #Move elements of arr 1 position ahead of key if greater
            arr[j+1]=arr[j] #This is where the movement happens
            j=j-1 #This just goes back to compare with previous smaller elements
        arr[j+1]=key #Key is placed at sorted position
    return arr

arr = [1, 5, 3, 8, 2, 9, 7, 6, 0]
print(InsertionSort(arr))

def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr

arr = [1, 5, 3, 8, 2, 9, 7, 6, 0]
print(BubbleSort(arr))

#Compares consecutive items
#Highest item bubbles to right
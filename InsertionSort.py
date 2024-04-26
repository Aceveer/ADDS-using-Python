def InsertionSort(arr):
    for i in range(1,len(arr)):
        j=i-1
        min = arr[i]
        while j>=0 and min<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=min
    return arr
arr = [1, 5, 3, 8, 2, 9, 7, 6, 0]
print(InsertionSort(arr))

#Consider sorted and unsorted arrays
#Start from 2nd element
#Consider 1st to be sorted
#Compare 1st and 2nd and sort
#Introduce 3rd element, compare with sorted items and place it in position
#j works backwards
def merge(arr1,arr2):
    i=0 #arr1
    j=0 #arr2
    result = []
    while i<len(arr1) and j<len(arr2): #check if i and j are within arr1 and arr2
        if arr1[i]<arr2[j]: #comparision
            result.append(arr1[i]) #add
            i=i+1 #next element
        else:
            result.append(arr2[j]) #add
            j=j+1 #next element

    #this is for any missed elements
    while i<len(arr1):
        result.append(arr1[i])
        i+=1

    while j<len(arr2):
        result.append(arr2[j])
        j+=1

    return result

def MergeSort(arr):

    if len(arr) <=1:
        return arr

    mid = len(arr)//2
    left = MergeSort(arr[:mid]) #sort left subarray
    right = MergeSort(arr[mid:]) #sort right subarray

    return merge(left,right)

arr = [1, 5, 3, 8, 2, 9, 7, 6, 0]
print(MergeSort(arr))
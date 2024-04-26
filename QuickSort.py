def Partition(array, low, high):
    pivot = array[high]
    i=low-1

    #Compare each element with pivot
    for j in range(low,high):
        if array[j] <= pivot:
            i=i+1 #if greater element found, swap it
            array[i],array[j] = array[j],array[i] #Swap
    #Swap greater element with pivot
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i+1

def Quicksort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = Partition(array, low, high)

        # Recursive call on the left of pivot
        Quicksort(array, low, pi - 1)

        # Recursive call on the right of pivot
        Quicksort(array, pi + 1, high)
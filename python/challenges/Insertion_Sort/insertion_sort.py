def insertion_sort(lst):
    sorted_array=[]
    # Traverse through 1 to len(lst)
    for i in range(1, len(lst)):

        key = lst[i]

        j = i-1
        while j >=0 and key < lst[j] :
          lst[j+1] = lst[j]
          j -= 1
          lst[j+1] = key


    for i in range(len(lst)):
        sorted_array.append(lst[i])
    return sorted_array
if __name__=="__main__":


    arr=[2,3,5,7,13,11]
    # 4,8,15,16,23,42

    # Reverse_sorted=[20,18,12,8,5,-2]
    # Few_uniques=[5,12,7,5,5,7]
    # Nearly_sorted: [2,3,5,7,13,11]


    insertion_sort(arr)

    # insertionSort(arr)
    # print ("Sorted array is:")





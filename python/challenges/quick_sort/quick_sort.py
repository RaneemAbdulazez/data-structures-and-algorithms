def quick_sort(lst,left,right):
    if left<right:
        partition_arr=partition(lst,left,right)
        quick_sort(lst,left,partition_arr-1)
        quick_sort(lst,right,partition_arr-1)



def partition(lst,left,right):
    i=left
    j=right-1
    pivot=right


    while i<j:
        while i<right and lst[i]<pivot:
            i+=1
            while j>left and lst[j]>pivot:

                j-=1

            if i<j:
                lst[i],lst[j]=lst[j],lst[i]

    if lst[i]>pivot:
            lst[i],lst[right]=lst[right],lst[i]

    return i




print("hello")
if __name__=="__main__":
    lst=[22,50,30,70,20,24,66]
    # quick_sort(lst,0,len(lst)-1)



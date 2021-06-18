def merge_sort(lst):
  # print("list=",lst)
  n=len(lst)
  if n>1:
    mid=n//2
    # print("mid=",mid)
    left=lst[0:mid]
    # print("left:",left)
    right=lst[mid:]
    # print("right:",right)
    # print("-"*50)

    merge_sort(left)
    merge_sort(right)

    Merge(left,right,lst)
  return lst


def Merge(left,right,lst):
    # print("right= ",right)
    # print("left= ",left)

    i=0
    j=0
    k=0
    while i<len(left) and j<len(right):
      # print(left[i],right[j])

      if left[i]<=right[j]:

        lst[k]=left[i]
        i+=1

      else:
        lst[k]=right[j]
        j+=1

      k+=1
    # print(lst)

    if i==len(left):
      # print("*"*50)
      for x in right[j:]:
        lst[k]=x
        k+=1
        i+=1

    else:
      # print("*"*50)

      for x in left[i:]:
        lst[k]=x
        k+=1
        j+=1

    return lst



if __name__=="__main__":
    lista=[20,18,12,8,5,-2]

    print(merge_sort(lista))



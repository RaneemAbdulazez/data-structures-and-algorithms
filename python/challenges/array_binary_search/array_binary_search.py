
def binary_search(lst,val):
  start_point=0
  end_point=len(lst)+1
  print(lst[start_point:end_point])

  while start_point<end_point:
    mid_point=(start_point+end_point)//2
    print(mid_point,'mid')


    if lst[mid_point]==val:
      return mid_point

    if lst[mid_point]<val:
      #5<8
      start_point=mid_point+1
      #2+1=3

      print(start_point,'start_point')

    else:
      print('end_point')
      end_point=mid_point
    # print(end_point,'end_point')

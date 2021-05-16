import math
def binary_search(lst, value):
    new_list =lst
    mid=midpint(len(new_list))


    while  len(new_list) :

        if value==new_list[mid]:
            return mid

        if value > new_list[mid]:
            new_list = new_list[mid:]
            mid=midpint(len(new_list))


        elif value < new_list[mid]:
            new_list = new_list[:mid]


            mid=midpint(len(new_list))
        else:
            return -1

    else:
        return 'empty'



def midpint(len2):
    if not len2 % 2:
        mid = len2 // 2

    else:
        mid = math.ceil(len2 // 2)

    return mid


print(binary_search([1,2,3,4,5], 2))

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

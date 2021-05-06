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

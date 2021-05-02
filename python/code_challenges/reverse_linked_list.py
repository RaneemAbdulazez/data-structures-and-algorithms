def reverse(my_list):

    if type(my_list) != list or len(my_list)==0:

        #  print ('not valid input')

         return 'not valid input'

    reverse = []

    for item in my_list:

            reverse.insert(0, item)
            print(reverse)

    return reverse




ranem=[]
reverse(ranem)


# var = [1,2,3]
# if type(var) != list:
#     print('hello')

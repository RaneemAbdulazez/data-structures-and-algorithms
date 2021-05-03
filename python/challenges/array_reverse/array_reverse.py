

def reverse(my_list):
    if type (my_list)!=list or len(my_list)==0:
            return 'not valid input'

    reverse = []
    for item in my_list:
        reverse.insert(0, item)
    return reverse




if __name__ == "__main__":
    riddle_index = 0

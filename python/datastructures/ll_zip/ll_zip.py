from datastructures.linked_list.linked_list import LinkedList

def zipLists(first, second):
     first = first
     second = second
     current1 = first.head
     
     current2 = second.head
     length1 =0
     length2 =0
     temp = {}
     while(current1):
        length1 += 1
        current1 = current1.next
     while(current2):
        length2 += 1
        current2 = current2.next
    # print("l1", length1 , "l2", length2)
     if length1 < length2:
       print("true")
       temp =first
       first = second
       second =temp
       current1 = first.head
       current2 = second.head
     linked_first = first.head
     linked_second = second.head
     while linked_first and linked_second:
            first_next = linked_first.next
            second_next = linked_second.next
            linked_second.next = first_next 
            linked_first.next = linked_second 
            linked_first = first_next
            linked_second = second_next
            second.head = linked_second
     return f'{first}'


     

# linked1 = LinkedList()
# linked1.append(1)
# linked1.append(3)
# linked1.append(2)

# linked2 = LinkedList()
# linked2.append("5")
# linked2.append("9")
# linked2.append(4)

# zipLists(linked1,linked2)
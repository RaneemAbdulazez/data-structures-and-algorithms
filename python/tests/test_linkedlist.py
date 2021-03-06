from datastructures.linked_list.linked_list import LinkedList 


def test_instance():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


#Add_First To Empty LinkedList
def test_LinkedList_insert():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(0)
    assert test_LinkedList.head.value == 0


#Add_ To Not Empty LinkedList From the beginning 
def test_LinkedList_insert_second_Test():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(0)
    assert test_LinkedList.head.value == 0
    test_LinkedList.insert(1)
    assert test_LinkedList.head.next.value == 0

#To Check if the LinkedList contain a node with specific value 
def test_LinkedList_includes():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(0)
    test_LinkedList.insert(1)
    assert test_LinkedList.includes(1) == True
    assert test_LinkedList.includes(100) == False

#To Check if the LinkedList contain a node with specific value 
def test__str__():
    test_LinkedList = LinkedList()
    test_LinkedList.insert('9')
    test_LinkedList.insert('1')
    test_LinkedList.insert('-')
    test_LinkedList.insert('D')
    test_LinkedList.insert('I')
    test_LinkedList.insert('V')
    test_LinkedList.insert('O')
    test_LinkedList.insert('C')
    test_LinkedList.insert('_')
    test_LinkedList.insert('0')
    test_LinkedList.insert('2')
    test_LinkedList.insert('0')
    test_LinkedList.insert('2')
    assert test_LinkedList.__str__() == "{ 2 } -> { 0 } -> { 2 } -> { 0 } -> { _ } -> { C } -> { O } -> { V } -> { I } -> { D } -> { - } -> { 1 } -> { 9 } -> NULL"


def test_kthFromEnd():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(5)
    test_LinkedList.insert(3)

    test_LinkedList.insert(2)

    test_LinkedList.insert('raneem')

    # test_LinkedList.append(88)
    print(test_LinkedList)
    actual = test_LinkedList.kth_from_the_end(1)
    excpected = 3
    assert excpected == actual

def test_kthFromEnd2():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(5)
    test_LinkedList.insert(3)

    test_LinkedList.insert(2)

    test_LinkedList.insert('raneem')
    actual = test_LinkedList.kth_from_the_end(15)

    excpected = 'Sorry, the value is larger than the linked list'
    assert excpected == actual

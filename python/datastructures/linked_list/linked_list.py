class Node:
  
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{{ {self.value} }}'

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self,value):
        new_node=Node(value)

        if not self.head:
            self.head=new_node
        else:
           new_node.next=self.head    
           self.head=new_node

    def includes(self, value):
        if not self.head:
            return False
        else:
            current_Node = self.head        
            while current_Node != None:
                if current_Node.value == value:
                    return True
                else:
                    current_Node = current_Node.next
            return False

    def __str__(self):

        current_Node = self.head
        print(current_Node)
        linkedList_Serise = ''
        while current_Node != None:
            linkedList_Serise += f'{current_Node} -> '
            current_Node=current_Node.next
        linkedList_Serise+= 'NULL'
        return linkedList_Serise


    def append(self, item):
        """Append item to the end of the list"""
        current = self.head
        previous = None
        pos = 0
        length = self.size()
        while pos < length:
            previous = current
            current = current.getNext()
            pos += 1
            new_node = Node(item)
            if previous is None:
                new_node.setNext(current)
                self.head = new_node
            else:
                previous.setNext(new_node)




    def kth_from_the_end(self, k):
        current = self.head
        count = 0

        while current.next:
            current = current.next
            count += 1

        if k > count:
            return 'Sorry, the value is larger than the linked list'
        if k > count:
            raise Exception('Sorry, the value is larger than the linked list')


        current = self.head

        for _ in range(count - k):
            current = current.next
        print(current.value)
        return current.value

    
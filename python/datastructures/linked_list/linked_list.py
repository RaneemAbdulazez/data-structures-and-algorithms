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

    
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


    # def append(self, item):
    #     """Append item to the end of the list"""
    #     current = self.head
    #     previous = None
    #     pos = 0
    #     length = self.size()
    #     while pos < length:
    #         previous = current
    #         current = current.getNext()
    #         pos += 1
    #         new_node = Node(item)
    #         if previous is None:
    #             new_node.setNext(current)
    #             self.head = new_node
    #         else:
    #             previous.setNext(new_node)


    def append(self, value):
            new_node = Node(value)
            current = self.head
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node


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

    def insert_after(self,node,new_node):
        node_1=Node(node)
        node_2=Node(new_node)
        if not self.head or not node_1.value or not node_2.value:
            return 'not valid'
        
        
        # set pointer to head
        current=self.head
        print (node_1.value, node_2.value ,current)
        while current and node_1.value!=current.value:
            current=current.next
            
        temp=current.next  #=5        
        current.next=node_2 #4
        while current: #3
            temp=temp.next #6
            current=temp
        return 'added'
    
    def swap_nodes(self,node1,node2):
        current=self.head
    
        while current:
            if current.value==node1:
                node1_pointer=current
            if current.value==node2:
                node2_pointer=current
            current=current.next
            if node1_pointer and node2_pointer:
                temp=node2_pointer
                
                


            
    # def insertAfter(self, value, newVal):
        
    #         new_node = Node(newVal)
    #         current = self.head
    #         if not self.head:
    #                 self.head = new_node
    #         else:
    #             current = self.head
    #             while current.next:
    #                 if current.next.value == value:
    #                     current = current.next
    #                     old_node = current.next
    #                     current.next = new_node
    #                     new_node.next = old_node
    #                     return  f' "{newVal}" added secssfuly...'
    #                 else:
    #                     current = current.next
                        
    #             return "this node is not exist!"


if __name__=="__main__":
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node5=Node(5)
    
    ll=LinkedList()
    ll.append(node1)
    ll.append(node2)
    ll.append(node3)
    ll.append(node5)
    # print(ll)
    ll.insert_after(3,4)
    # print(ll)
    
    
    
    
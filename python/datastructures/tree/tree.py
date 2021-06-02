from challenges.stacks_and_queues.stacks_and_queues import Queue

class Node :
    def __init__(self,val):
        self.val=val
        self.next=None
        
        
class Stack:
    def __init__(self ,node=None) :
        self.top=node
        
        
  
    def push(self, val):
        if not self.top:
            self.top = Node(val)
        else:
            node = Node(val)
            node.next = self.top
            self.top = node
                
            
        
    def __str__(self):
        current=self.top
        while current:
            print(current.val)
            current=current.next
            
        return "done"
        
        
        
            
            
    def pop(self):
        if self.if_empty():
            raise Exception("Empty") 
        temp=self.top
        self.top=temp.next
        temp.next=None
        
        return temp.val
        
                
    def if_empty(self):
        return not self.top
            
            
            
        
class Tnode:
    def __init__(self,val=None):
        self.val=val
        self.right=None
        self.left=None
        
        
class Binary_tree:

    def __init__(self,root=None):
        self.root=root      
        self.pre_order_list=[] 
        self.in_order_list=[]
        self.post_order_list=[]
    def pre_order(self):
    
        def walk(root):
            self.pre_order_list.append(root.val)
            if root.left:
                walk(root.left)
                
                
            if root.right:
                
                walk(root.right)
       
        walk(self.root)
        return self.pre_order_list
        
        
    def post_order(self):
        def rev_walk(root):
            # print(root.val)
            if root.left:
                # print(root.left.val)
                rev_walk(root.left)
                # print(root.val)
            if root.right:
                # print(root.right.val)
                rev_walk(root.right)
            print(root.val)
            self.post_order_list.append(root.val)
   
        rev_walk(self.root)
        return self.post_order_list
        
    
    def in_order(self):
        def rev_walk(root):
            # print(root.val)
            if root.left:
                # print(root.left.val)
                rev_walk(root.left)
                # print(root.val)
            print(root.val)
            self.in_order_list.append(root.val)
            if root.right:
                # print(root.right.val)
                
                rev_walk(root.right)
            
    
        rev_walk(self.root)
        print(self.in_order_list)
        return self.in_order_list
    
    def findMax(self):
        if self.root:
            self.maximum_value=self.root.val
            
        else:
            return "tree is empty"
            # print ("*"*50,type(self.root.left.val))
            
        def walk(root):
            if root.left:
                 walk(root.left)
            if self.maximum_value < root.val:
               self.maximum_value = root.val
            if root.right:
                walk(root.right)
        walk(self.root)
        return self.maximum_value
    
    def bread_first(self):
        # Use queque for FIFO
        self.bread_first_list = []
        queque = Queue()
        queque.enqueue(self.root)
        while not queque.is_empty():
            item = queque.dequeue()
            print(item.val)
            self.bread_first_list.append(item.val)

            if item.left is not None:
                queque.enqueue(item.left)


            if item.right is not None:
                queque.enqueue(item.right)

        return self.bread_first_list
                
    
class Binary_Search_Tree(Binary_tree):
    def __init__(self):
        self.root=None
        
    def add(self,val):
        if self.root is None:
            self.root=Tnode(val)
        else:
            self._add(val,self.root)
            
    def _add(self,val,current_node):
        if val <current_node.val:
            if current_node.left is None:
                current_node.left=Tnode(val)
                
            else: 
                self._add(val,current_node.left)
        elif val>current_node.val:
            if current_node.right is None:
                current_node.right =Tnode(val)
            else:
                self._add(val,current_node.right)
        else:
            print("the value exists ")

    
    def contains(self,val):
        if self.root:
            found=self._contains(val,self.root)
            if found:
                return True
            return False
        else :
            return None  # tree is empty
        
    def _contains(self,val,current_node):
        if val>current_node.val and current_node.right:
            return self._contains(val,current_node.right)
        elif val<current_node.val and current_node.left:
            return self._contains(val,current_node.left)
        if val==current_node.val:
            return True
        
  
                 
                 
if __name__=="__main__":
   
    node1=Tnode("A")
    node1.left=Tnode("B")
    node1.right=Tnode("C")
    node1.right.left=Tnode("F")
    node1.left.right=Tnode("E")
    node1.left.left=Tnode("D")
    
    
    binar_tree=Binary_tree(node1)

    # binar_tree.add(5)
    # binar_tree.add(2)
    # binar_tree.add(10)
    # binar_tree.add(13)
    # binar_tree.add(15)
    
    # binar_tree.findMax()
    # print(binar_tree.contains(10))
    
    
    
    # binar_tree.post_order()
    # # binar_tree.breadth()
    print("----"*10)
    # binar_tree.pre_order()
    # print("----"*10)
    
    # binar_tree.in_order()
    
    
    
        
    
        
                
        























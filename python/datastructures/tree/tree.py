from typing import Counter


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
    def __init__(self,root):
        self.root=root      
        
        
        
        
    def pre_order(self):
        
        
        def walk(root):
            print(root.val)
            if root.left:
                walk(root.left)
            if root.right:
                walk(root.right)
        walk(self.root)
        
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
   
        rev_walk(self.root)
        
    
    def in_order(self):
        def rev_walk(root):
            # print(root.val)
            if root.left:
                # print(root.left.val)
                rev_walk(root.left)
                # print(root.val)
            print(root.val)
            if root.right:
                # print(root.right.val)
                
                rev_walk(root.right)
            
    
        rev_walk(self.root)
    
class Binary_Search_Tree:
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

                
   
 
        
        # # print(node.val)
        # if self.root is None:

        #     def add_root(self,node):
  
        #         self.root=node
                
        # elif self.root.right is None:
        #     add_right(node)
            
        # elif self.root.left is None:
        #     add_left(node)
            
            
        #     def add_right(self,node):    
        #         current=self.root
        #         while current:
        #             current=current.right
        #         self.root.right=node
        #         print(self.root.right.val)
                
                
        #     def add_left(self,node):    
        #         current=self.root
        #         while current:
        #             current=current.left
        #         self.root.left=node
        #         print(self.root.left.val)
      
    
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
        
        def findMax(root):
        
            # Base case
            if (root == None):
                return float('-inf')
        
            # Return maximum of 3 values:
            # 1) Root's data 2) Max in Left Subtree
            # 3) Max in right subtree
            res = root.data
            lres = findMax(root.left)
            rres = findMax(root.right)
            if (lres > res):
                res = lres
            if (rres > res):
                res = rres
            return res
        

                 
                 
if __name__=="__main__":
   
    node1=Tnode("A")
    node1.left=Tnode("B")
    node1.right=Tnode("C")
    node1.right.left=Tnode("F")
    node1.left.right=Tnode("E")
    node1.left.left=Tnode("D")
    
    
    binar_tree=Binary_tree()
    binar_tree.add(4)
    print(binar_tree.root.val)
     binar_tree(root)
    # binar_tree.add(2)
    # binar_tree.add(8)
    # binar_tree.add(10)
    # print(binar_tree.contains(10))
    
    
    
    # binar_tree.post_order()
    # # binar_tree.breadth()
    print("----"*10)
    # binar_tree.pre_order()
    # print("----"*10)
    
    # binar_tree.in_order()
    
    
    
        
    
        
                
        























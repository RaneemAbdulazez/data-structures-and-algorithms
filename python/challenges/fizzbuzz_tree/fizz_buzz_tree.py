from datastructures.tree.tree import *



def fizz_buzz_tree(tree):
    print(tree.pre_order())
    if not tree.root:
        return None
    "make a node for the tree"
    node=Fuzz_node(tree.root)
    new_tree=Binary_tree(node)
    k_tree_list= new_tree.pre_order()
    # print(k_tree_list)
    return k_tree_list


node_list=[]
def Fuzz_node(node):

    new_node=Tnode(node.val) 
    if node.left:
        new_node.left=Fuzz_node(node.left)
    if node.right:
        new_node.right=Fuzz_node(node.right)
    new_node.val=fizz_buzz(new_node.val)
    return new_node
    
def fizz_buzz(val):
    
    if val%3==0 and val%5==0:
        return'fizzBuzz'
    elif  val%3==0:
        return 'fizz'
    elif val%5==0:
        return'Buzz'
    else:
        return str(val)
   
    
if __name__=="__main__":
    nodi=Tnode(1)
    nodi.left=Tnode(2)
    nodi.right=Tnode(3)
    nodi.left.right=Tnode(4)
    nodi.left.left=Tnode(5)
    nodi.right.left=Tnode(15)
    tree=Binary_tree(nodi)
    # print(tree.pre_order())
    
    fizz_buzz_tree(tree)
    
    
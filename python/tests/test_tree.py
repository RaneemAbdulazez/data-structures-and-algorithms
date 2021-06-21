from datastructures.tree.tree import *

# from datastructures.tree.tree import *

#Can successfully instantiate an empty tree

def test_empty_tree():
    tree=Binary_tree()
    assert tree.root==None
    


# add the value the empty tree
def test_add_to_empty_tree(pr_BT): 
    pr_BT.add(4)
    assert pr_BT.root.value == 4
    
def test_preOrder(pr_BT):
    assert pr_BT.preOrder() == [4, -1, 3, 9, 6, 5, 8]

def test_inOrder(pr_BT):
    assert pr_BT.inOrder() == [-1, 3, 4, 5, 6, 8, 9]
    
def test_postOrder(pr_BT):
    assert pr_BT.postOrder() == [3, -1, 5, 8, 6, 9, 4]



# check the value the empty tree 
def test_empty_tree():
    pr_BT = BinarySearchTree()
    assert pr_BT.contains(55) == False
    

# check a values in ! empty tree
def test_contains_tree(pr_BT):
    assert pr_BT.contains(5) == True
    
# check a values in ! empty tree
def test_Not_contains_tree(pr_BT):
    assert pr_BT.contains(555) == False
    
def test_Not_find_maximum_value():
    bt_test =BinaryTree() 
    with pytest.raises(AssertionError):  # pass the Exception type or Exception for all Exceptions
        bt_test.find_maximum_value()
    
def test_find_maximum_value():
    bt_test =BinaryTree()
    bt_test.root = Node(6) 
    bt_test.root.right = Node(5)
    bt_test.root.left = Node(-1)
    bt_test.root.right.left = Node(7)
    bt_test.root.left.left = Node(10)
    bt_test.root.right.right = Node(3) 
    assert bt_test.find_maximum_value() == 10

@pytest.fixture
def pr_BT():
    binary_Tree = Binary_tree()
    binary_Tree.add(4)
    binary_Tree.add(9)
    binary_Tree.add(-1)
    binary_Tree.add(6)
    binary_Tree.add(3)
    binary_Tree.add(8)
    binary_Tree.add(5)
    return binary_Tree


# Can successfully instantiate a tree with a single root node
# Can successfully add a left child and right child to a single root node
# Can successfully return a collection from a preorder traversal
# Can successfully return a collection from an inorder traversal
# Can successfully return a collection from a postorder traversal



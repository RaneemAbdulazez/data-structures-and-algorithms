# from python.datastructures.tree.tree import Binary_tree
# from python.datastructures.tree.tree import Binary_Search_Tree, Binary_tree
from datastructures.tree.tree import Binary_Search_Tree,Binary_tree
import pytest 


    # binar_tree=Binary_Search_Tree()
    # binar_tree.add(4)
    # print(binar_tree.root.val)
    



# Can successfully return a collection from a preorder traversal
# Can successfully return a collection from an inorder traversal
# Can successfully return a collection from a postorder traversal

#Can successfully instantiate an empty tree
    
def test_empty_tree(tree_df):
    actual=tree_df.root.val
    excepted=4
 
    assert actual==excepted
    
    

# Can successfully instantiate a tree with a single root node




def test_single_root_tree():
    binar_tree=Binary_Search_Tree()
    binar_tree.add(2)
    actual=binar_tree.root.val
    excepted=2
    assert actual==excepted
    
    
    
# Can successfully add a left child and right child to a single root node
def test_left_and_right_and_left():
    
    

# def test_preOrder(tree_df):
#     assert tree_df.preOrder() == [4, -1, 3, 9, 6, 5, 8]

# def test_inOrder(tree_df):
#     assert tree_df.inOrder() == [-1, 3, 4, 5, 6, 8, 9]
    
# def test_postOrder(tree_df):
#     assert tree_df.postOrder() == [3, -1, 5, 8, 6, 9, 4]



# # check the value the empty tree 
# def test_empty_tree():
#     pr_BT = BinarySearchTree()
#     assert pr_BT.contains(55) == False
    

# # check a values in ! empty tree
# def test_contains_tree(pr_BT):
#     assert pr_BT.contains(5) == True
    
# # check a values in ! empty tree
# def test_Not_contains_tree(pr_BT):
#     assert pr_BT.contains(555) == False
    
# def test_Not_find_maximum_value():
#     bt_test =BinaryTree() 
#     with pytest.raises(AssertionError):  # pass the Exception type or Exception for all Exceptions
#         bt_test.find_maximum_value()
    
# def test_find_maximum_value():
#     bt_test =BinaryTree()
#     bt_test.root = Node(6) 
#     bt_test.root.right = Node(5)
#     bt_test.root.left = Node(-1)
#     bt_test.root.right.left = Node(7)
#     bt_test.root.left.left = Node(10)
#     bt_test.root.right.right = Node(3) 
#     assert bt_test.find_maximum_value() == 10

@pytest.fixture
def tree_df():
    # A, B, D, E, C, F
    binary_Tree = Binary_Search_Tree()
    binary_Tree.add(4)
    # binary_Tree.add(9)
    # binary_Tree.add(5)
    # binary_Tree.add(2)
    # binary_Tree.add(3)
    # binary_Tree.add(4)
    # binary_Tree.add(1)
    return binary_Tree
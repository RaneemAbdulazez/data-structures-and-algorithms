# # from python.datastructures.tree.tree import Binary_tree
# # from python.datastructures.tree.tree import Binary_Search_Tree, Binary_tree
from datastructures.tree.tree import Binary_Search_Tree,Binary_tree,Node,Tnode
import pytest 


#     # binar_tree=Binary_Search_Tree()
#     # binar_tree.add(4)
#     # print(binar_tree.root.val)
    



# # Can successfully return a collection from a preorder traversal
# # Can successfully return a collection from an inorder traversal
# # Can successfully return a collection from a postorder traversal

# #Can successfully instantiate an empty tree
    
def test_empty_tree():
    tree=Binary_tree()
    actual=tree.root
    excepted=None
 
    assert actual==excepted
    
    

# # Can successfully instantiate a tree with a single root node




def test_single_root_tree():
    binar_tree=Binary_Search_Tree()
    binar_tree.add(2)
    actual=binar_tree.root.val
    excepted=2
    assert actual==excepted
    
    
    
# # Can successfully add a left child and right child to a single root node

def test_right_left_tree(tree_df):
  
    excepted=[4, 2, 9]
    actual=[tree_df.root.val,tree_df.root.left.val,tree_df.root.right.val]
    assert actual==excepted

    
    

def test_pre_order(tree_df2):
    
    assert tree_df2.pre_order() == [4, 3, 2, 1, 6, 2]

def test_inOrder(tree_df2):
    assert tree_df2.in_order() == [2, 3, 1, 4, 2, 6]
    
def test_postOrder(tree_df2):
    assert tree_df2.post_order() == [2, 1, 3, 2, 6, 4]



def test_contains(tree_df):

    actual = [ tree_df.contains(4) , tree_df.contains(20) , tree_df.contains(1)]
    expected = [True, False, True]
    assert actual == expected 
    


def test_Not_find_maximum_value():
    bt_test =Binary_tree()
    # with pytest.raises(AssertionError):  # pass the Exception type or Exception for all Exceptions
    assert bt_test.findMax()=='tree is empty'
    
def test_find_maximum_value():
    bt_test =Binary_tree()
    bt_test.root = Tnode(6) 
    bt_test.root.right = Tnode(5)
    bt_test.root.left = Tnode(-1)
    bt_test.root.right.left = Tnode(7)
    bt_test.root.left.left = Tnode(10)
    bt_test.root.right.right = Tnode(3) 
    assert bt_test.findMax() == 10
    
def test_breadth_first(tree_breadth):
    actual = tree_breadth.bread_first()
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    assert actual == expected
    
    
@pytest.fixture
def tree_breadth():
    node1 = Tnode(2)
    node1.left = Tnode(7)
    node1.left.right = Tnode(6)
    node1.left.right.left = Tnode(5)
    node1.left.right.right = Tnode(11)
    node1.left.left = Tnode(2)
    node1.right = Tnode(5)
    node1.right.right = Tnode(9)
    node1.right.right.left = Tnode(4)
    binary_tree = Binary_tree(node1)
    return binary_tree 


@pytest.fixture
def tree_df():
    # A, B, D, E, C, F
    binary_Tree = Binary_Search_Tree()
    binary_Tree.add(4)
    binary_Tree.add(9)
    binary_Tree.add(5)
    binary_Tree.add(2)
    binary_Tree.add(3)
    binary_Tree.add(4)
    binary_Tree.add(1)
    return binary_Tree

@pytest.fixture
def tree_df2():
    # A, B, D, E, C, F
    node1=Tnode(4)
    node1.left=Tnode(3)
    node1.right=Tnode(6)
    node1.right.left=Tnode(2)
    node1.left.right=Tnode(1)
    node1.left.left=Tnode(2)
    binary_tree=Binary_tree(node1)
    return binary_tree
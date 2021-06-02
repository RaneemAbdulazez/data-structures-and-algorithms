# from challenges.fizzbuzz_tree.fizz_buzz_tree import *
from datastructures.tree.tree import *
from challenges.fizzbuzz_tree.fizz_buzz_tree import *



def test_make_a_tree(k_tree):
    actual=k_tree.root.val
    excepted=1
    assert actual==excepted
    
    
def test_preorder_a_tree(k_tree):
    actual=k_tree.pre_order()
    excepted= [1, 2, 5, 4, 3, 15]
    assert actual==excepted
    
    
def test_fizz_buzz(k_tree):
    actual=fizz_buzz_tree(k_tree)
    excepted= ['1', '2', 'Buzz', '4', 'fizz', 'fizzBuzz']
    assert actual==excepted
    
    
    
    
    
    
    
    
    
import pytest    
@pytest.fixture    
def k_tree():
    nodi=Tnode(1)
    nodi.left=Tnode(2)
    nodi.right=Tnode(3)
    nodi.left.right=Tnode(4)
    nodi.left.left=Tnode(5)
    nodi.right.left=Tnode(15)
    tree=Binary_tree(nodi)
    # print(tree.pre_order())
        
    # fizz_buzz_tree(tree)
    return tree
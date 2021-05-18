from datastructures.ll_zip.ll_zip import zipLists
from datastructures.linked_list.linked_list import LinkedList
# from datastructures.linked_list.linked_list import LinkedList

import pytest

def test_zipList(list_test1,list_test2):
    actual = zipLists(list_test1,list_test2)
    excpected = "{1} -> {5} -> {3} -> {9} -> {2} -> {4} ->  NULL"
    assert excpected == actual
def test_zipList_unbalance1(list_test1,list_test2):
    list_test1.append(4)
    actual = zipLists(list_test1,list_test2)
    excpected = "{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> {4} ->  NULL"
    assert excpected == actual
def test_zipList_unbalance2(list_test1,list_test2):
    list_test2.append(4)
    actual = zipLists(list_test1,list_test2)
    excpected = "{5} -> {1} -> {9} -> {3} -> {4} -> {2} -> {4} ->  NULL"
    assert excpected == actual
def test_zipList_None(list_test1):
    list_test2 = LinkedList()
    actual = zipLists(list_test1,list_test2)
    excpected = "{1} -> {3} -> {2} ->  NULL"
    assert excpected == actual

@pytest.fixture
def list_test1():
    linked1 = LinkedList()
    linked1.append(1)
    linked1.append(3)
    linked1.append(2)
    return linked1
@pytest.fixture
def list_test2():
    linked2 = LinkedList()
    linked2.append("5")
    linked2.append("9")
    linked2.append(4)
    return linked2
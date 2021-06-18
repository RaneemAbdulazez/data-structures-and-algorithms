from challenges.Insertion_Sort.insertion_sort import insertion_sort
import pytest

def test_insertion():
    input=[8,4,23,42,16,15]
    actual=insertion_sort(input)
    excepted=[4, 8, 15, 16, 23, 42]
    assert actual==excepted


def test_insertion_reverse_sorted():
    input=[20,18,12,8,5,-2]
    actual=insertion_sort(input)
    excepted=[-2, 5, 8, 12, 18, 20]
    assert actual==excepted



def test_insertion_few_uniques():
    input=[5,12,7,5,5,7]
    actual=insertion_sort(input)
    excepted=[5, 5, 5, 7, 7, 12]
    assert actual==excepted





def test_insertion_Nearly_sorted():
    input=[2,3,5,7,13,11]
    actual=insertion_sort(input)
    excepted=[2, 3, 5, 7, 11, 13]
    assert actual==excepted






# Sample Arrays
# In your blog article, visually show the output of processing this input array:

#

# For your own understanding, consider also stepping through these inputs:

# Reverse-sorted: [20,18,12,8,5,-2]
# Few uniques: [5,12,7,5,5,7]
# Nearly-sorted: [2,3,5,7,13,11]









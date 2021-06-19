
from challenges.quick_sort.quick_sort import quick_sort


# Reverse-sorted: [20,18,12,8,5,-2]
# Few uniques: [5,12,7,5,5,7]
# Nearly-sorted: [2,3,5,7,13,11]



def test_merging():
    # (start, end, array):
    input=[20,18,12,8,5,-2]
    actual=quick_sort(0, len(input) - 1, input)
    excepted=[-2, 5, 8, 12, 18, 20]
    assert actual==excepted

def test_few_uniques():
    input=[5,12,7,5,5,7]
    actual=quick_sort(0, len(input) - 1, input)
    excepted=[5, 5, 5, 7, 7, 12]
    assert actual==excepted

def test_nearly_sorted():
    input=[2,3,5,7,13,11]
    actual=quick_sort(0, len(input) - 1, input)
    excepted=[2, 3, 5, 7, 11, 13]
    assert actual==excepted




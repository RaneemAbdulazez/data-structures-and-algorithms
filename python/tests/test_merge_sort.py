from challenges.Merge_Sort.merge_sort import merge_sort

def test_merging():
    input=[20,18,12,8,5,-2]
    actual=merge_sort(input)
    excepted=[-2, 5, 8, 12, 18, 20]
    assert actual==excepted

def test_few_uniques():
    input=[5,12,7,5,5,7]
    actual=merge_sort(input)
    excepted=[5, 5, 5, 7, 7, 12]
    assert actual==excepted

def test_nearly_sorted():
    input=[2,3,5,7,13,11]
    actual=merge_sort(input)
    excepted=[2, 3, 5, 7, 11, 13]
    assert actual==excepted




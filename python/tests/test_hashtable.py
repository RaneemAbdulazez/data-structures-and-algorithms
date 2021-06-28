from datastructures.hashtable.hashtable import *
import pytest


def test_add():
    hash_map = Hashmap()
    hash_map.add('Jordan','Amman')
    actual = hash_map.__str__()
    expected = 'Jordan -> Amman'
    assert  actual == expected

def test_add_duplicate():
    hash_map1 = Hashmap()
    hash_map1.add('python','used for Machine learning')
    hash_map1.add('python','used for web development')
    actual = hash_map1.__str__()
    expected = 'python -> used for web development'
    assert  actual == expected


def test_get(hash_map_test):
    actual = (hash_map_test.get('python'),hash_map_test.get('Jordan'))
    expected = ('web development' , 'not found')
    assert  actual == expected

def test_contains(hash_map_test):
    actual = (hash_map_test.contains('python') , hash_map_test.contains('Ruby'))
    expected = (True, False)
    assert  actual == expected


@pytest.fixture
def hash_map_test():
    hash_map = Hashmap()
    hash_map.add('python','Machine learnign ')
    hash_map.add('python','web development')
    hash_map.add('javascript','web development')
    hash_map.add('java','mobile application')
    hash_map.add('C#','game development')

    return hash_map


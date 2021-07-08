import bin_tree
import pytest

arr = [5, 2, 4, 9, 3, 7, 6, 2, 4, 5, 4, 810, 16, 487, 52, 64]


@pytest.fixture
def tree():
    my_tree = bin_tree.BinTree()
    for i in arr:
        my_tree.insert(i)
    return my_tree


def test_insert1():
    new_tree = bin_tree.BinTree()
    assert new_tree.insert("5") is True


def test_insert2():
    new_tree = bin_tree.BinTree()
    assert new_tree.insert("A") is False


def test_search1(tree):
    for i in arr:
        assert tree.search(i) is not None


def test_search2(tree):
    assert tree.search(555) is None


def test_search3():
    new_tree = bin_tree.BinTree()
    assert new_tree.search(1) is None


def test_prefix1(tree):
    new_arr = tree.get_tree_prefix()
    for i in range(0, len(new_arr)-1):
        assert new_arr[i] < new_arr[i+1]


def test_prefix2():
    new_tree = bin_tree.BinTree()
    new_arr = new_tree.get_tree_prefix()
    assert new_arr is None


def test_postfix1(tree):
    new_arr = tree.get_tree_postfix()
    for i in range(0, len(new_arr)-1):
        assert new_arr[i] > new_arr[i+1]


def test_postfix2():
    new_tree = bin_tree.BinTree()
    new_arr = new_tree.get_tree_postfix()
    assert new_arr is None

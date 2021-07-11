import bin_tree
import pytest

inputs = [5, 2, 4, 9, 3, 7, 6, 2, 4, 5, 4, 810, 16, 487, 52, 64]


@pytest.fixture
def tree():
    my_tree = bin_tree.BinTree()
    for i in inputs:
        my_tree.insert(i)
    return my_tree


@pytest.fixture
def empty_tree():
    empty_tree = bin_tree.BinTree()
    return empty_tree


# testing the set up

def test_setup(empty_tree):
    assert isinstance(empty_tree, bin_tree.BinTree)
    assert empty_tree.root is None


# inserting in empty tree section

def test_insert_integer_to_empty_tree(empty_tree):
    assert empty_tree.insert(5) is True


def test_insert_real_number_to_empty_tree(empty_tree):
    assert empty_tree.insert(7.6) is True


def test_insert_integer_as_string_to_empty_tree(empty_tree):
    assert empty_tree.insert("5") is True


def test_insert_real_number_as_string_to_empty_tree(tree):
    assert tree.insert("7.6") is True


def test_insert_non_integer_as_string_to_empty_tree(empty_tree):
    assert empty_tree.insert("A") is False


# inserting in NON empty tree section

def test_insert_integer_to_non_empty_tree(tree):
    assert tree.insert(10) is True


def test_insert_real_number_to_non_empty_tree(tree):
    assert tree.insert(11.6) is True


def test_insert_existing_integer_to_non_empty_tree(tree):
    assert tree.insert(5) is True


def test_insert_integer_as_string_to_non_empty_tree(tree):
    assert tree.insert("10") is True


def test_insert_real_number_as_string_to_non_empty_tree(tree):
    assert tree.insert("11.6") is True


def test_insert_non_integer_as_string_to_non_empty_tree(tree):
    assert tree.insert("AB") is False


# Searching in empty tree section

def test_search_for_integer_in_empty_tree(empty_tree):
    assert empty_tree.search(9) is None


def test_search_for_real_number_in_empty_tree(empty_tree):
    assert empty_tree.search(9.5) is None


def test_search_for_integer_as_string_in_empty_tree(empty_tree):
    assert empty_tree.search("10") is None


def test_search_for_real_number_as_string_in_empty_tree(empty_tree):
    assert empty_tree.search("11.6") is None


def test_search_for_non_integer_as_string_in_empty_tree(empty_tree):
    assert empty_tree.search("akj") is None


# Searching in NON empty tree section

def test_search_for_non_existing_integer_in_non_empty_tree(tree):
    assert tree.search(10) is None


def test_search_for_existing_integer_in_non_empty_tree(tree):
    assert tree.search(9) is not None
    assert tree.search(9).value == 9


def test_search_for_non_existing_real_number_in_non_empty_tree(tree):
    assert tree.search(10.5) is None


def test_search_for_existing_real_number_in_non_empty_tree(tree):
    assert tree.search(9.5) is not None
    assert tree.search(9).value == 9


def test_search_for_non_existing_integer_as_string_in_non_empty_tree(tree):
    assert tree.search("10") is None


def test_search_for_existing_integer_as_string_in_non_empty_tree(tree):
    assert tree.search("9") is not None
    assert tree.search("9").value == 9


def test_search_for_non_existing_real_number_as_string_in_non_empty_tree(tree):
    assert tree.search("10.6") is None


def test_search_for_existing_real_number_as_string_in_non_empty_tree(tree):
    assert tree.search("9.6") is not None
    assert tree.search("9.6").value == 9


def test_search_for_non_integer_as_string_in_non_empty_tree(tree):
    assert tree.search("akj") is False


# test get ascending

def test_ascending_in_empty_tree(empty_tree):
    new_arr = empty_tree.get_tree_ascending()
    assert new_arr is None


def test_ascending_in_non_empty_tree(tree):
    new_arr = tree.get_tree_ascending()
    for i in range(0, len(new_arr) - 1):
        assert new_arr[i] < new_arr[i + 1]


@pytest.mark.parametrize("input1,input2", [([1, 2, 3, 4, 5, 6], [3, 2, 1, 6, 4, 5])])
def test_ascending_in_two_trees(input1, input2):
    new_tree = bin_tree.BinTree()
    new_tree2 = bin_tree.BinTree()
    for value in input1:
        new_tree.insert(value)
    for value in input2:
        new_tree2.insert(value)
    array1 = new_tree.get_tree_ascending()
    array2 = new_tree2.get_tree_ascending()
    for i in range(0, len(array1)):
        assert array1[i] == array2[i]


# test get descending

def test_descending_in_empty_tree(empty_tree):
    new_arr = empty_tree.get_tree_descending()
    assert new_arr is None


def test_descending_in_non_empty_tree(tree):
    new_arr = tree.get_tree_descending()
    for i in range(0, len(new_arr) - 1):
        assert new_arr[i] > new_arr[i + 1]


@pytest.mark.parametrize("input1,input2", [([1, 2, 3, 4, 5, 6], [3, 2, 1, 6, 4, 5])])
def test_descending_in_two_trees(input1, input2):
    new_tree = bin_tree.BinTree()
    new_tree2 = bin_tree.BinTree()
    for value in input1:
        new_tree.insert(value)
    for value in input2:
        new_tree2.insert(value)
    array1 = new_tree.get_tree_descending()
    array2 = new_tree2.get_tree_descending()
    for i in range(0, len(array1)):
        assert array1[i] == array2[i]


# test ordering section

@pytest.mark.parametrize("input_values", [[5, 4, 6], [10, 1, 15]])
def test_insert_order_in_empty_tree(empty_tree, input_values):
    for i in inputs:
        empty_tree.insert(i)
    assert empty_tree.root.value is not None
    assert empty_tree.root.left.value < empty_tree.root.value
    assert empty_tree.root.right.value > empty_tree.root.value


def test_insert_order_in_my_tree(tree):
    assert tree.root is not None
    assert tree.root.value == 5
    assert tree.root.left.value == 2
    assert tree.root.right.value == 9
    assert tree.search(9).left.value == 7
    assert tree.search(9).right.value == 810
    assert tree.search(487).left.value == 52
    assert tree.search(487).right is None
    assert tree.search(999) is None

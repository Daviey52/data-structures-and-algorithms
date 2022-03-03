

from merge_sort.merge_sort import merge_sort

import pytest


def test_merge_sort():
    array1 =[8,4,23,42,16,15]
    expected = [4,8,15,16,23,42]
    actual = merge_sort(array1)
    assert expected == actual

def test_merge_sort1():
    array1= [20,18,12,8,5,-2]
    expected = [-2,5,8,12,18,20]
    actual = merge_sort(array1)
    assert expected == actual

def test_merge_sort2():
    array1= [5,12,7,5,5,7]
    expected = [5,5,5,7,7,12]
    actual = merge_sort(array1)
    assert expected == actual

def test_merge_sort3():
    array1= [2,3,5,7,13,11]
    expected = [2,3,5,7,11,13]
    actual = merge_sort(array1)
    assert expected == actual

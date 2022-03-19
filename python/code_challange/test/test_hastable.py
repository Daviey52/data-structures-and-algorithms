from hashtable.hashtable import Hashtable
import pytest


def test_hash():
    hashtable=Hashtable()
    actual = hashtable.hash('gold')
    expected = 998
    assert actual == expected

def test_hash_empty():
    hashtable=Hashtable()
    actual = hashtable.hash('')
    expected = 0
    assert actual == expected

def test_hash_contains():
    hashtable=Hashtable()
    hashtable.add('gold', 'dav')
    actual = hashtable.contains('gold')
    expected = True
    assert actual == expected

def test_hash_get():
    hashtable=Hashtable()
    hashtable.add('gold','dav')
    actual = hashtable.get('gold')
    expected = 'dav'
    assert actual == expected




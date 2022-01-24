from stack_queue_brackets.brackets import Brackets
import pytest

def test_bracket_1():
    str1 = "[]"
    assert Brackets().validating_brackets(str1) == True


def test_bracket_1():
    str1 = "[]"
    assert Brackets().validating_brackets(str1) == True

def test_bracket_2():
    str1 = "{}(){}"
    assert Brackets().validating_brackets(str1) == True

@pytest.mark.skip("pending")
def test_bracket_3():
    str1 = "()[[Extra characters]]"
    assert Brackets().validating_brackets(str1) == True

@pytest.mark.skip("pending")
def test_bracket_4():
    str1 = "{}{Code}[Fellows](())"
    assert Brackets().validating_brackets(str1) == True

def test_bracket_5():
    str1 = "[({}]"
    assert Brackets().validating_brackets(str1) == False

def test_bracket_6():
    str1 = "(]("
    assert Brackets().validating_brackets(str1) == False

def test_bracket_7():
    str1 = "["
    assert Brackets().validating_brackets(str1) == False

def test_bracket_8():
    str1 = "{(}}"
    assert Brackets().validating_brackets(str1) == False



from calculator import *


def test_add_post_num():
    result = add(2,3)
    assert result == 5

def test_add_neg_num():
    result = add(-2,-3)
    assert result == -5

def test_sub_ne_num():
    result = sub(2,3)
    assert result == -1

def test_div_neg_num():
    result = div(6,3)
    assert result == 2
import pytest


@pytest.mark.xfail
def test_third_case():
    print(f"Inside {test_third_case.__name__}")
    assert 4 == 6, "4 is not equal to 6"


@pytest.mark.case1
def test_fourth_case():
    assert 6 < 9

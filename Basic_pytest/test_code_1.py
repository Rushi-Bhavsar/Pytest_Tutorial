import pytest


@pytest.mark.case
def test_first_case(func):
    print(func)
    print("Hello")


@pytest.mark.skip
def test_second_case():
    print("Welcome")

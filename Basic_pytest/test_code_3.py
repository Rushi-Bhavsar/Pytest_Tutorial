import pytest


@pytest.mark.usefixtures("func")
@pytest.mark.usefixtures("func1")
class TestCaseDemo:

    def test_fixture_case(self):
        print("Execution inside test_fixture_case")

    def test_fixture_case1(self):
        print("Execution inside test_fixture_case1")

    def test_fixture_case2(self):
        print("Execution inside test_fixture_case2")

    def test_fixture_case3(self):
        print("Execution inside test_fixture_case3")

    def test_fixture_case4(self):
        print("Execution inside test_fixture_case4")

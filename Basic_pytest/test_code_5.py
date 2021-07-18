import pytest


@pytest.mark.usefixtures("para_fixture")
class TestDemo3:

    def test_case_six(self, para_fixture):
        print(para_fixture, type(para_fixture))

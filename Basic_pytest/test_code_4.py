import pytest


@pytest.mark.usefixtures("load_data")
class TestCaseDemoSecond:
    def test_parametrized_fixture(self, load_data):
        print(type(load_data))
        for key in load_data.keys():
            print(key, '->', load_data[key])

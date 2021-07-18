import pytest
import json
from faker import Faker


@pytest.fixture()
def func():
    print("First I will be executed at method level")
    a = 5
    yield a
    print("\nLast I will be executed at method level")


@pytest.fixture(scope="class")
def func1():
    print("First I will be executed at class level")
    yield
    print("\nLast I will be executed at class level")


@pytest.fixture()
def load_data():
    print("Inside Load data function")
    return {"key1": "value1", "key2": "value2"}


@pytest.fixture(params=[('One', 'Two', 'Three'), ['One', 'Two', 'Three'], {"key": "value"}])
def para_fixture(request):
    return request.param


@pytest.fixture()
def load_url():
    with open('data.json', 'r') as f:
        dict_python = json.load(f)
    return dict_python


@pytest.fixture()
def create_dummy_data():
    fake = Faker()
    my_dict = {**{'name': fake.name(), 'job': fake.job()}}
    yield my_dict
    del my_dict
    print("\nDelete dictionary after every test case.")

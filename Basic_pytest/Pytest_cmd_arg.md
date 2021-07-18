### Command Line Argument.
- To run test file from CMD go to the directory where test_*.py file is present and use py.test
- To see detail logs use -v flag.
- To print console logs(print statements which are present in testcase function) on CMD use below -s flag.
- To run only specific testcase use -k and testcase name.
- To tag multiple testcase use mark decorator and to run them use -m flag.
- We can also use "or" while running the test using marker.
```shell
> py.test -m "case or case1" -v -s
```
- We can have fixture at method level i.e fixture will be executed for every method inside class.
- It's similar to setUp and tearDown method of UnitTest framework.
- We can also have fixture at class level i.e fixture will be executed once per class.
- It's similar to setUpClass and tearDownClass method of UnitTest framework.
- When we want some data from fixture, then we can use return keyword in the fixture.
- We can return anything from fixture.
- In case of parametrized fixture, the name of the parameter of the fixture function must be request only, 
  and we need to return request.param.

```python
import pytest


@pytest.fixture(params=[('One', 'Two', 'Three'), ['One', 'Two', 'Three'], {"key": "value"}])
def para_fixture(request):
    return request.param

```
- By default, pytest give information of failed cases only, if we want to short information 
  about all testcases then we can use -rA flag.

  
- Pytest record property. **https://stackoverflow.com/questions/57216970/write-pytest-test-function-return-value-to-file-with-pytest-hookimpl**
```python
# testcase file
import pytest
@pytest.mark.usefixtures('get_request_object')
class TestCode:

    @pytest.mark.django_db
    @pytest.mark.create_user
    def test_user_creation(self, customer_create_data, get_request_object, record_property):
        request = get_request_object
        data = customer_create_data['data']
        url = customer_create_data['create_customer_api_url']
        headers = customer_create_data['headers']

        response = request.post(url=url, data=data, headers=headers)
        assert response.status_code == 201
        record_property("pk", response.json()['pk'])
        record_property("username", response.json()['username'])
        record_property("auth_token", response.json()['token'])
```
```python
# conftest.py file
def pytest_runtest_teardown(item, nextitem):
    print(dict(item.user_properties))

```


### Daily Topics
- Write basic test case.
- Run testcase from CMD and pycharm.
- Use of -v, -s, -k flags of pytest.
- Run specific testcase using -k flag.
- Tag multiple testcase with mark Decorator and then run all those test case using -m flag.
- Skip a specific test case using mark.skip Decorator. We can also have skipif which work on some condition.
- Run the testcase but don't report then use mark.xfail Decorator.
- Pytest fixture and conftest.py file.
- method fixture and class fixture.
- Fixture with return keyword.  
- Parametrized fixture accepting single value and multiple value.
# Load Data from file into test case.
import requests
import pytest


@pytest.mark.usefixtures('load_url')
class TestUrls:

    @pytest.mark.get_url
    def test_get_url(self, load_url):
        assert bool(load_url) != False
        for key in load_url.keys():
            if key == "get_url":
                for url in load_url[key]:
                    print(url)
                    print(type(requests.get(url).json()))
                    assert requests.get(url).status_code == 200

    @pytest.mark.create_url
    def test_post_url(self, load_url, create_dummy_data):
        assert bool(load_url) != False
        for key in load_url.keys():
            if key == "post_url":
                for url in load_url[key]:
                    response = requests.post(url, data=create_dummy_data)
                    assert response.status_code == 201


    @pytest.mark.update_url
    def test_put_url(self, load_url, create_dummy_data):
        assert bool(load_url) != False
        for key in load_url.keys():
            if key == "put_url":
                for url in load_url[key]:
                    response = requests.put(url, data=create_dummy_data)
                    assert response.status_code == 200

    @pytest.mark.update_url
    def test_patch_url(self, load_url, create_dummy_data):
        assert bool(load_url) != False
        for key in load_url.keys():
            if key == "patch_url":
                for url in load_url[key]:
                    response = requests.put(url, data=create_dummy_data)
                    assert response.status_code == 200

    @pytest.mark.delete_url
    def test_delete_url(self, load_url):
        assert bool(load_url) != False
        for key in load_url.keys():
            if key == "delete_url":
                for url in load_url[key]:
                    assert requests.delete(url).status_code == 204

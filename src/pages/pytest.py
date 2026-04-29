import pytest
from django.test import Client

client = Client()

@pytest.mark.parametrize("url", ["/", "/about/"])
def test_public_pages_return_200(url):
    response = client.get(url)
    assert response.status_code == 200
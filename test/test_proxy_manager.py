import pytest
from unittest.mock import patch, MagicMock
from proxy_manager import ProxyManager

@pytest.fixture
def mock_requests():
    with patch('proxy_manager.requests.get') as mock_get:
        yield mock_get

def test_fetch_proxies(mock_requests):
    mock_response = MagicMock()
    mock_response.text = "proxy1:8080\nproxy2:8080"
    mock_requests.return_value = mock_response

    pm = ProxyManager('http://test-url.com')
    proxies = pm.fetch_proxies()

    assert proxies == ['proxy1:8080', 'proxy2:8080']
    mock_requests.assert_called_once_with('http://test-url.com')

def test_get_random_proxy():
    pm = ProxyManager('http://test-url.com')
    pm.proxies = ['proxy1:8080', 'proxy2:8080']

    proxy = pm.get_random_proxy()
    assert proxy in pm.proxies
import pytest
from unittest.mock import patch, MagicMock
from twitter_scraper import scrape_twitter_trends

@pytest.fixture
def mock_webdriver():
    with patch('twitter_scraper.webdriver.Chrome') as mock_chrome:
        driver_mock = MagicMock()
        mock_chrome.return_value = driver_mock
        yield driver_mock

def test_scrape_twitter_trends(mock_webdriver):
    mock_trends = [MagicMock(text='Trend 1\nDetails'), MagicMock(text='Trend 2\nDetails')]
    mock_webdriver.find_elements.return_value = mock_trends

    trends = scrape_twitter_trends()

    assert len(trends) == 2
    assert trends == ['Trend 1', 'Trend 2']
    mock_webdriver.get.assert_called_once_with("https://twitter.com/login")
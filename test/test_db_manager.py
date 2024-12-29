import pytest
from unittest.mock import patch, MagicMock
from db_manager import DBManager

@pytest.fixture
def mock_mongo_client():
    with patch('db_manager.MongoClient') as mock_client:
        yield mock_client

def test_insert_trends(mock_mongo_client):
    mock_collection = MagicMock()
    mock_mongo_client.return_value.__getitem__.return_value.__getitem__.return_value = mock_collection

    db_manager = DBManager('mongodb://test')
    trends = ['Trend1', 'Trend2', 'Trend3', 'Trend4', 'Trend5']
    ip_address = '127.0.0.1'

    result = db_manager.insert_trends(trends, ip_address)

    assert 'nameoftrend1' in result
    assert result['nameoftrend1'] == 'Trend1'
    assert result['ip_address'] == ip_address
    mock_collection.insert_one.assert_called_once()
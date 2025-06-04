from datetime import datetime, timedelta
from app import process_date_data

def test_process_date_data_basic():
    today = datetime.utcnow()
    items = [
        {'commit': {'author': {'date': (today - timedelta(days=i)).strftime('%Y-%m-%dT%H:%M:%SZ')}}}
        for i in range(3)
    ]
    result = process_date_data(items, lambda x: x['commit']['author']['date'])
    for i in range(3):
        date_str = (today - timedelta(days=i)).strftime('%Y-%m-%d')
        assert result[date_str] == 1

def test_process_date_data_empty():
    result = process_date_data([], 'created_at')
    assert len(result) == 31
    assert all(value == 0 for value in result.values())

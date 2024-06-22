import pytest
import sys
sys.path.append('/workspaces/aula08/')
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add(client):
    rv = client.post('/add', json={'a': 1, 'b': 2})
    assert rv.get_json() == {'result': 3}

def test_subtract(client):
    rv = client.post('/subtract', json={'a': 4, 'b': 2})
    assert rv.get_json() == {'result': 2}

def test_multiply(client):
    rv = client.post('/multiply', json={'a': 3, 'b': 2})
    assert rv.get_json() == {'result': 6}

def test_divide(client):
    rv = client.post('/divide', json={'a': 8, 'b': 2})
    assert rv.get_json() == {'result': 4}

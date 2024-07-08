import pytest
import json
import pathlib
from pydantic_spaceapi.v13 import SpaceAPIv13Model

@pytest.fixture
def valid_v13():
    file = pathlib.Path("tests/examples/valid_v13.json")  
    with open(file) as f:  
        return json.loads(f.read())

def test_working(valid_v13):
    """
    Check that we can parse a valid v13 definition
    """
    obj = SpaceAPIv13Model(**valid_v13)
    assert isinstance(obj, SpaceAPIv13Model)
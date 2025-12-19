import uuid
import pytest


@pytest.fixture
def random_str():
    rand_str = str(uuid.uuid4())
    return rand_str

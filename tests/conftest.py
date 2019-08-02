from gen3 import auth, submission, index
from cdisutilstest.code.conftest import (  # pylint: disable=unused-import
    indexd_server,
    indexd_client,
)
import pytest

# endpoint = 'https://endpoint.net/'
# auth = auth.Gen3Auth(endpoint, refresh_file="credentials.json")


#@pytest.fixture
#def sub():
#    return submission.Gen3Submission(endpoint, auth)
#
#
#@pytest.fixture
#def indexd():
#    return index.Gen3Index(endpoint + "index/", auth)


# for unittest with mock server
@pytest.fixture(scope="function")
def index_client(indexd_client):
    """ 
    Handles getting all the docs from an
    indexing endpoint. Currently this is changing from
    signpost to indexd, so we'll use just indexd_client now.
    I.E. test to a common interface this could be multiply our
    tests:
    https://docs.pytest.org/en/latest/fixture.html#parametrizing-fixtures
    """
    return indexd_client

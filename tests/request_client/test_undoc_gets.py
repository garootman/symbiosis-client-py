import pytest

from symbiosis_api_client import HttpxRequestClient, models


@pytest.fixture
def client():
    clnt = HttpxRequestClient()
    assert clnt.health_check() is True
    yield clnt
    clnt.close()


def test_client_get_swap_configs(client):
    swap_config = client.get_swap_configs()
    assert isinstance(swap_config, models.SwapConfigsResponseSchema)
    assert len(swap_config.root) > 20

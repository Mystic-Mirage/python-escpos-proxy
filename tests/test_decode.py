import pytest

from escpos_proxy.decode import parse_url
from escpos_proxy.types import Text


@pytest.mark.parametrize(
    "data",
    [
        [Text("hello")],
    ],
)
def test_decode_url(data, printer, url):
    assert parse_url(url) == (printer, data)

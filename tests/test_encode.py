import pytest

from escpos_proxy.encode import make_url
from escpos_proxy.types import Text


@pytest.mark.parametrize(
    "data",
    [
        "hello",
        ["hello"],
        [Text("hello")],
    ]
)
def test_make_url(data, printer, url):
    assert make_url(printer, data) == url

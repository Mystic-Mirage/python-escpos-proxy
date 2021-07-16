from pathlib import Path

import pytest

from escpos_proxy.printer import Printer


@pytest.fixture
def url():
    return (
        "escpos://proxy?ce7YvfHiNS6YKc4UAu4Dze5SWTDaVJFGUBdT6Ti68ao97fGox"
        "XYT5uKXDVqtCvGbCd6dr7mPvb4MBGkDUfAf7XszjZig5PWKvEtXcDAY5tfZamwyV"
        "NMu3ebNvZJHwW8u9dcKZnjiSfcKweD9tZsfcTcuBFqRMyzts8Mq8cvvxzU6TMr3d"
        "5zWHVbajbsGtwZ4fCUGGQqcb5ieGgzoRp3bt9GghLRQAoKXMApm"
    )


@pytest.fixture
def datadir():
    return Path(__file__).with_name("data")


@pytest.fixture
def printer(datadir):
    return Printer(datadir / "printer.yaml")
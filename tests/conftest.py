from pathlib import Path

import pytest

from escpos_proxy.printer import Printer


@pytest.fixture
def url():
    return (
        "escpos://proxy?4g5PQQr94icf85qfujn4fhzZhvzdwNiM1p3YNCcGBXZTeKmP3"
        "9KsLGEgX52EtGzLV399TWTxtHDJUU5wxsrjkiV4sznwsZnq18MrNoPVVD5QGwUoE"
        "avBsfrJUZNyjUM7RjnGaP1jSFsoDBVAJQYEfNYyw9NBv8RrE5bNPfuVLVb69zKyJ"
        "vxVDZEWGubu9V3LKtfo3T1EdzoLRJH34NRfKPYRJ2C"
    )


@pytest.fixture
def datadir():
    return Path(__file__).with_name("data")


@pytest.fixture
def printer(datadir):
    return Printer(datadir / "printer.yaml")

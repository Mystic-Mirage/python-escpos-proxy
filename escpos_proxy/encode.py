import zlib
from typing import List, Union
from urllib.parse import urlunparse

import base58
import bson

from .constants import NETLOC, PATH, SCHEME
from .printer import Printer
from .types import Image, Text


def make_url(printer: Printer, data: Union[List, str, bytes]):
    if isinstance(data, (str, bytes)):
        data = [data]

    encoded = []
    for item in data:
        if isinstance(item, str):
            item = Text(item)
        elif isinstance(item, bytes):
            item = Image(item)
        encoded.append(item)

    raw = dict(data=encoded, **printer)
    binary = bson.dumps(raw)
    compressed = zlib.compress(binary, level=9)
    qs = base58.b58encode_check(compressed).decode()

    return urlunparse((SCHEME, NETLOC, PATH, None, qs, None))

import urllib.parse
import zlib

import base58
import bson

from .constants import NETLOC, SCHEME
from .printer import Printer
from .types import Image, Text


def parse_url(url):
    parsed = urllib.parse.urlparse(url)
    if not all(
        [
            parsed.scheme == SCHEME,
            parsed.netloc == NETLOC,
        ]
    ):
        raise ValueError("Wrong url")
    elif parsed.query == "":
        raise ValueError("Empty query")

    binary = base58.b58decode_check(parsed.query)
    decompressed = zlib.decompress(binary)
    decoded = bson.loads(decompressed)

    data = decoded.pop("data")
    printer = Printer(**decoded)

    if isinstance(data, (bytes, str)):
        data = [data]

    parsed = []
    for item in data:
        if isinstance(item, str):
            item = Text(item)
        elif isinstance(item, bytes):
            item = Image(item)
        parsed.append(item)

    return printer, parsed

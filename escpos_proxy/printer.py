from copy import deepcopy
from functools import wraps
from io import BytesIO, StringIO
from pathlib import Path
from typing import Optional

import escpos.config
import escpos.printer
import yaml


def _print_method(m):
    @wraps(m)
    def wrapper(self, *args, **kwargs):
        self.open()
        kw = deepcopy(self.defaults.get(m.__name__)) or {}
        kw.update(kwargs)

        return m(self._printer, *args, **kw)

    return wrapper


class Page(dict):
    def __init__(self, width=42, bottom_margin=0):
        super().__init__(width=width, bottom_margin=bottom_margin)


class Printer(dict):
    def __init__(self, printer, defaults=None, page=None):
        if isinstance(printer, Path):
            with printer.open("rb") as f:
                kw = yaml.safe_load(f)
            printer = kw["printer"]
            defaults = kw.get("defaults")
            page = kw.get("page")

        defaults = defaults or {}
        page = Page(**page) if page else Page()
        super().__init__(printer=printer, defaults=defaults, page=page)

        self._printer: Optional[escpos.printer.Escpos] = None

    def open(self, force=False):
        if force or self._printer is None:
            fp = StringIO()
            yaml.safe_dump(self, fp)
            config_bytes = BytesIO(fp.getvalue().encode())

            config = escpos.config.Config()
            config.load(config_bytes)

            self._printer = config.printer()

    def close(self):
        if self._printer is not None:
            self._printer.close()

    def print(self, data):
        for item in data:
            item.print(self)

    image = _print_method(escpos.printer.Escpos.image)
    text = _print_method(escpos.printer.Escpos.text)
    textln = _print_method(escpos.printer.Escpos.textln)


del _print_method

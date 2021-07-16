from io import BytesIO
from pathlib import Path

import escpos.escpos
import PIL.Image


class Image(bytes):
    def __new__(cls, src):
        if isinstance(src, Path):
            src = src.read_bytes()
        return super().__new__(cls, src)

    def print(self, printer: escpos.escpos.Escpos, defaults):
        fp = BytesIO(self)
        img_source = PIL.Image.open(fp)
        printer.image(img_source=img_source, **defaults)


class Text(str):
    def print(self, printer: escpos.escpos.Escpos, defaults):
        printer.text(txt=self)

import sys
from config import S_C, S_J
from barcode_decoder import BarcodeDecoder

class BarcodeReader(object):
    def __init__(self, barcode_decoder: BarcodeDecoder) -> None:
        self.__barcode_decoder = barcode_decoder

    def read(self)->None:
        while True:
            c = sys.stdin.read(1)
            self.__barcode_decoder.decode(c)
            if c not in (S_C, S_J):
                break

            
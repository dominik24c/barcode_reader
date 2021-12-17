from stdin_reader import stdin_reader
from barcode_decoder import BarcodeDecoder

class BarcodeReader(object):
    def __init__(self, barcode_decoder: BarcodeDecoder) -> None:
        self.__barcode_decoder = barcode_decoder

    def read(self)->None:
        with stdin_reader() as line:
            self.__barcode_decoder.set_line(line)
            self.__barcode_decoder.decode()

            
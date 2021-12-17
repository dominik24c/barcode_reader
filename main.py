from barcode_decoder import BarcodeDecoder
from barcode_reader import BarcodeReader

def main()->None:
    barcode_reader = BarcodeReader(BarcodeDecoder())
    barcode_reader.read()
    
if __name__ == '__main__':
    main()
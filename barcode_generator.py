import random
import sys
import re

from config import DATA_DIR, S_C, S_J, SIZE_OF_GENERATED_DATA
from exceptions import InvalidFilename, ArgIsRequired

class BarcodeGenerator:
    @staticmethod
    def generate(filename: str):
        with open(DATA_DIR / filename,"w") as f:
            data = []
            for _ in range(SIZE_OF_GENERATED_DATA):
                res = random.choices([S_J,S_C])
                data.append(res[0])
            f.write("".join(data))



if __name__ == '__main__':
    if len(sys.argv) !=2:
        raise ArgIsRequired()

    arg = sys.argv[1]
    if not re.match("^.*.txt$",arg):
        raise InvalidFilename()
    BarcodeGenerator.generate(arg)
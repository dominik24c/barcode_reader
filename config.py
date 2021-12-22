import os
from pathlib import Path

BASE_DIR = Path(os.getcwd())
DATA_DIR = BASE_DIR / "data"

S_J = "J"
S_C = "C"
STATES = (S_J,S_C)

V_O = "0"
V_1 = "1"
V_EMPTY = "-"


SIZE_OF_GENERATED_DATA = 512


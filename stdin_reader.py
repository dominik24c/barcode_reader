import sys
from contextlib import contextmanager

@contextmanager
def stdin_reader()->str:
    for line in sys.stdin:
        yield line

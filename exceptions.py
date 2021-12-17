class BarCodeException(Exception):
    pass

class InvalidValuesInString(BarCodeException):
    """Throw if string doesn't contain only characters (S_J, S_C)"""
    pass

class InvalidFirstCharacter(BarCodeException):
    """Throw if first character is not white (S_J)"""
    pass

class InvalidLine(BarCodeException):
    """Throw if regex is not passed the test"""
    pass
class BarCodeException(Exception):
    pass

class InvalidFilename(BarCodeException):
    """Throw if filename extension is not .txt """
    pass

class ArgIsRequired(BarCodeException):
    """Throw if user doesnt passed one argument in script"""
    pass
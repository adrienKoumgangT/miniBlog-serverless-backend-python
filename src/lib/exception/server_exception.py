class NotFoundException(Exception):

    def __init__(self, message, code=None):
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self):
        if self.code is None:
            return f"NotFoundException: {self.message}"
        else:
            return f"NotFoundException: {self.code} - {self.message}"


class UnauthorizedException(Exception):

    def __init__(self, message, code=None):
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self):
        if self.code is None:
            return f"UnauthorizedException: {self.message}"
        else:
            return f"UnauthorizedException: {self.code} - {self.message}"


class InvalidClassException(Exception):

    def __init__(self, message, code=None):
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self):
        if self.code is None:
            return f"InvalidClassException: {self.message}"
        else:
            return f"InvalidClassException: {self.code} - {self.message}"


class InvalidKeyException(Exception):

    def __init__(self, message, code=None):
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self):
        if self.code is None:
            return f"InvalidKeyException: {self.message}"
        else:
            return f"InvalidKeyException: {self.code} - {self.message}"


class InvalidValueException(Exception):

    def __init__(self, message, code=None):
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self):
        if self.code is None:
            return f"InvalidValueException: {self.message}"
        else:
            return f"InvalidValueException: {self.code} - {self.message}"

class AuthenticationException(Exception):
    def __init__(self):
        super().__init__("INCORRECT CREDENTIALS")


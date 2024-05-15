class InvalidInputException(Exception):
    def __init__(self):
        super().__init__("Invalid inputs are given")
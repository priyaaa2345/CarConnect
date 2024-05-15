class AdminNotFoundException(Exception):
    def __init__(self):
        super().__init__("Theres no admin with the given id")
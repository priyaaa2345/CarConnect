
class ReservationException(Exception):
    def __init__(self):
        super().__init__("The specified vehicle id is already reserved..")
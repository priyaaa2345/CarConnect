class VehicleNotFoundException(Exception):
    def __init__(self):
        super().__init__("Theres no such vehicle with that id")
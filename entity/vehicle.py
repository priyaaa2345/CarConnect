class Vehicle:
    def __init__(self, VehicleID, Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate):
        self.__VehicleID = VehicleID
        self.__Model = Model
        self.__Make = Make
        self.__Year = Year
        self.__Color = Color
        self.__RegistrationNumber = RegistrationNumber
        self.__Availability = Availability
        self.__DailyRate = DailyRate

    def get_vehicle_id(self):
        return self.__VehicleID
    
    def set_vehicle_id(self, VehicleID):
        self.__VehicleID = VehicleID

    def get_model(self):
        return self.__Model
    
    def set_model(self, Model):
        self.__Model = Model

    def get_make(self):
        return self.__Make
    
    def set_make(self, Make):
        self.__Make = Make

    def get_year(self):
        return self.__Year
    
    def set_year(self, Year):
        self.__Year = Year

    def get_color(self):
        return self.__Color
    
    def set_color(self, Color):
        self.__Color = Color

    def get_registrationnumber(self):
        return self.__RegistrationNumber
    
    def set_registrationnumber(self, RegistrationNumber):
        self.__RegistrationNumber = RegistrationNumber

    def get_availability(self):
        return self.__Availability
    
    def set_availability(self, Availability):
        self.__Availability = Availability

    def get_dailyrate(self):
        return self.__DailyRate
    
    def set_dailyrate(self, DailyRate):
        self.__DailyRate = DailyRate

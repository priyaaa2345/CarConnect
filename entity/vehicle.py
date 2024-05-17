
class Vehicle:
    def __init__(
        self,
        VehicleID,
        Model,
        Make,
        Year,
        Color,
        RegistrationNumber,
        Availability,
        DailyRate,
    ):
        self.__VehicleID = VehicleID
        self.__Model = Model
        self.Make = Make
        self.Year = Year
        self.Color = Color
        self.__RegistrationNumber = RegistrationNumber
        self.Availability = Availability
        self.__DailyRate = DailyRate

    def get_vehicle_id(self):
        return self.__VehicleID
    
    def set_vehicle_id(self,VehicleID):
        self.__VehicleID=VehicleID

    def get_model(self):
        return self.__Model
    
    def set_model(self,Model):
        self.__Model=Model

    def get_registrationnumber(self):
        return self.__RegistrationNumber
    
    def set_registrationnumber(self,RegistrationNumber):
        self.__RegistrationNumber=RegistrationNumber

    def get_dailyrate(self):
        return self.__DailyRate
    
    def set_dailyrate(self,DailyRate):
        self.__DailyRate=DailyRate


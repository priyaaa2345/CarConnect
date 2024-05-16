import unittest

from dao.vehicle_service import VehicleService
from entity.vehicle import Vehicle
class TestInterestModule(unittest.TestCase):
    # Setup: Arrange
    def setUp(self):
        self.vehicle_service = VehicleService()

    def test_add_vehicle(self):
        vehicleId=111
        Model= " Phantom"
        Make=" Rolls Royce"
        Year= 2024
        Color="black"
        RegistrationNumber=1112
        Availability= 0
        DailyRate=14000000
        created_vehicle=self.vehicle_service.AddVehicle(vehicleId,Model,Make,Year,Color,RegistrationNumber,Availability,DailyRate)
        self.assertTrue(created_vehicle)  #to chek if try returns true


    
    def AddVehicle(self,vehicleId,Model,Make,Year,Color,RegistrationNumber,Availability,DailyRate):
        try:
            self.cursor.execute("insert into Vehilce values(?,?,?,?,?,?,?,?)",
                   (vehicleId,Model,Make,Year,Color,RegistrationNumber,Availability,DailyRate))
            self.conn.commit() #permanently stores the data..if it doenst done, we can undo things
            return True
        except Exception as e:
            print(e)
            return False
    
      
if __name__=="__main__":
    unittest.main()
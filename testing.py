import unittest
from dao.customer_service import CustomerService
from dao.vehicle_service import VehicleService
from entity.customer import Customer
from entity.vehicle import Vehicle
from exception.authentication_exception import AuthenticationException

class TestCustomerService(unittest.TestCase):
    def setUp(self):
        self.customer_service = CustomerService()
# # 1)
    # def test_customer_authentication_with_invalid_credentials(self):
    #     # Arrange
    #     customer_id = 1
    #     invalid_password = "day"

    #     # Act
    #     authentication_result = self.customer_service.Authenticate(customer_id, invalid_password)

    #     # Assert

    #     self.assertFalse(authentication_result, " invalid credentials.")

#    #2) 
#     def test_update_customer_information(self):
#         # Arrange: CreatING a new customer
#         new_customer_data = Customer(
#             CustomerID=16,
#             FirstName="kavya",
#             LastName="rocky",
#             Email="jkadhir@gmail.com",
#             PhoneNumber="3434827282",
#             Address="wes st,kanpur",
#             Username="jjays",
#             Password="rasd",
#             RegistrationDate="2022-03-01"
#         )
#         self.customer_service.RegisterCustomer(
#             new_customer_data.CustomerID,
#             new_customer_data.FirstName,
#             new_customer_data.LastName,
#             new_customer_data.Email,
#             new_customer_data.PhoneNumber,
#             new_customer_data.Address,
#             new_customer_data.Username,
#             new_customer_data.Password,
#             new_customer_data.RegistrationDate
#         )

#         # Act: UpdatING customer information
#         updated_customer_data = Customer(
#             CustomerID=16,
#             FirstName="kavya",
#             LastName="rocky",
#             Email="kadhir@gmail.com",
#             PhoneNumber="2323274837",
#             Address="xy st,chennai",
#             Username="jjays",
#             Password="rasd",
#             RegistrationDate="2022-03-01"
#         )
#         self.customer_service.UpdateCustomer(
#             updated_customer_data.PhoneNumber,
#             updated_customer_data.Address,
#             updated_customer_data.Email,
#             updated_customer_data.CustomerID
#         )

#         # Assert: Retrieving the data
#         updated_customer = self.customer_service.GetCustomerById(16)
#         self.assertEqual(str(updated_customer.PhoneNumber), "2323274837")
#         self.assertEqual(updated_customer.Address, "xy st,chennai")
#         self.assertEqual(updated_customer.Email, "kadhir@gmail.com")
#         self.assertEqual(updated_customer.Username, "jjays")
#         self.assertEqual(updated_customer.Password, "rasd")
#         self.assertEqual(updated_customer.RegistrationDate, "2022-03-01")

#     def tearDown(self):
#        

#         self.customer_service.DeleteCustomer(16)



class TestVehicleService(unittest.TestCase):
    def setUp(self):
        self.vehicle_service = VehicleService()
    # def test_add_vehicle(self):
    #     result = self.vehicle_service.AddVehicle(
    #         111,
    #         "Phantom",
    #         "Rolls Royce",
    #         2024,
    #         "Orange",
    #         3244,
    #         1,
    #         14000000
    #     )
    #     self.assertFalse(result)

    #     # Retrieve the added vehicle
    #     retrieved_vehicle = self.vehicle_service.GetVehicleById(111)
    #     # self.assertIsNotNone(retrieved_vehicle)

    #     # Check the details of the added vehicle
    #     self.assertEqual(retrieved_vehicle[0], 111)  # VehicleID
    #     self.assertEqual(retrieved_vehicle[1], "Phantom")  # Model
    #     self.assertEqual(retrieved_vehicle[2], "Rolls Royce")  # Make
    #     self.assertEqual(retrieved_vehicle[3], 2024)  # Year
    #     self.assertEqual(retrieved_vehicle[4], "Orange")  # Color
    #     self.assertEqual(retrieved_vehicle[5], 3244)  # RegistrationNumber
    #     self.assertEqual(retrieved_vehicle[6], )  # Availability
    #     self.assertEqual(retrieved_vehicle[7], 14000000)  # DailyRate

    def test_update_vehicle(self):
    #     # Add a new vehicle first
    #     self.vehicle_service.AddVehicle(
    #         111,
    #         "Phantom",
    #         "Rolls Royce",
    #         2024,
    #         "Orange",
    #         3244,
    #         0,
    #         14000000
    #     )

    #     # Update only DailyRate and Availability
        self.vehicle_service.UpdateVehicle(2400000,1,111)

        # Retrieve the updated vehicle
        retrieved_updated_vehicle = self.vehicle_service.GetVehicleById(111)
        # self.assertIsNotNone(retrieved_updated_vehicle)

        self.assertEqual(retrieved_updated_vehicle[6], 1)  # Availability
        self.assertEqual(retrieved_updated_vehicle[7], 2400000)  # DailyRate

        # Assert the other fields remain unchanged
        # self.assertEqual(retrieved_updated_vehicle[1], "Phantom")  # Model
        # self.assertEqual(retrieved_updated_vehicle[2], "Rolls Royce")  # Make
        # self.assertEqual(retrieved_updated_vehicle[3], 2024)  # Year
        # self.assertEqual(retrieved_updated_vehicle[4], "Orange")  # Color
        # self.assertEqual(retrieved_updated_vehicle[5], 3244)  # RegistrationNumber







































#     def test_add_new_vehicle(self):
#         # Arrange: Create a new vehicle object
#         new_vehicle = Vehicle(
#             VehicleID=109,  
#             Model="Phantom",
#             Make="Rolls Royce",
#             Year=2024,
#             Color="orange",
#             RegistrationNumber=324,
#             Availability=0,
#             DailyRate=14000000
#         )
        
#         # Act: Add the new vehicle
#         added_successfully = self.vehicle_service.AddVehicle(
#             new_vehicle.get_vehicle_id(),          
#             new_vehicle.get_model(),               
#             new_vehicle.get_make(),                
#             new_vehicle.get_year(),                 
#             new_vehicle.get_color(),                
#             new_vehicle.get_registrationnumber(),   
#             new_vehicle.get_availability(),        
#             new_vehicle.get_dailyrate()            
#         )

#         # Assert: Check if the vehicle was added successfully
#         self.assertTrue(added_successfully, "Failed to add new vehicle.")
        
#         # Check if the vehicle exists in the database
#         retrieved_vehicle = self.vehicle_service.GetVehicleById(new_vehicle.get_vehicle_id())
#         self.assertIsNotNone(retrieved_vehicle, "Vehicle not found in database after adding.")

#     def tearDown(self):
#         # Remove the added vehicle
#         self.vehicle_service.RemoveVehicle(109)  





# # 4)
#     def test_update_vehicle(self):
#         self.vehicle_service.AddVehicle(109,
#             "Phantom",
#             "Rolls Royce",
#             2024,
#             "orange",
#             324,
#             0,
#             14000000)
#         retrivedVehicle = self.vehicle_service.GetVehicleById(109)
#         updateVehicle = Vehicle(VehicleID=109,
#             Model="Phantom",
#             Make="Rolls Royce",
#             Year=2024,
#             Color="Orange",
#             RegistrationNumber=324,
#             Availability=1,
#             DailyRate=2400000)
#         self.vehicle_service.UpdateVehicle(updateVehicle)

#         # Retrieve the updated vehicle
#         retrieved_updated_vehicle = self.vehicle_service.GetVehicleById(109)

#         # Assert the fields have been updated
#         self.assertEqual(retrieved_updated_vehicle.Availability, 1)
#         self.assertEqual(retrieved_updated_vehicle.DailyRate, 2400000)

#         # Assert the other fields remain unchanged
#         self.assertEqual(retrieved_updated_vehicle.Model, "Phantom")
#         self.assertEqual(retrieved_updated_vehicle.Make, "Rolls Royce")
#         self.assertEqual(retrieved_updated_vehicle.Year, 2024)
#         self.assertEqual(retrieved_updated_vehicle.Color, "Orange")
#         self.assertEqual(retrieved_updated_vehicle.RegistrationNumber, 324)
#         # self.vehicle_service.UpdateVehicle(updateVehicle,retrivedVehicle[0])
#         # retrivedUpdatedVehicle = self.vehicle_service.GetVehicleById(109)
#         # self.assertEqual(retrivedUpdatedVehicle[4],"Brown")




#5)


    # def test_get_available_vehicles(self):
    #     vehicles = self.vehicle_service.GetAvailableVehicles()

    #     self.assertEqual(len(vehicles),6)
# #6)
    # def test_get_all_vehicles(self):
    #     all_vehicles = self.vehicle_service.GetAllVehicles()

    #     self.assertTrue(all_vehicles, "The list of all vehicles is empty.")

    #     self.assertEqual(len(all_vehicles), 11)


if __name__=="__main__":
    unittest.main()
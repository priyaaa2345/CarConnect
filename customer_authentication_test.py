import unittest
from dao.customer_service import CustomerService
from dao.vehicle_service import VehicleService
from entity.customer import Customer
from entity.vehicle import Vehicle
from exception.authentication_exception import AuthenticationException

class TestCustomerService(unittest.TestCase):
    def setUp(self):
        self.customer_service = CustomerService()
#1)
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
#         # Creating a new customer here
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
#         self.customer_service.RegisterCustomer('cus_id', 'Firs_name', 'las_name', 'mail', 'Phon', 'addr', 'Usernam', 'passwo', 'reg_date'

# )
#         self.customer_service.RegisterCustomer(
#         cus_id=new_customer_data.CustomerID,
#         Firs_name=new_customer_data.FirstName,
#         las_name=new_customer_data.LastName,
#         mail=new_customer_data.Email,
#         Phon=new_customer_data.PhoneNumber,
#         addr=new_customer_data.Address,
#         Usernam=new_customer_data.Username,
#         passwo=new_customer_data.Password,
#         reg_date=new_customer_data.RegistrationDate
#     )

#         # Updating customer information
#         updated_customer_data = Customer(
#             customer_id=16,
#             first_name="Kadhir",
#             last_name="rocky",
#             email="kadhir@gmail.com",
#             phone_number="2323274837",
#             address="xy st,chennai",
#             username="jkathir",
#             password="jkay",
#             registration_date="2024-04-01"
#         )
#         self.customer_service.UpdateCustomer(updated_customer_data)

#         # Retrieve updated customer information
#         updated_customer = self.customer_service.GetCustomerById(16)

#         # Assert
#         self.assertEqual(updated_customer.first_name, "Kadhir")
#         self.assertEqual(updated_customer.last_name, "rocky")
#         self.assertEqual(updated_customer.email, "kadhir@gmail.com")
#         self.assertEqual(updated_customer.phone_number, "2323274837")
#         self.assertEqual(updated_customer.address, "xy st,chennai")
#         self.assertEqual(updated_customer.username, "jkathir")
#         self.assertEqual(updated_customer.password, "jkay")
#         self.assertEqual(updated_customer.registration_date, "2024-04-01")


#     def tearDown(self):
#         self.customer_service.DeleteCustomer(16)




class TestVehicleService(unittest.TestCase):
    def setUp(self):
        self.vehicle_service = VehicleService()

#3rd in testing

    # def test_add_new_vehicle(self):
    #     # Arrange: Create a new vehicle object  (and it works...finallyyy🎉)
    #     new_vehicle = Vehicle(
    #         VehicleID=109,
    #         Model="Phantom",
    #         Make="Rolls Royce",
    #         Year=2024,
    #         Color="orange",
    #         RegistrationNumber=324,
    #         Availability=0,
    #         DailyRate=14000000
    #     )
    #     added_successfully = self.vehicle_service.AddVehicle(
    #         new_vehicle.VehicleID,
    #         new_vehicle.Model,
    #         new_vehicle.Make,
    #         new_vehicle.Year,
    #         new_vehicle.Color,
    #         new_vehicle.RegistrationNumber,
    #         new_vehicle.Availability,
    #         new_vehicle.DailyRate
    #     )


    #     self.assertTrue(added_successfully, "Failed to add new vehicle.")

    #     self.vehicle_service.RemoveVehicle(109)


    def test_update_vehicle(self):
        self.vehicle_service.AddVehicle(109,
            "Phantom",
            "Rolls Royce",
            2024,
            "orange",
            324,
            0,
            14000000)
        retrivedVehicle = self.vehicle_service.GetVehicleById(109)
        updateVehicle = Vehicle(VehicleID=109,
            Model="Phantom",
            Make="Rolls Royce",
            Year=2024,
            Color="Brown",
            RegistrationNumber=324,
            Availability=0,
            DailyRate=14000000)
        self.vehicle_service.UpdateVehicle(updateVehicle,retrivedVehicle[0])
        retrivedUpdatedVehicle = self.vehicle_service.GetVehicleById(109)
        self.assertEqual(retrivedUpdatedVehicle[4],"Brown")




#5)


#     def test_get_available_vehicles(self):
#         vehicles = self.vehicle_service.GetAvailableVehicles()

#         self.assertEqual(len(vehicles),6)
# #6)
#     def test_get_all_vehicles(self):
#         all_vehicles = self.vehicle_service.GetAllVehicles()

#         # self.assertTrue(all_vehicles, "The list of all vehicles is empty.")

#         self.assertEqual(len(all_vehicles), 11)


if __name__=="__main__":
    unittest.main()
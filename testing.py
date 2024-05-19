import unittest
from dao.customer_service import CustomerService
from dao.vehicle_service import VehicleService
from entity.customer import Customer
from entity.vehicle import Vehicle
from exception.authentication_exception import AuthenticationException

# class TestCustomerService(unittest.TestCase):
#     def setUp(self):
#         self.customer_service = CustomerService()
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

#3) 2 times op received

class TestVehicleService(unittest.TestCase):

    # def setUp(self):
    #     self.vehicle_service = VehicleService()
    #     # Add a vehicle once for all tests
    #     self.vehicle_service.AddVehicle(112, "Series", "Audi", 2018, "blue", 12323, 1, 5000)
    #     print("Vehicle 112 added successfully.")

    # def tearDown(self):
    #     # Remove the vehicle once after all tests
    #     self.vehicle_service.RemoveVehicle(112)
    #     print("Vehicle 112 removed successfully.")

    # def test_update_vehicle(self):
    #     print("Running test_update_vehicle")

    #     # Act: Update the existing vehicle's availability and daily rate
    #     update_success = self.vehicle_service.UpdateVehicle(6000, 0, 112)
    #     print("Vehicle 112 updated successfully.")

    #     # Retrieve updated vehicle details
    #     retrieved_vehicle = self.vehicle_service.GetVehicleById(112)

    #     # Assert: Check the updated values
    #     self.assertIsNotNone(retrieved_vehicle, "Vehicle not found in database after updating.")
    #     self.assertEqual(retrieved_vehicle[6], 0)  # Availability
    #     self.assertEqual(retrieved_vehicle[7], 6000)  # DailyRate


#op is fine::
#3) 4)
        def setUp(self):
            self.vehicle_service = VehicleService()
            # Add a vehicle once for all tests
            add_success = self.vehicle_service.AddVehicle(112, "Series", "Audi", 2018, "blue", 12323, 1, 5000)
            self.assertTrue(add_success, "Failed to add vehicle in setUp")

        def tearDown(self):
            # Remove the vehicle once after all tests
            remove_success = self.vehicle_service.RemoveVehicle(112)
            self.assertTrue(remove_success, "Failed to remove vehicle in tearDown")

        def test_update_vehicle(self):
            print("Running test_update_vehicle")

            # Act: Update the existing vehicle's availability and daily rate
            update_success = self.vehicle_service.UpdateVehicle(6000, 0, 112)
            self.assertTrue(update_success, "Failed to update vehicle.")

            # Retrieve updated vehicle details
            retrieved_vehicle = self.vehicle_service.GetVehicleById(112)

            # Assert: Check the updated values
            self.assertIsNotNone(retrieved_vehicle, "Vehicle not found in database after updating.")
            self.assertEqual(retrieved_vehicle[6], 0)  # Availability
            self.assertEqual(retrieved_vehicle[7], 6000)  # DailyRate


















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
   
    
#     def test_update_customer_information(self):
#         # Creating a new customer here
#         new_customer_data = Customer(
#             customer_id=15,
#             first_name="kavya",
#             last_name="rocky",
#             email="jkadhir@gmail.com",
#             phone_number="1332290450",
#             address="wes st,kanpur",
#             username="jjays",
#             password="rasd",
#             registration_date="2022-03-01"
#         )
#         self.customer_service.RegisterCustomer(new_customer_data)

#         # Updating customer information
#         updated_customer_data = Customer(
#             customer_id=15,
#             first_name="Kadhir",
#             last_name="rocky",
#             email="kadhir@gmail.com",
#             phone_number="9876543210",
#             address="xy st,chennai",
#             username="jkathir",
#             password="jkay",
#             registration_date="2024-04-01"
#         )
#         self.customer_service.UpdateCustomer(updated_customer_data)

#         # Retrieve updated customer information
#         updated_customer = self.customer_service.GetCustomerById(1)

#         # Assert
#         self.assertEqual(updated_customer.first_name, "Kadhir")
#         self.assertEqual(updated_customer.last_name, "rocky")
#         self.assertEqual(updated_customer.email, "kadhir@gmail.com")
#         self.assertEqual(updated_customer.phone_number, "9876543210")
#         self.assertEqual(updated_customer.address, "xyz st,chennai")
#         self.assertEqual(updated_customer.username, "jkathir")
#         self.assertEqual(updated_customer.password, "jkay")
#         self.assertEqual(updated_customer.registration_date, "2024-04-01")

#     def tearDown(self):
#         self.customer_service.DeleteCustomer(1)



# if __name__=="__main__":
#     unittest.main()
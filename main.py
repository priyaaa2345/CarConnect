from entity import Customer, Vehicle, Reservation, Admin
from dao import CustomerService,VehicleService,ReservationService,AdminService
# print(conn_str)
# conn = pyodbc.connect(conn_str)
# cursor = conn.cursor()

# cursor.execute("select 1")
print("database is connected")
print("Welcome to CarConnect 🚗")



class MainMenu:
    customer_service = CustomerService()
    vehicle_service=VehicleService()
    reservation_service=ReservationService()
    admin_service=AdminService()




    def Customer_menu(self):
        while True:
            print(
                """ Enter the option: 
                    1.Authentication
                    2.Get Customer detail by id
                    3.Get Customer by username
                    4. Register Customer
                    5. Update Customer
                    6. Delete Customer
                    7. Display all details
                    8.Back to main menu
                    """
            )
            choice = int(input("enter your choice: "))
            if choice == 1:
                customerid = int(input("enter the customer id : "))
                password = input("enter the password: ")
                self.customer_service.Authenticate(customerid, password)
                
                    
                
            elif choice == 2:
                custom_id = int(input("Enter the customer id to get the details: "))
                get_detail_by_id = self.customer_service.GetCustomerById(custom_id)
                print(" THe details are : ", get_detail_by_id)
            elif choice == 3:
                custom_name = input("enter the customer name to get the total details: ")
                get_detail_by_name = self.customer_service.GetCustomerByUsername(custom_name)
                print("the details are: ", get_detail_by_name)

            elif choice == 4:
                cus_id = int(input("Enter a customer id: "))
                Firs_name = input("Enter your first name: ")
                las_name = input("enter your last name: ")
                mail = input("enter your mail address: ")
                Phon = int(input("enter your phone num : "))
                addr = input("Enter your current address:")
                Usernam = input("Enter a valid username: ")
                passwo = input("enter a valid password: ")
                reg_date = input("Enter registration date: ")
                self.customer_service.RegisterCustomer(
                    cus_id, Firs_name, las_name, mail, Phon, addr, Usernam, passwo, reg_date
                )
                print("Customer Registration DONE!! ")

            elif choice == 5:
                phoon = int(input("enter your phone num to update : "))
                addre = input("Enter your current address:")
                emai = input("Enter your current email address: ")
                cust_id = int(input("Enter a customer id to make the updates: "))
                self.customer_service.UpdateCustomer(phoon, addre, emai, cust_id)
                print("updation done..")

            elif choice == 6:
                custu_id = int(input("Enter the customer id that needs to be deleted: "))
                self.customer_service.DeleteCustomer(custu_id)
                print("Deleted completely!!")
            elif choice == 7:
                result = self.customer_service.display_all()
                print("The available details are: ", result)
            elif choice == 8:
                break


    def Vehicle_menu(self):
        while True:
            print("""Enter your choice:
                1. Get details by Id
                2. Get available vehicles
                3. Add vehicle
                4. Update Vehicle
                5. Remove vehicle
                6. View All
                7. Back to main menu
                """)
            choice=int(input("enter your choice: "))
            if choice == 1:
                vehi_id= int(input("Enter the vehicle id to get details: "))
                detail=self.vehicle_service.GetVehicleById(vehi_id)
                print("The vehicle details are: ",detail)
            elif choice==2:
                avail=self.vehicle_service.GetAvailableVehicles()
                print("the available vehicles are: ",avail)
            elif choice==3:
                ve_id=int(input("Enter the vehicelId "))
                modl=input("Enter the model for the vehicle: ")
                make=input("enter the brand who made the vehicle: ")
                year=int(input("Enter the year of manufacturing: "))
                color=input("Enter the color of vehicel ")
                Register_num= int(input("Give the unique registration number: "))
                Availabi=int(input("Give the availability for the vehicle(1/0): "))
                Daily_rate=int(input("enter the daily rate for vehicle: "))
                self.vehicle_service.AddVehicle(ve_id,modl,make,year,color,Register_num,Availabi,Daily_rate)
                print("Vehicle added ✅ ")
            elif choice==4:   #error
                dail_rate=int(input("Enter the dailyrate to update: "))
                availab=int(input("Enter the data to update availability(1/0): "))
                veh_id=int(input("enter the vehicle id to change the data: "))
                self.vehicle_service.UpdateVehicle(dail_rate,availab,veh_id)
                print("updation done!")

            elif choice==5: 
                v_id=int(input("enter the vehicle id to delete from log: "))
                self.vehicle_service.RemoveVehicle(v_id)
                print("Removed succesfully..")

            elif choice==6:
                all_vehicle=self.vehicle_service.GetAllVehicles()
                print(" ",all_vehicle)

            elif choice==7:
                break
                



    def Reservation_menu(self):
        while True:
            print("""Enter an option
                1. Get details by id
                2. Get details by customer id
                3. Create a new Reservation
                4. Update Reservation
                5. Cancel Reservation
                6. Calculate total cost
                7. Back to  main menu
                """)
            choice= int(input("enter an option: "))
            if choice==1:
                res_id=int(input("Enter the reservation id to get the total details: "))
                detail= self.reservation_service.GetReservationById(res_id)
                print("the details are: ",detail)
            elif choice==2:
                cus_id=int(input("enter the customer id to get the total details: "))
                details=self.reservation_service.GetReservationsByCustomerId(cus_id)
                print("the details area: ",details)
            elif choice==3:
                re_id=int(input("Enter the reservation id: "))
                cu_id=int(input("Enter the customer id : "))
                ve_id=int(input("Enter the vehicle id pls: "))
                start_date=input("give the starting date of reservation: ")
                end_date=input("Pls enter the end date of reservation: ")
                tot_cost=int(input("Enter the total cost for reservation: "))
                status=input("Enter the status(completed/pending): ")
                self.reservation_service.create_reservation(re_id,cu_id,ve_id,start_date,end_date,tot_cost,status)
                print("reservation done")

            elif choice==4:
                cust_id=int(input("Enter the customer id : "))
                veh_id=int(input("Enter the vehicle id pls: "))
                stats=input("Enter the status(completed/pending): ")
                self.reservation_service.UpdateReservation(cust_id,veh_id,stats)
                print("updated")

            elif choice==5:
                resv_id=int(input("Enter the reservation id: "))
                self.reservation_service.CancelReservation(resv_id)
                print("deleted!!")

            elif choice == 6:
                resvv_id=int(input("Enter the reservation id: "))
                toto=self.reservation_service.CalculateTotalCost(resvv_id)
                print("the total cost is : ",toto)

            elif choice == 7:
                break


    def Authenticate(self, password):
        return self.password in password


    def Admin_menu(self):
        while True:
            print("""
                    1. GetAdminById
                    2. GetAdminByUsername
                    3. RegisterAdmin
                    4. UpdateAdmin
                    5. DeleteAdmin
                    6. View all
                    7. Back to main menu
                """
                )
            choice=int(input("Enter a choice: "))
            if choice == 1:
                ad_id=int(input("Enter the admin id to get details: "))
                result=self.admin_service.GetAdminById(ad_id)
                print("The details are: ",result)

            elif choice==2:
                ad_name=input("Enter the username to get the details: ")
                detail=self.admin_service.GetAdminByUsername(ad_name)
                print("the details are: ",detail)

            elif choice==3:
                add_id=int(input("enter the admin id to register: "))
                firs_name=input("Enter the first name: ")
                las_name=input("enter the last name: ")
                email=input("enter the email: ")
                ph= int(input("enter the phone number: "))
                usrnm=input("enter the valid username: ")
                paswd=input("Enter the password: ")
                role=input("enter the role(super_admin/fleet_manager): ")
                jndate=input("enter the join date: ")
                self.admin_service.RegisterAdmin(add_id,firs_name,las_name,email,ph,usrnm,paswd,role,jndate)
                print("Registered!!")
            elif choice ==4:
                firs_namee=input("Enter the first name: ")
                las_namee=input("enter the last name: ")
                emaill=input("enter the email: ")
                phh= int(input("enter the phone number: "))
                usrnmm=input("enter the valid username: ")
                paswdd=input("Enter the password: ")
                rolee=input("enter the role(super_admin/fleet_manager): ")
                jndatee=input("enter the join date: ")
                add_idd=int(input("enter the admin id to register: "))
                self.admin_service.UpdateAdmin(firs_namee,las_namee,emaill,phh,usrnmm,paswdd,rolee,jndatee,add_idd)
                print("Updated")
            elif choice ==5:
                a_id=int(input("Enter admin id to delete their detail: "))
                self.admin_service.DeleteAdmin(a_id)
                print("deleted successfully!!")
            elif choice==6:
                alll=self.admin_service.view_admin()
                print("the details area: ", alll)

            elif choice==7:
                break
    







# class DatabaseContext:
#     pass

# Class AuthenticationService:


# class ReportGenerator:
#     pass
def main():
    main_menu= MainMenu()
    while True:
        print(
            """
              1. Customer menu
              2. Vehicle menu
              3. Reservation menu
              4. Admin menu
              5. Exit
              
              """
        )
        choice = int(input("enter your choice:  "))
        if choice == 1:
            main_menu.Customer_menu()
        elif choice == 2:
            main_menu.Vehicle_menu()

        elif choice == 3:
            main_menu.Reservation_menu()

        elif choice == 4:
            main_menu.Admin_menu()
        elif choice == 5:
            break


if __name__ == "__main__":
    print("Welcome!!")
    main()
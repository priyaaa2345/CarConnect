import pyodbc

server_name = "MSI\SQLEXPRESS"
database_name = "carconnect"


conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)

print(conn_str)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

cursor.execute("select 1")
print("database is connected")
print("Welcome to CarConnect 🚗")


class Customer:
    def __init__(
        self,
        CustomerID,
        FirstName,
        LastName,
        Email,
        PhoneNumber,
        Address,
        Username,
        Password,
        RegistrationDate,
    ):
        self.CustomerID = CustomerID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.PhoneNumber = PhoneNumber
        self.Address = Address
        self.Username = Username
        self.Password = Password
        self.RegistrationDate = RegistrationDate


def Customer_menu():
    customer_service = CustomerService()
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
            if customer_service.Authenticate(customerid, password):
                print("Authentication successful.")
            else:
                print("Authentication failed. Incorrect customer ID or password.")
        elif choice == 2:
            custom_id = int(input("Enter the customer id to get the details: "))
            get_detail_by_id = customer_service.GetCustomerById(custom_id)
            print(" THe details are : ", get_detail_by_id)
        elif choice == 3:
            custom_name = input("enter the customer name to get the total details: ")
            get_detail_by_name = customer_service.GetCustomerByUsername(custom_name)
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
            customer_service.RegisterCustomer(
                cus_id, Firs_name, las_name, mail, Phon, addr, Usernam, passwo, reg_date
            )
            print("Customer Registration DONE!! ")

        elif choice == 5:
            phoon = int(input("enter your phone num to update : "))
            addre = input("Enter your current address:")
            emai = input("Enter your current email address: ")
            cust_id = int(input("Enter a customer id to make the updates: "))
            customer_service.UpdateCustomer(phoon, addre, emai, cust_id)
            print("updation done..")

        elif choice == 6:
            custu_id = int(input("Enter the customer id that needs to be deleted: "))
            customer_service.DeleteCustomer(custu_id)
            print("Deleted completely!!")
        elif choice == 7:
            result = customer_service.display_all()
            print("The available details are: ", result)
        elif choice == 8:
            break


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
        self.VehicleID = VehicleID
        self.Model = Model
        self.Make = Make
        self.Year = Year
        self.Color = Color
        self.RegistrationNumber = RegistrationNumber
        self.Availability = Availability
        self.DailyRate = DailyRate


def Vehicle_menu():
    vehicle_service=VehicleService()
    while True:
        print("""Enter your choice:
              1. Get details by Id
              2. Get available vehicles
              3. Add vehicle
              4. Update Vehicle
              5. Remove vehicle
              6. Back to main menu
              """)
        choice=int(input("enter your choice: "))
        if choice == 1:
            vehi_id= int(input("Enter the vehicle id to get details: "))
            detail=vehicle_service.GetVehicleById(vehi_id)
            print("The vehicle details are: ",detail)
        elif choice==2:
            avail=vehicle_service.GetAvailableVehicles()
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
            vehicle_service.AddVehicle(ve_id,modl,make,year,color,Register_num,Availabi,Daily_rate)
            print("Vehicle added ✅ ")
        elif choice==4:   #error
            dail_rate=int(input("Enter the dailyrate to update: "))
            availab=int(input("Enter the data to update availability(1/0): "))
            veh_id=int(input("enter the vehicle id to change the data: "))
            vehicle_service.UpdateVehicle(dail_rate,availab,veh_id)
            print("updation done!")

        elif choice==5: #error
            v_id=int(input("enter the vehicle id to delete from log: "))
            vehicle_service.RemoveVehicle(v_id)
            print("Removed succesfully..")

        elif choice==6:
            break
            


class Reservation:
    def __init__(
        self,
        ReservationID,
        CustomerID,
        VehicleID,
        StartDate,
        EndDate,
        TotalCost,
        Status,
    ):
        self.ReservationID = ReservationID
        self.CustomerID = CustomerID
        self.VehicleID = VehicleID
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.TotalCost = TotalCost
        self.Status = Status

def Reservation_menu():
    reservation_service=ReservationService()
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
            detail= reservation_service.GetReservationById(res_id)
            print("the details are: ",detail)
        elif choice==2:
            cus_id=int(input("enter the customer id to get the total details: "))
            details=reservation_service.GetReservationsByCustomerId(cus_id)
            print("the details area: ",details)
        elif choice==3:
            re_id=int(input("Enter the reservation id: "))
            cu_id=int(input("Enter the customer id : "))
            ve_id=int(input("Enter the vehicle id pls: "))
            start_date=input("give the starting date of reservation: ")
            end_date=input("Pls enter the end date of reservation: ")
            tot_cost=int(input("Enter the total cost for reservation: "))
            status=input("Enter the status(completed/pending): ")
            reservation_service.CreateReservation(re_id,cu_id,ve_id,start_date,end_date,tot_cost,status)
            print("reservation done")

        elif choice==4:
            cust_id=int(input("Enter the customer id : "))
            veh_id=int(input("Enter the vehicle id pls: "))
            stats=input("Enter the status(completed/pending): ")
            reservation_service.UpdateReservation(cust_id,veh_id,stats)
            print("updated")

        elif choice==5:
            resv_id=int(input("Enter the reservation id: "))
            reservation_service.CancelReservation(resv_id)
            print("deleted!!")

        elif choice == 6:
            resvv_id=int(input("Enter the reservation id: "))
            toto=reservation_service.CalculateTotalCost(resvv_id)
            print("the total cost is : ",toto)

        elif choice == 7:
            break


class Admin:
    def __init__(
        self,
        AdminID,
        FirstName,
        LastName,
        Email,
        PhoneNumber,
        Username,
        Password,
        Role,
        JoinDate,
    ):
        self.AdminID = AdminID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.PhoneNumber = PhoneNumber
        self.Username = Username
        self.Password = Password
        self.Role = Role
        self.JoinDate = JoinDate


def Authenticate(self, password):
    return self.password in password


def Admin_menu():
    admin_service=AdminService()
    while True:
        print("""
                1. GetAdminById
                2. GetAdminByUsername
                3. RegisterAdmin
                4. UpdateAdmin
                5. DeleteAdmin
              """
              )
        choice=int(input("Enter a choice: "))
        if choice == 1:
            ad_id=int(input("Enter the admin id to get details: "))
            result=admin_service.GetAdminById(ad_id)
            print("The details are: ",result)

        elif choice==2:
            ad_name=input("Enter the username to get the details: ")
            detail=admin_service.GetAdminByUsername(ad_name)
            print("the details are: ",detail)

        elif choice==3:
            pass
        elif choice ==4:
            pass

        elif choice ==5:
            adm_id=int(input("Enter admin id to delete their detail: "))
            admin_service.DeleteAdmin(adm_id)
            print("deleted successfully!!")
    


class CustomerService:

    def Authenticate(self, customerid, password):
        cursor.execute(
            """
                        select customerid,password from customer
                        where customerid=? and password=?
                       """,
            (customerid, password),
        )
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False

    def GetCustomerById(self, custom_id):
        cursor.execute(
            """
                     select * from customer
                     where customerid = ?
                       """,
            (custom_id),
        )
        return cursor.fetchall()

    def GetCustomerByUsername(self, custom_name):
        cursor.execute(
            """
                       select * from customer
                       where Username = ?
                       """,
            (custom_name), 
        )
        return cursor.fetchall()

    def RegisterCustomer(
        self, cus_id, Firs_name, las_name, mail, Phon, addr, Usernam, passwo, reg_date
    ):
        cursor.execute(
            """
                            insert into Customer values(
                            ?,?,?,?,?,?,?,?,?                       
                            )
                       """,
            (cus_id, Firs_name, las_name, mail, Phon, addr, Usernam, passwo, reg_date),
        )
        conn.commit()

    def UpdateCustomer(self, phoon, addre, emai, cust_id):  # error
        cursor.execute(
            """
                       update customer set PhoneNumber=?,
                       Address= ?,
                       Email=?,
                       where CustomerID = ?

                       """,
            (phoon, addre, emai, cust_id),
        )
        conn.commit()

    def DeleteCustomer(self, custu_id):
        cursor.execute(
            """
                       delete from customer
                       where customerid= ?
                       """,
            (custu_id),
        )
        conn.commit()

    def display_all(self):
        cursor.execute(
            """
select* from customer
                       """
        )
        result = cursor.fetchall()
        return result


class VehicleService:

    def GetVehicleById(self, vehi_id):
        cursor.execute(
            """
                            select * from Vehicle
                            where VehicleID= ?
                       """,
            (vehi_id),
        )
        return cursor.fetchall()
    
    def GetAvailableVehicles(self):
        cursor.execute(
            """                      
                        select * from Vehicle
                        where Availability= 1;

                       """,
        )
        return cursor.fetchall()

    def AddVehicle(
        self,
        ve_id,modl,make,year,color,Register_num,Availabi,Daily_rate
    ):
        cursor.execute(
            """
insert into Vehicle values(?,?,?,?,?,?,?,?)
                       """,
            (
                ve_id,modl,make,year,color,Register_num,Availabi,Daily_rate
            ),
        )
        conn.commit()

    def UpdateVehicle(self,dail_rate,availab,veh_id):
        cursor.execute(
            """
                       update Vehicle
                       set DailyRate= ?,
                       Availability=?,
                       where VehicleID=?
                       """,
            (dail_rate,availab,veh_id),
        )
        conn.commit()

    def RemoveVehicle(self, v_id):
        cursor.execute(
            """delete from Vehicle 
                       where vehicleID=?
                       """,
            (v_id),
        )
        conn.commit()

class ReservationService:
    def CalculateTotalCost(self, ReservationID):
        cursor.execute(
            """
                            select totalcost from Reservation
                            where reservationid=?
                    """,
            (ReservationID),
        )
        return cursor.fetchall()

    def GetReservationById(self,res_id):
        cursor.execute("""
                       select * from Reservation
                       where Reservationid= ?
                       """,(res_id))
        return cursor.fetchall()

    def GetReservationsByCustomerId(self,cus_id):
        cursor.execute("""
                       select * from Reservation
                       where CustomerID=?
                       
                       """,(cus_id))
        return cursor.fetchall()

    def CreateReservation(self,re_id,cu_id,ve_id,start_date,end_date,tot_cost,status):
        cursor.execute("""insert into Reservation values(?,?,?,?,?,?,?)
                       """,(re_id,cu_id,ve_id,start_date,end_date,tot_cost,status))
        conn.commit()

    def UpdateReservation(self,cust_id,veh_id,stats):
        cursor.execute("""
update Reservation
                       set CustomerID=?,
                       VehicleID=?,
                       Status=?
                       where ReservaionID=?
                       """,(cust_id,veh_id,stats))
        conn.commit()

    def CancelReservation(self,resv_id):
        cursor.execute("""
delete from Reservation
                       where ReservationID=?
                       """,(resv_id))
        
    def CalculateTotalCost(self,resvv_id):
        cursor.execute("""
select sum(TotalAmount) from Reservation
                           where ReservationID=?
                           """,(resvv_id))
        return cursor.fetchall()


class AdminService:
    def GetAdminById():
        cursor.execute("""
select * from Admin
                       where AdminID=?
                       """,())
        return cursor.fetchall()

    def GetAdminByUsername():
        cursor.execute("""select * from Admin
                       where Username=?""",())
        return cursor.fetchall()

    def RegisterAdmin():
        cursor.execute("""
insert into Admin values(?,?,?,?,?,?,?,?,?)
                       """,())
        conn.commit()
        

    def UpdateAdmin():
        conn.commit()
        

    def DeleteAdmin():
        cursor.execute("""
                       delete from Admin 
                       where AdminID=?
                       """,())
        conn.commit()


# class DatabaseContext:
#     pass

# Class AuthenticationService:


# class ReportGenerator:
#     pass


if __name__ == "__main__":
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
            Customer_menu()
        elif choice == 2:
            Vehicle_menu()

        elif choice == 3:
            Reservation_menu()

        elif choice == 4:
            Admin_menu()
        elif choice == 5:
            break

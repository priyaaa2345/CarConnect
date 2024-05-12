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
    pass


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

    def CalculateTotalCost(self, ReservationID):
        cursor.execute(
            """
                            select totalcost from Reservation
                            where reservationid=?
                    """,
            (ReservationID),
        )
        return cursor.fetchall()


def Reservation_menu():
    pass


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
    pass


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

    def GetVehicleById(self, VehicleID):
        cursor.execute(
            """
                            select * from Vehicle
                            where VehicleID= ?
                       """,
            (VehicleID),
        )

    def GetAvailableVehicles():
        cursor.execute(
            """                      
                        select * from Vehicle
                        where Availability= 1;

                       """,
        )

    def AddVehicle(
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
        cursor.execute(
            """
insert into Vehicle values(?,?,?,?,?,?,?,?)
                       """,
            (
                VehicleID,
                Model,
                Make,
                Year,
                Color,
                RegistrationNumber,
                Availability,
                DailyRate,
            ),
        )

    def UpdateVehicle(self, DailyRate, Availability, VehicleID):
        cursor.execute(
            """
                       update vehicle
                       set DailyRate= ?
                       Availability=?
                       where VehicleID=?
                       """,
            (DailyRate, Availability, VehicleID),
        )

    def RemoveVehicle(self, VehicleID):
        cursor.execute(
            """delete from vehicle 
                       where vehicleID=?
                       """,
            (VehicleID),
        )


class ReservationService:
    def GetReservationById():
        pass

    def GetReservationsByCustomerId():
        pass

    def CreateReservation():
        pass

    def UpdateReservation():
        pass

    def CancelReservation():
        pass


class AdminService:
    def GetAdminById():
        pass

    def GetAdminByUsername():
        pass

    def RegisterAdmin():
        pass

    def UpdateAdmin():
        pass

    def DeleteAdmin():
        pass


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

from util.DBConn import DBConnection
# from tabulate import tabulate
class ReportGenerator(DBConnection):
    def generation_of_report(self,CustomerID):    
        self.cursor.execute("""
                                
select Customer.CustomerID,
        FirstName,
        LastName,
        Email,
        PhoneNumber,
        Address,
        Username,
        Password,
        RegistrationDate,
        Vehicle.VehicleID,
        StartDate,
        EndDate,
        TotalCost,
        Status,
         Model, Make,
         RegistrationNumber from Customer
		 inner join Reservation on 
		 Customer.CustomerID = Reservation. CustomerID
		 inner join Vehicle on 
		 Reservation.VehicleID= Vehicle.VehicleID
                            where Customer.CustomerID=?;""",(CustomerID),
         )
        
        # tried using tables but not working
        
        return self.cursor.fetchall()
        # if data:
        #     headers = [
        #     "Customer ID", "First Name", "Last Name", "Email", "Phone Number",
        #     "Address", "Username", "Password", "Registration Date", "Vehicle ID",
        #     "Start Date", "End Date", "Total Cost", "Status", "Model", "Make",
        #     "Registration Number"
        # ]
        
        # table=tabulate(data, headers=headers, tablefmt="pretty")
        # print(table)
        # return table

            
        
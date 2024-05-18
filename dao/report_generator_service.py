from util.DBConn import DBConnection

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
        
        return self.cursor.fetchall()
            
        
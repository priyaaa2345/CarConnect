from customer import Customer
from vehicle import Vehicle
from reservation import Reservation


class ReportGenerator(Customer,Vehicle,Reservation):
     def __init__(self, CustomerID,
        FirstName,
        LastName,
        Email,
        PhoneNumber,
        Address,
        Username,
        Password,
        RegistrationDate,
        VehicleID,
        StartDate,
        EndDate,
        TotalCost,
        Status,
         Model, Make,
         RegistrationNumber,
         report_end):
        
        # Caling const of base clas

        super().__init__( CustomerID,
        FirstName,
        LastName,
        Email,
        PhoneNumber,
        Address,
        Username,
        Password,
        RegistrationDate,
        VehicleID,
        StartDate,
        EndDate,
        TotalCost,
        Status,
         Model, Make,
         RegistrationNumber,
         report_end
         )

        self.report_end = report_end




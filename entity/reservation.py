
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
        self.__ReservationID = ReservationID
        self.__CustomerID = CustomerID
        self.VehicleID = VehicleID
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.__TotalCost = TotalCost
        self.Status = Status


    def get_reservation_id(self):
        return self.__ReservationID
    
    def set_reservationid(self,ReservationID):
        self.__ReservationID=ReservationID

    def get_customer_id(self):
        return self.__CustomerID
    
    def set_customerid(self,CustomerID):
        self.__CustomerID=CustomerID

    def get_totalcost(self):
        return self.__TotalCost
    
    def set_totalcost(self,TotalCost):
        self.__TotalCost=TotalCost
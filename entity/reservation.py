
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
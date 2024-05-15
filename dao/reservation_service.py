from exception.reservation_exception import ReservationException
from util.DBConn import DBConnection
class ReservationService(DBConnection):
    def CalculateTotalCost(self, ReservationID):
        self.cursor.execute(
            """
                            select totalcost from Reservation
                            where reservationid=?
                    """,
            (ReservationID),
        )
        return self.cursor.fetchall()

    def GetReservationById(self,res_id):
        self.cursor.execute("""
                       select * from Reservation
                       where Reservationid= ?
                       """,(res_id))
        return self.cursor.fetchall()

    def GetReservationsByCustomerId(self,cus_id):
        self.cursor.execute("""
                       select * from Reservation
                       where CustomerID=?
                       
                       """,(cus_id))
        return self.cursor.fetchall()
    def create_reservation(self, re_id, cu_id, ve_id, start_date, end_date, tot_cost, status):
        try:
            self.cursor.execute("""insert into Reservation values(?,?,?,?,?,?,?)""",
                                (re_id, cu_id, ve_id, start_date, end_date, tot_cost, status))
            self.cursor.execute("select ReservationId from Reservation where ReservationID=?", (re_id,))
            result = self.cursor.fetchone()  # Fetch one row from the query result
            if result:  # If result is not None
                raise ReservationException()
        except ReservationException as e:
            print(e)
            # Handle the exception as needed
            return None  # Indicate failure
        else:
            return result  # Indicate success


    # def CreateReservation(self,re_id,cu_id,ve_id,start_date,end_date,tot_cost,status):
    #     try:  #try again
    #         self.cursor.execute("""insert into Reservation values(?,?,?,?,?,?,?)
    #                    """,(re_id,cu_id,ve_id,start_date,end_date,tot_cost,status))
    #         # self.conn.commit()
    #         result = self.cursor.fetchone() #execute("select ReservationId from Reservation where ReservationID=?",(re_id))
    #         if not result:
    #             raise ReservationException()
    #     except ReservationException as e:
    #         print(e)
    #     return result

    def UpdateReservation(self,cust_id,veh_id,stats):
        self.cursor.execute("""
update Reservation
                       set CustomerID=?,
                       VehicleID=?,
                       Status=?
                       where ReservaionID=?
                       """,(cust_id,veh_id,stats))
        self.conn.commit()

    def CancelReservation(self,resv_id):
        self.cursor.execute("""
delete from Reservation
                       where ReservationID=?
                       """,(resv_id))
        
    def CalculateTotalCost(self,resvv_id):
        self.cursor.execute("""
select sum(TotalAmount) from Reservation
                           where ReservationID=?
                           """,(resvv_id))
        return self.cursor.fetchall()


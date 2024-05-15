from exception.vehicle_not_exception import VehicleNotFoundException
from util.DBConn import DBConnection

class VehicleService(DBConnection):

    def GetVehicleById(self, vehi_id):
        try:
            self.cursor.execute(
            """
                            select * from Vehicle
                            where VehicleID= ?
                       """,
            (vehi_id),
            )
            details=self.cursor.fetchall()
            if len(details)==0:
                raise VehicleNotFoundException()        # whenever we raise error it goes to except blk     
            else:          
                print(details)
        except Exception as e:
            print("oops an error..",e)
    
    def GetAvailableVehicles(self):
        self.cursor.execute(
            """                      
                        select * from Vehicle
                        where Availability= 1;

                       """,
        )
        return self.cursor.fetchall()

    def AddVehicle(
        self,
        ve_id,modl,make,year,color,Register_num,Availabi,Daily_rate
    ):
        self.cursor.execute(
            """
insert into Vehicle values(?,?,?,?,?,?,?,?)
                       """,
            (
                ve_id,modl,make,year,color,Register_num,Availabi,Daily_rate
            ),
        )
        self.conn.commit()

    def UpdateVehicle(self,dail_rate,availab,veh_id):
        self.cursor.execute(
            """
                       update Vehicle
                       set DailyRate= ?,
                       Availability=?,
                       where VehicleID=?
                       """,
            (dail_rate,availab,veh_id),
        )
        self.conn.commit()

    def RemoveVehicle(self, v_id):
        self.cursor.execute(
            """delete from Vehicle 
                       where vehicleID=?
                       """,
            (v_id),
        )
        self.conn.commit()

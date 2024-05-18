from exception.vehicle_not_exception import VehicleNotFoundException
from util.DBConn import DBConnection

class VehicleService(DBConnection):

    def GetVehicleById(self, vehi_id):
        try:
            self.cursor.execute(
                """
                SELECT * FROM Vehicle WHERE VehicleID= ?
                """,
                (vehi_id,)
            )
            details = self.cursor.fetchall()
            if len(details) == 0:
                raise VehicleNotFoundException()
            else:
                print(details)
        except Exception as e:
            print("Oops, an error occurred:", e)

    def GetAvailableVehicles(self):
        self.cursor.execute(
            """                      
                        SELECT * FROM Vehicle
                        WHERE Availability= 1;
                       """
        )
        return self.cursor.fetchall()

    def AddVehicle(self, ve_id, modl, make, year, color, Register_num, Availabi, Daily_rate):
        try:
            self.cursor.execute(
                """
                INSERT INTO Vehicle VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (ve_id, modl, make, year, color, Register_num, Availabi, Daily_rate)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print("Error adding vehicle:", e)
            return False

    def UpdateVehicle(self, dail_rate, availab, veh_id):
        self.cursor.execute(
            """
            UPDATE Vehicle SET DailyRate = ?, Availability = ? WHERE VehicleID = ?
            """,
            (dail_rate, availab, veh_id)
        )
        self.conn.commit()

    def RemoveVehicle(self, v_id):
        try:
            self.cursor.execute(
                """
                DELETE FROM Reservation WHERE VehicleID=?
                """,
                (v_id,)
            )
            self.cursor.execute(
                """
                DELETE FROM Vehicle WHERE VehicleID=?
                """,
                (v_id,)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print("Error removing vehicle:", e)
            return False

    def GetAllVehicles(self):
        self.cursor.execute("SELECT * FROM Vehicle")
        return self.cursor.fetchall()

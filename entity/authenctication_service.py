
from util.DBConn import DBConnection
from exception.authentication_exception import AuthenticationException


class AuthenticationService(DBConnection):

    def check_customer(self,username,password):
        try:
            self.cursor.execute(
            """
                        select Username,Password from customer
                        where Username=? and password=?
                       """,
            (username, password),
        )
            result = self.cursor.fetchone()
            if not result:
                raise AuthenticationException()
            print("Authentication successful!!")

        except AuthenticationException as e:
            print(e)
        return result
    
    def check_admin(self,username,password):
        try:
            self.cursor.execute(
            """
                        select Username,Password from Admin
                        where Username=? and Password=?
                       """,
            (username, password),
        )
            result = self.cursor.fetchone()
            if not result:
                raise AuthenticationException()
            print("Authentication successful!!")

        except AuthenticationException as e:
            print(e)
        return result



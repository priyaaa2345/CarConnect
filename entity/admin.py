
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
        self.__AdminID = AdminID
        self.FirstName = FirstName
        self.LastName = LastName
        self.__Email = Email
        self.PhoneNumber = PhoneNumber
        self.__Username = Username
        self.__Password = Password
        self.__Role = Role
        self.JoinDate = JoinDate

    
    def get_adminid(self):
        return self.__AdminID
    def set_adminid(self,AdminID):
         self.__AdminID=AdminID

    
    def get_email(self):
        return self.__Email
    
    def set_firstname(self,Email):
         self.__Email=Email

    
    def get_username(self):
        return self.__Username
    
    def set_fusername(self,Username):
         self.__Username=Username

    
    def get_password(self):
        return self.__Password
    
    def set_password(self,Password):
         self.__Password=Password

    def get_role(self):
        return self.__Role
    
    def set_role(self,Role):
        self.__Role=Role



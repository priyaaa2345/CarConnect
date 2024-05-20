class Customer:
    def __init__(
        self,
        CustomerID,
        FirstName,
        LastName,
        Email,
        PhoneNumber,
        Address,
        Username,
        Password,
        RegistrationDate,
    ):
        self.__CustomerID = CustomerID 
        self.FirstName = FirstName
        self.LastName = LastName
        self.__Email = Email
        self.PhoneNumber = PhoneNumber
        self.Address = Address
        self.__Username = Username
        self.__Password = Password
        self.RegistrationDate = RegistrationDate

    def get_customer_id(self):
        return self.__CustomerID

    def set_customer_id(self, CustomerID):
        self.__CustomerID = CustomerID

    def get_email(self):
        return self.__Email

    def set_email(self, Email):
        self.__Email = Email

    def get_username(self):
        return self.__Username

    def set_username(self, Username):
        self.__Username = Username

    def get_password(self):
        return self.__Password

    def set_password(self, Password):
        self.__Password = Password

    

class mpesaUser:
    __companyName = "Apple"
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def getName(self):
        return self.name

    def getphoneNumber(self):
        return self.phoneNumber

    def setName(self, name):
        self.name = name

    def setphoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def getcompanyName(self):
        return self.__companyName

newaMpesaUser = mpesaUser("Filemon", "0712345690")
print(newaMpesaUser.getName())

newaMpesaUser.setName("Philemon")
print(newaMpesaUser.getName())


"""
-in line 1 i am defining the class mpesaUser:
-all functions in the class have the first parameter as self to show that this specific class is being refered to.

-in line 2 i declared the variable companyName 

-in line 3 i am creating a contructor function and defining it using __init__(self, name, phoneNumber):
-in line 5 and 5 i am defining the properties in the constructor.

-in line 7 and 10, i am defining functions (getters) to get the name and phone numbers of the Users.
-in line 8 and 11, i am returning the values of the name and phone numbers of the Users.

-in line 13 and 15 i am defining functions (setters) to set the name and phone numbers of the Users.
-in line 14 and 17, i am defining the properties, name and phoneNumber.

-in line 19 i am defining a function (getter) to get the companyName of the Users.
-in line 20 i am returning the value of the companyName of the Users. i am using the access modifier of two underscores to make this property private so it can't be changed so only Apply staff will use it. 

-in line 22 i am creating an instance.
-in line 23 i am printing the name of that instance.
-in line 25 i am setting (changing) the name of that instance.
-in line 26 i am printing the revised name.
"""

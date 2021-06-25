from mpesaUser import mpesaUser
class employee(mpesaUser):
    def recieveMoney():
        pass

    employees = [
        {
            "name" : "Sam Tomashi",
            "phoneNumber" : "0713457653"
        },
        {
            "name" : "Back Obama",
            "phoneNumber" : "0726538716"
        },
        {
            "name" : "Nelson Mandela",
            "phoneNumber" : "0795646358"
        }
    ]

newEmployee = employee("Sam Tomashi", "0713457653")
print(newEmployee.getName())
print(newEmployee.phoneNumber)

newEmployee = employee("Back Obama", "0726538716")
print(newEmployee.getName())
print(newEmployee.phoneNumber)

'''
-in line 1 i am importing the parent class, mpesaUser, into this child class, employee.
-in line 2 i am defining the class employee and inheriting the properties from the parent class into this child class.

-in line 3 i am defining a function that allows employees to recieve money.

-in line 6 to 19 i am defining the variable called employees. it is a list of dictionaries of three employees. with the keys, name and phoneNumber.
-in line 21 and 25 i am creating instances based on two of the dictionaries.
-in line 22, 23, 26, and 27 i am printing the name and the phoneNumber of the instances.
'''
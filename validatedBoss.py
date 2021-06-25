from mpesaUser import mpesaUser
class validatedBoss(mpesaUser):
    def inputAmountToPayEmployees():
        amount = int(input("Enter amount here"))
        if amount > 1000:
            x = amount * 0.02
            print(x + amount)

        else:
            print(amount)

    inputAmountToPayEmployees()

newvalidatedBoss = validatedBoss("Nelson Mandela", "0795646358")
print(newvalidatedBoss.getName())
print(newvalidatedBoss.phoneNumber)

'''
-in line 1 i am importing the parent class, mpesaUser, into this child class, validatedBoss.
-in line 2 i am defining the class validatedBoss and inheriting the properties from the parent class into this child class.

-in line 3 i am defining a function which prompts the Boss to enter the amount they wish to pay the employees.
-in line 4 i am declaring the variable called amount to be what the boss enters and for that value to be converted into the integer data type using casting.
-in line 5 i am giving a conditional statement saying if the amount is more that 1000,
 (in line 6) then multiply that amount and
 (in line 7) print the new value added to the amount to show the boss how much will be deducted from their mpesa account.
-in line 9 and 10 i am giving the else statement telling the computer to print the original amount if it is not more than 1000.
-in line 12 i am calling the function inputAmount().

-in line 14 i am creating an instance based on one of the dictionaries.
-in line 15 and 16 i am printing the name and phoneNumber of the instance i created.
'''

from mpesaUser import mpesaUser
class boss(mpesaUser):

    def inputPin():
        pin = int(input("Enter 4 digit pin here: "))
        print(pin)

    inputPin()

    def validateBossPin(self):
        # logic for validating the Boss's pin by crosschecking mpesa's records with what the Boss entered.
        # logic giving a conditional statement saying that if the pin is correct, proceed to ask for amount, else, ask again for the pin.
        pass

newBoss = boss("Harry", "0712312312")
print(newBoss.getName())
print(newBoss.phoneNumber)

'''
-in line 1 i am importing the parent class, mpesaUser, into this child class, bosses.
-in line 2 i am defining the class bosses and inheriting the properties from the parent class into this child class.

-in line 4 i am defining a function which prompts the boss to enter their four digit pin.
-in line 5 i am declaring the variable called pin to be what the boss enters and for that value to be converted into the integer data type using casting.
-in line 6 i am printing the pin entered by the boss.
-in line 8 i am calling the function inputPin().

-in line 10 i am defining a function to validate the boss's pin.
-in line 11 and 12 i have commented that there is to be logic validating the mpesa pin and an if statement allowing the boss to proceed if the pin is correct or to be prompted for the pin again if it is not correct.
-in line 13 i am using the pass statememnt to tell the computer not to run the function because i do not have the actual logic.

-in line 15 i am creating an instance.
-in line 16 i am printing the name of that instance.
-in line 17 i am printing the phoneNumber of that instance.

'''
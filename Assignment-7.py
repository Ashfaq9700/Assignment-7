# 1. Write a python script to display the number of days in a given month number.
"""Solution
user_Input_Month = int(input("Enter Month :"))

match user_Input_Month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 Days")
    case 4 | 6 | 9 | 11:
        print("30 Days")
    case 2:
        print("28 Days")
    case _:
        print("Please Enter Valid Month")        
"""

"""
# 2. Write a menu driven program to perform following operations - Addition, Subtraction,
# Multiplication, Division

print("This is the Calculation Program")
print("-------------------------------")

num_1 = int(input("Enter First Value  : "))
num_2 = int(input("Enter Second Value :"))

menu = int(input("Press 1 for Addition\nPress 2 for Subtraction\nPress 3 for Multiplication\nPress 4 for Division\nEnter Here :"))
print(menu)

match menu:
    case 1:
        print("The Sum of Two Numbers is :",num_1+num_2)
    case 2:
        print("The Subtraction of Two Numbers is :",num_1-num_2)
    case 3:
        print("The Multiplication of Two Numbers is :",num_1*num_2)
    case 4:
        print("The Division of Two Numbers is :",num_1/num_2)
    case _:
        print("Invalid Input")
"""

"""
# 4. Write a program which takes user's age and display the category of person. Age
# below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
# Experienced, Age above or equal 60 - Senior Citizen.

age =  int(input("Enter Your Age : "))

match age:
    case age if((age>0) and (age <10)):
        print("Kid")
    case age if((age>=10) and (age <20)):
        print("Teen")
    case age if((age>=20) and (age <40)):
        print("Young")
    case age if((age>=40) and (age <60)):
        print("Experienced")
    case age if((age >=60) and (age <=100)):
        print("Senior Citizen")
    case _:
        print("Enter Valid Age")
"""

"""
# 5. Write a program which takes a number from user. Print Saurabh Shukla if the number
# is even, print Prateek Jain if the number is negative odd number and print Aditya
# Choudhary if number is positive odd number.

userInput = int(input("Enter Number :"))

match userInput:
    case userInput if((userInput%2==0)):
        print("Saurabh Shukla")
    case userInput if((userInput%2!=0)and (userInput<0)):
        print("Prateek Jain")
    case userInput if((userInput%2!=0)and (userInput>0)):
        print("Aditya Choudhary")
    case _:
        print("Enter Valid Number")
"""

"""
# 6. Write a python program to check whether a given string is a multiword string or single
# word string using match case statement

userString = input("Enter String :")

match userString:
    case userString if((len(userString)> 1)):
        print("Multi String")
    case userString if((len(userString)== 1)):
        print("Single String")
    case _:
        print("Enter Valid String")
print(type(userString))
"""

"""
# 7. Write a python program to check whether a given number is positive, negative or
# zero using match case statement

userInput = int(input("Enter Number : "))

match userInput:
    case userInput if(userInput>0):
        print("Positive")
    case userInput if(userInput==0):
        print("Zero")
    case userInput if(userInput<0):
        print("Negative")
"""

"""
# 8. Write a python script to check whether two given strings are identical, first string
# comes before the second in dictionary order or first string comes after the second
# string in dictionary order using match case statement

msg = "Hi"
msg_2 = "i"
result = False

match result:
    case result if(msg == msg_2):
        result = True
        print("identical")
       
    case result if(msg_2 == msg):
        result = True
        print("identical")
      
    case _:
        print("Not Identical")
"""

"""
10. Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday
------------------------------------------------------------------------------
Solution
fcolor = input("Which Color You Like : ")
fcolor = fcolor.lower()
result = fcolor.split()
fresult = result[2]


match fresult:
    case fresult if(fresult ==  "yellow"):
        print("Monday")
    case fresult if(fresult ==  "blue"):
        print("Tuesday")
    case fresult if(fresult ==  "orange"):
        print("Wednesday")
    case fresult if(fresult ==  "white"):
        print("Thursday")
    case fresult if(fresult ==  "black"):
        print("Friday")
    case fresult if(fresult ==  "red"):
        print("Saturday")
    case _:
        print("Sunday")
"""
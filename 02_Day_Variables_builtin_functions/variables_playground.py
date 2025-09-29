"""print(len('gnaknga , gaslejg l.ge mml'))
try:
    full_name = str(input('Please Enter Your Full Name: '))
    age = int(input('Please Enter Your Age: '))

    print(f'Your Full Name is: {full_name}')
    print(f'You Are {age} Years Old')

except ValueError:
    print("Invalid Input") """

"""num_int = 10
print("num_int:", num_int)
num_float = float(num_int)
print("num_float:", f'{num_float : .2f}')
num_string = num_float
print("num_string:", f'{num_float}000000')

#float to int
x = 13.54
print(int(x))

#int to str
x = 30
print(x)
x_string = str(x)
print(x_string)

#str to list
name = 'wardell stephlin'
print (name)
name_to_list = list(name)
print (name_to_list)
"""

#EXERCISES

#Write a python comment saying 'Day 2: 30 Days of python programming'
#Day 2: 30 Days of python programming

#Declare a first name variable and assign a value to it
first_name = "Lin"
#Declare a last name variable and assign a value to it
last_name = "San Gabriel"
#Declare a full name variable and assign a value to it
full_name = first_name + " " + last_name
#Declare a country variable and assign a value to it
country = "Philipines"
#Declare a city variable and assign a value to it
city = "Olongapo"
#Declare an age variable and assign a value to it
age = 22
#Declare a year variable and assign a value to it
year = 2025
#Declare a variable is_married and assign a value to it
is_married = True
#Declare a variable is_true and assign a value to it
is_true = True
#Declare a variable is_light_on and assign a value to it
is_light_on = False
#Declare multiple variable on one line
first_name,last_name,country,city = "Lin", "San Gabriel", "Philipines", "Olongapo"

#Check the data type of all your variables using type() built-in function
print ('first_name:',type(first_name))
print ('last_name:',type(last_name))
print ('country:',type(country))
print ('city:',type(city))
print ('age:',type(age))
print ('year:',type(year))
print ('is_married:',type(is_married))
print ('is_true:',type(is_true))
print ('is_light_on:',type(is_light_on))
print(first_name,last_name,country,city)

#Using the _len()_ built-in function, find the length of your first name
print(len(first_name))
#Compare the length of your first name and your last name
print(f"The length of my first name is {len(first_name)} characters long, while the length of my last name is {len(last_name)} characters long")
#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
#Add num_one and num_two and assign the value to a variable total
sum = num_one + num_two
#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
#Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two 
#Divide num_one by num_two and assign the value to a variable division
quotient = num_one / num_two
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two
#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

#The radius of a circle is 30 meters.
    #Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
    #Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
    #Take radius as user input and calculate the area.
import math
r = int(input("Enter a valid integer for radius: "))
area_of_circle = math.pi * r ** 2
circum_of_circle = 2 * math.pi * r

print(f"The area of the circle is {area_of_circle: .2f}m²") 
print(f"The circumference of the circle is {circum_of_circle: .2f}m")


#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = str(input("First Name:"))
last_name = str(input ("Last Name:"))
country = str(input("Country:"))
age = int(input("Age:"))

print (f"Your name is {first_name} {last_name}. At the age of {age}, you're residing in the {country}.")
#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
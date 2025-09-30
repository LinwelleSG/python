"""x = int(input("Enter an integer to be cubed: "))
result = x ** 3
print(result)

print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

import math
radius = int (input("Enter the radius:"))                           
area_of_circle = math.pi * radius ** 2        
print(f'Area of a circle: {area_of_circle : .2f}')"

print('1 is 1', 1 is 1)                   # True - because the data values are the same

#EXERCISES
#Day 3: 30 Days of python programming

#💻 Exercises - Day 3

#1. Declare your age as integer variable
age = (int(22))
#2. Declare your height as a float variable
height = (float(175))
#3. Declare a variable that store a complex number
var = (complex(2j))
#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b = float(input("Enter the base of the triangle:"))
h = float(input("Enter the base of the triangle:"))

area = 0.5 * b * h

print(f"The are of the triangle is {area}")


#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
abc = input("Enter the sides a, b, and c (separate with a comma):")
a , b , c = map(int, abc.split(","))
parameter = a + b + c
print(f"The Parameter of the triangle is {parameter}") 


#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length_width = input("Enter a length and a width of a rectangle to get the area and perimeter (separate with a comma e.g. length,width):")
length , width = map(float, length_width.split(","))
area = length * width
perimeter = 2 * (length + width)

print(f"The area of the rectangle is {area}, and the perimeter is {perimeter}.")

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14
import math
radius = int(input("Enter a radius of a circle to calculate the area: "))
area = math.pi * radius * radius
circumference = 2 * math.pi * radius
print(f"A circle with a radius of {radius} has an area of {area: .2f} and a circumference of {circumference: .2f}.")

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
x1,y1 = 2,2
x2,y2 = 6,10
slope = (y2 - y1) / (x2 - x1)
ed = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
slope = round(slope, 2)
ed = round(ed, 2)
print(slope)
print(ed)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
import math

# coefficients
a = 1
b = 6
c = 9

# discriminant
D = b**2 - 4*a*c

if D < 0:
    print("No real roots")
elif D == 0:
    x = -b / (2*a)
    print(f"The value of x where y=0 is: {x}")
else:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"The values of x where y=0 are: {x1}, {x2}") 
    
#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
x = "python"
y = "dragon"
statement = x == y
print(statement) 

#Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
x,y= "python" , "dragon"
check = ("on" in x) and ("on" in y)
print (check) 

#_I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.
sentence = "_I hope this course is not full of jargon_"
print("_jargon_" in sentence)

#There is no 'on' in both dragon and python
x = "python"
y = "dragon"
print (not("on" in x) or not("on" in y))

#Find the length of the text _python_ and convert the value to float and convert it to string
x = "python"
length = len(x)
print(float(length))
print(str(length)) 

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
try:
    x = float(input("Enter a number to check if it is even or odd: "))
    if x % 2 == 0:
            print(f"{x} is an even number")
    else:
            print(f"{x} is an odd number")
        
except ValueError:
    print("Invalid input")
    
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
fd = 7 // 3
value = int(2.7)
print (fd == value)

#Check if type of '10' is equal to type of 10
print( type('10') == type(10))

#Check if int('9.8') is equal to 10
print(int(9.8) == 10)

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter the number of hours you work:"))
rate = float(input("Enter your rate per hour:"))
print (f"you can earn {hours * rate : .2f}PHP in {int(hours)} hours of work.") 
"""
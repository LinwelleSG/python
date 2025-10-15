"""def generate_full_name():
    first_name = "Linwelle "
    last_name = "San Gabriel"
    full_name = first_name + last_name
    return full_name
print(generate_full_name()) 

def greetings(name):
    greeting = name + ", Welcome to Mobile Legends"
    return greeting
print(greetings("Doc Jay"))

def  add_hundred(num):
    return num + 100
num = int(input("Enter a number to add to a hundred: "))
print(add_hundred(num))

def sum_of_nums(n):
    total = 0
    for i in range(n+1):
        total += i
    return total
print(sum_of_nums(10))
print(sum_of_nums(100))

#mass time gravity
def weight(mass,gravity):
    total_weight = f"{mass*gravity:.2f}N"
    return total_weight
print(weight(45,9.81))

def mass(weight,gravity):
    total_mass = weight / gravity
    return total_mass
print(f"{mass(441.45,9.81):.2f}")

def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print(print_fullname(lastname = 'Asabeneh',firstname = 'Yetayeh'))

def is_even(n):
    if n % 2 == 0:
        return f"{n} is an even number"
    return f"{n} is an odd number"
print(is_even(5))

def all_even_numbers(n):
    evens = []
    for i in range(n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(all_even_numbers(25))

def full_name(fstnm ,lstnm = "SG"):
    fn = fstnm + " " + lstnm
    return fn
print(full_name("Yel"))

def sum_of_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total 
print(sum_of_nums(2,5,72,3)) 

#💻 Exercises: Day 11
#Exercises: Level 1
#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def sum_of_nums(x,y):
    sum = x + y
    return sum
print(sum_of_nums(44,25))
#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
import math
def area_of_circle(pi,radius):
    area = math.pi * radius ** 2
    return area
print(f"{area_of_circle(math.pi,25):.2f}")
#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if not isinstance(num, (int,float)):
            return "All numbers must be integers or float"
        total += num
    return total
nums_input = input("Enter numbers separated by comma: ")
nums = [float(n) for n in nums_input.split(",")]

print(add_all_nums(*nums)) 

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def c_to_f(c):
    f = c * (9/5) + 32
    return f
print(c_to_f(25))
#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ["December", "January", "February"]:
        return f"{month} is Winter season."
    elif month in ["March", "April","May"]:
        return f"{month} is Spring season."
    elif month in ["June","July","August"]:
        return f"{month} is Summer season."
    elif month in ["September","October","November"]:
        return f"{month} is Autumn season."
    else:
        return "Please enter a valid month"
print(check_season(input("Enter a month to determine which season it is: "))) """

#Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1,y1,x2,y2):
    slope =  (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(3,5,7,9))
#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(x,a,b,c):
    quadratic = ((a * x) ** 2) + ((b * x) ** 2) + c
    return quadratic
print(solve_quadratic_eqn(3,5,2,4))
#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for item in lst:
        print(item)
names = ["Lin","Du","JM"]
print_list(names)
#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(items):
    reversed_items = []
    for i in range(len(items) -1, -1, -1):
        reversed_items.append(items[i])
    return reversed_items
numbers = [5,10,15,20,25]
print(reverse_list(numbers))
#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalized_list_items(listahan):
    for item in listahan:
        print(item.upper())
titles = ["shawshank", "friends", "mobile legends"]
capitalized_list_items(titles)
#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(                                                        ):




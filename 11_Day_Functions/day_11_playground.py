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
print(check_season(input("Enter a month to determine which season it is: "))) 

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
def add_item(lest,aytem):
         lest.append(aytem)
         return lest
lestahan = ["Yel", "Dan", "Lin"]
print(add_item(lestahan,"Goy")) """
#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst,item):
    if item in lst:
        lst.remove(item)
    return lst
items = ["Hikaru", "Magnus", "Fabiano","Gukesh"]
print(remove_item(items, "Magnus"))
#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    total = 0
    for i in range(num + 1):
        total += i
    return total
print(sum_of_numbers(10))
#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    odds = 0
    for i in range(n + 1):
        if i % 2 == 1:
            odds += i
    return odds
print(sum_of_odds(10))
#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(n):
    even = 0
    for i in range(n + 1):
        if i % 2 == 0:
            even += i
    return even
print(sum_of_even(10))
#Exercises: Level 2
#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    odds = []
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
            
    print(f"The number of odd numbers in {n} is {len(odds)}")
    print(f"The number of even numbers in {n} is {len(evens)}")
    
    return {"odds" : odds, "evens" : evens}

print(evens_and_odds(20))

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    total = 1
    for i in range(1,n + 1):
        total *= i
    return total
print(factorial(3))
#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(item):
    if not item:
        return True
    else:
        return False
print(is_empty([]))


#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    lst_sorted = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst_sorted[mid - 1] + lst_sorted[mid]) / 2
    else:
        return lst_sorted[mid]

def calculate_mode(lst):
    frequency = {}
    for num in lst:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    if len(modes) == len(lst):
        return None  
    return modes

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    squared_diffs = [(x - mean) ** 2 for x in lst]
    return sum(squared_diffs) / len(lst)

def calculate_std(lst):
    variance = calculate_variance(lst)
    return variance ** 0.5

nums = [5,2,23,3,6,9]
print(calculate_mean(nums))
print(calculate_median(nums))
print(calculate_mode(nums))
print(calculate_range(nums))
print(calculate_variance(nums))
print(f"{calculate_std(nums):.2f}")

#Write a functions which checks if all items are unique in the list.
def is_unique(lst):
    return len(lst) == len(set(lst))
items = ["Wesley", "SJC", "Columban", "SJC"]
print(is_unique(items))

#Write a function which checks if all the items of the list are of the same data type.
def is_same(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    
    for item in lst:
        if type(item) != first_type:
            return False
    return True
print(is_same([2, "Carlsen", {"gg": "ez"}]))

#Write a function which check if provided variable is a valid python variable
def is_valid(var):
    return var.isidentifier()
print(is_valid("8python"))
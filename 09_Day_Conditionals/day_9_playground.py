"""n = 0

if n > 0:
    if n % 2 == 0:
        print(f"{n} is an even positive number")
    else:
        print(f"{n} is a positive odd number")
elif n < 0:
    print(f"{n} is a negative number")
else:
    print(f"{n}")
    
profession = input("Enter your profession: ")
salary = int(input("Enter your current salary: "))
if profession in ["IT", "Technology", "Student"] and salary >= 5000:
    print("You are a great technologist and earning well.")
elif profession in ["IT", "Technology", "Student"] and salary < 5000:
    print("Keep striving, fellow technologist. you will earn well soon.")
else:
    print("You are not a technologist")
    
#💻 Exercises: Day 9
#Exercises: Level 1
#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to drive")
elif 18 - age == 1:
    print(f"You need 1 more year to drive")
else:
    print(f"You need {18 - age} more years to drive")

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"The first number ({a}) is greater that the second number ({b}).")
elif a < b:
    print(f"The second number ({b}) is greater that the first number ({a}).")
else:
    print(f"Both numbers ({a} and {b}) are equal")

computer_age = 45
age = int(input("Enter your age: "))

if age > computer_age:
    if age - computer_age == 1:
        print("You are a year older than me")
    else:
        print(f"You are {age - computer_age} years older than me.")
elif age < computer_age:
    if computer_age - age == 1:
        print(f"I am a year older than you.")
    else:
        print(f"I am {computer_age - age} years older than you.")
else:
    print("We're the same age")
    
#Write a code which gives grade to students according to theirs scores:

#80-100, A
#70-89, B
#60-69, C
#50-59, D
#0-49, F
grade = float(input("Enter your grade: "))
if grade >= 80 and grade <= 100:
    print("Congratulations! You get an A")
elif grade >= 70 and grade < 80:
    print("Good job! You get a B")
elif grade >= 60 and grade < 70:
    print("Nice try! You get a C")
elif grade >= 50 and grade < 60:
    print("Nice try! You get a D")
elif grade <= 49 and grade >= 0:
    print("Nice try! You get an F")
else:
    print("Invalid grade")
    
#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
autumn = ["September","October","November"]
winter =["December","January","February"]
spring =["March","April","May"]
summer =["June","July","August"]
month = input("Enter a month to determine the season: ")
if month in autumn:
    print(f"{month}'s season is autumn")
elif month in winter:
    print(f"{month}'s season is winter")
elif month in spring:
    print(f"{month}'s season is spring")
else:
    print(f"{month}'s season is summer")



#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Please enter a fruit to add: ")
if new_fruit in fruits:
    print(f"{new_fruit} is already in the fruits list")
else:
    fruits.append(new_fruit)
    print(fruits) """


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

 # Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
"""if "skills" in person:
    skills = person["skills"]
    index = len(skills) // 2
    mid_skill = skills[index]
    print(mid_skill)
else:
    print("No skill key found")"""
 # Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person:
    if "Python" in person["skills"]:
         print("Python")
    else:
        print("There is a skill key but no Python value")
else:
    print("There is no \"skills\" key")
     
 # If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if person["skills"] == ["JavaScript" , "React"]:
     print("He is a front end developer")
elif ["Node", "Python" , "MongoDB"] in person["skills"]:
    print("He is a backend developer")
elif ["React" , "Node" , "MongoDB"] in person["skills"]:
    print("He is a fullstack developer")
else:
    print("Unknown Title")
    
 # If the person is married and if he lives in Finland, print the information in the following format:
  #  Asabeneh Yetayeh lives in Finland. He is married.
if person["is_married"] is True and person["country"] == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
else:
    print(f"{person['first_name']} {person['last_name']} does not live in {person['country']} or He is not married.")







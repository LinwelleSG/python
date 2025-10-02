"""multiline_string = ''I am a teacher and enjoy teaching.

I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.''
print(multiline_string)

first_name = (input('Enter your first name: ')) 
last_name = (input('Enter your last name: ')) 
space = ' '

print(f'your full name is {first_name + space + last_name}')
print(f'your first name has {len(first_name)} characters')
print(f'your last name has {len(last_name)} characters')
print(len(first_name) > len(last_name))

print('In every programming language it starts with "Hello, World!"')

print("In Game Name:\t\tKills\tDeaths\tAssists")
print("Stephlin Curry\t\t5\t6\t19")
print("\\\\")

first_name = "Wardell"
last_name = "Stephen"
sport = "basketball"
percentage = float(99.56)
formatted_string = "My name is %s %s. I play %s for a living. My shooting %% is %.2f%%" %(first_name,last_name,sport,percentage)
print(formatted_string)

import math
radius = 10
area = math.pi * radius ** 2
print("The area of a cricle with a radius of %d is %.2f" %(radius,area)) 


enter_artists = input("Enter your top celebrity crushes (separate with a comma): ")
artists = [i.strip() for i in enter_artists.split(",")]

if len(artists) > 1:
    print("Your top celebrity crushes are: " + ",".join(artists[:-2]) + " and " + (artists[-1]))
else:
    print(f"Your top celebrity is " + artists[0])
while True:   
    user_rolex = input("Enter your top rolex models (separate with comma):")
    rolex = [r.strip() for r in user_rolex.split(",")if r.strip()]

    if len(rolex) > 1:
        print("Your top rolexes are %s" % ", " .join(rolex[:-1]) + " and " + (rolex[-1]))
    elif len(rolex) == 1:
        print("Your top rolex is %s" %(rolex))
        break
    else:
        print("Please Enter a Rolex Model") 
        
while True:
    input_clothing = input("Enter your favorite clothing brands: ")
    clothing_brands = [c.strip() for c in input_clothing.split(",") if c.strip()]

    if len(clothing_brands) > 1:
        print(f"Your favorite clothing brands are {', ' .join(clothing_brands[:-1])} and {clothing_brands[-1]}")
    elif len(clothing_brands) == 1:
        print(f"Your favorite clothing brand is {clothing_brands[0]}")
        break
    else:
        print("Please enter at least 1 clothing brand") 
        
def count_sheeps(sheep):
    return sum(1 for s in sheep if s is True)
sheep = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True] 
  
fruits = "Apple"
first_name = "Lin"
last_name = "Curry"

print("{} {} likes {}".format(first_name,last_name,fruits)) 

x = 54
y = 33
print(f"{x} + {y}= {x+y}")
print(f"{x} - {y}= {x-y}")
print(f"{x} * {y}= {x*y}")
print(f"{x} / {y}= {x/y :.2f}") 

name = "Linwelle"
a,b,c,d,e,f,g,h = name
print(a,b,c,d) 

groom_first_name = input("Enter the first name of the groom: ")
groom_last_name = input("Enter the last name of the groom: ")
bride_first_name = input("Enter the first name of the bride: ")
bride_last_name = input("Enter the last name of the bride: ")

print(f"Stay in love, {bride_first_name} {groom_last_name}. <3")
random_word = input("Enter a random word: ")
first_three = random_word[0:3]
last_three = random_word[-3:]
print(f"The first three letters of the word {random_word} is: {first_three}")
print(f"The last three letters of the word {random_word} is: {last_three}")

language = 'Python'
pto = language[0:6:2] #
print(pto) 


print("Wardell Stepen"[::-1]) 

name = "Wardell Stephlin Curry"
print(name.count("l"))
print(name.count('l',6,-1))
print(name.count('ll S')) 

name = "Linwelle San Gabriel"
substring = "lle"
print(f"{name.index(substring)}th")
challenge = '4\u00B2'
print(challenge.isdigit())

while True:
    identifier = input("Please enter an indentifier to determine wether valid or not: ")
    if identifier.isidentifier():
            print("Valid")
            break
    else:
            print("Invalid")

first_name = input("Enter your first name: ")
print(first_name.isupper()) 

items = (input("Enter names separated by spaces: "))
items_collection = items.split()
print(", ".join(items_collection)) 

challenge = 'thirty days of python'
print(challenge.title())
print(challenge.swapcase())
print(challenge.startswith("th"))"""

#EXERCISES
#Day 4: 30 Days of python programming
#💻 Exercises - Day 4

#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a,b,c,d = "Thirty", "Days", "Of", "Python"
print(a,b,c,d)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
strings = ["coding", "for", "all"]
stripped_strings = ' '.join(strings)
print(stripped_strings.title())

#Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
#Print the variable company using print().
print(company)
#Print the length of the company string using len() method and print().
print(len(company))
#Change all the characters to uppercase letters using upper() method.
print(company.upper())
#Change all the characters to lowercase letters using lower() method.
print(company.lower())
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.swapcase())
#Cut(slice) out the first word of Coding For All string.
last_two = company[7:]
print(last_two)
#Check if Coding For All string contains a word Coding using the method index, find or other methods.
is_coding = "Coding" in company
print(is_coding)
#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))
groom_last = "San Gabriel"
bride_name = "Erielle"
bride_last = "Ticar"
bride = bride_name + ' ' + bride_last
print(bride.replace(bride_last,groom_last))
#Change Python for Everyone to Python for All using the replace method or other methods.
print(company.replace("Coding For All","Python For Everyone"))
#Split the string 'Coding For All' using space as the separator (split()) 
print(company.split())
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
apps = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(apps.split(','))
#What is the character at index 0 in the string Coding For All.
print(company[0])
#What is the last index of the string Coding For All.
print(company[-1])
#What character is at index 10 in "Coding For All" string.
print(company[10])
#Create an acronym or an abbreviation for the name 'Python For Everyone'.
python_for_everyone = company.replace("Coding For All", "Python For Everyone")
acronym = ''.join(word[0] for word in python_for_everyone.split())
print(acronym)
#Create an acronym or an abbreviation for the name 'Coding For All'.
print(''.join(word[0] for word in company.split()))
#Use index to determine the position of the first occurrence of C in Coding For All.
print(company.find('C'))
#Use index to determine the position of the first occurrence of F in Coding For All.
print(company.find('F'))
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))
#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
conjunction = "You cannot end a sentence with because because because is a conjunction"
print(conjunction.index('because'))
#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(conjunction.rindex('because'))
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
remove = "because because because"
start = conjunction.index(remove)
end = start + len(remove)
result = conjunction[:start] + conjunction[end+1:]
print(result)
#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(conjunction.find('because'))
#Does ''Coding For All' start with a substring Coding?
print(company.startswith("Coding"))
#Does 'Coding For All' end with a substring coding?
print(company.endswith("coding"))
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
cfa_spaces = '   Coding For All      '
print(cfa_spaces.strip(' '))

#Which one of the following variables return True when we use the method isidentifier():
# - 30DaysOfPython
# - thirty_days_of_python
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())
#Answer : thirty_days_of_python

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join('#' + lib for lib in libraries))

#Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

#Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
print("{:<10}{:<8}{:<10}{:<10}".format("Name", "Age", "Country", "City"))
print("{:<10}{:<8}{:<10}{:<10}".format("Asabeneh", "250", "Finland", "Helsinki"))

#Use the string formatting method to display the following:
#radius = 10
#area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.
import math
r = 30
area = math.pi * r ** 2
print("The area for a circle with the radius of %d is %.2f" %(r,area))

#Make the following using string formatting methods:
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144
x = 8
y = 6
print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} / {y} = {x/y:.2f}")
print(f"{x} % {y} = {x%y}")
print(f"{x} // {y} = {x//y}")
print(f"{8} ** {6} = {8**6}")
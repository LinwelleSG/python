"""count = 5
while count <= 25:
    if count == 14:
        count = count + 1
        continue
    print(count)
    count = count + 3

numbers = [2,4,67,8,45,64,990]
for num in numbers:
    print(num)

language = 'Python'
for letter in language:
    print(letter)
for i in range(len(language)):
    print(language[i])

numbers = (0,10,2,2303,998)
for num in numbers:
    print(num) 
    
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)  

for key , value in person.items():
    print(f"{key}: {value}") 
    
numbers = (0,1,2,3,4,5)
for num in numbers:
    print(num)
    if num == 3:
        continue
if num != 5:
    print(f"Next number should be {num + 1}")
else:
    print("loop's end")
print("outside the loop")  

st = set(range(12))
print(st)
lst = list(range(0,22,3))
print(lst)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
    if key == "skills":
        for skill in person['skills']:
            print(skill)

for num in range(11):
    print(num)
else:
    print(f"The number stops at {num}")    

for number in range(6):
    pass 
#💻 Exercises: Day 10
#Exercises: Level 1
#Iterate 0 to 10 using for loop, do the same using while loop.
for n in range(11):
    print(n)

num = 0
while num <= 10:
    print(num)
    num = num + 1  

#Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10,-1,-1):
    print(i)

num = 10
while num  != -1:
    print(num)
    num = num - 1
#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#
##
###
####
#####
######
#######
for i in range(1,8):
    print("#" * i) 

#Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for i in range(8):
    for j in range (8):
        print("#", end=" ")
    print()

#Print the following pattern:
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100
for i in range(11):
    print(f"{i} X {i} = {i * i}") """

#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in lst:
    print(item)

#Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(2,101,2):
    print(i)
 #Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(1,100,2):
    print(i)

 


    
    

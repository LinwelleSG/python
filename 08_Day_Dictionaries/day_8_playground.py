empty_dictionary = {}
print(empty_dictionary)
print(type(empty_dictionary))
print(len(empty_dictionary))

name = {
    "first_name" : "Lin", "last_name" : "SG" , "age" : 22,
    "is_married" : True , "address" : { "street" : "ph 2 blk 3 lot 11", "zip_code" : 2209},
    "skills" : ["Programming" , "Web Development", "Python"]
    }

print(len(name))
print(name["first_name"])
print(f"{name['first_name']}'s zip code is {name['address']['zip_code']}")
print(name.get('last_name'))
print(name.get('city'))

name["skills"][1] = "DevOps"
name["skills"].append("Web Development")
print(name["skills"])

print("city" in name)
print("zip_code" in name)
print("address" in name)

print(name.items())

name_copy = name.copy()
print(name_copy)

print(name.keys())
print(name.values())

#Exercises: Day 8

#Create an empty dictionary called dog
dog = {}

#Add name, color, breed, legs, age to the dog dictionary
dog = {"name" : "mac" , "color" : "brown" , "breed" : "aspin" , "legs" : 4 , "age" : 2}
print(dog)
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {"first_name" : "Yel" , "last_name" : "San Gabriel" , "gender" : "f" ,
           "age" : 23 , "is_married" : True , "skills" : ["nursing" , "first aid" ,
            "medicine"] , "country" : "USA" , "city" : "Olongapo" ,
           "address" : {"barangay" : "banicain" , "street" : "luna" , "zip_code" : 2200}}
#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
print(type(student["skills"]))

#Modify the skills values by adding one or two skills
student["skills"].append("caring")
print(student)

#Get the dictionary keys as a list
keys = student.keys
print(keys)
#Get the dictionary values as a list
values = student.values
print(values) 

#Change the dictionary to a list of tuples using items() method
print(student.items())

#Delete one of the items in the dictionary
print(student.popitem())
#Delete one of the dictionaries
del student["first_name"]
print(student)
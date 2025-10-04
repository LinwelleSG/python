"""def min_max(nums):
    return (min(nums) , max(nums))

lowest,highest = min_max([2,3,4,5,6,7,8])

print(lowest,highest)

fruits = ("apple","orange","banana","grapes")
last_index =len(fruits) - 1
last_fruit = fruits[last_index]
print(last_index)
print(last_fruit)
orange_banana = fruits[1:3]
print(orange_banana)
print(fruits[-1::-1])
"""
#💻 Exercises: Day 6
#Exercises: Level 1

#Create an empty tuple
tpl = ()
print(tpl)
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine
sisters = ("Tan","Jan","Krizia","Yel")
brothers = ("Joseph","Reginald","Diether","Dan")
#Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)
#How many siblings do you have?
print(f"I have {len(siblings)} siblings")
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ("Ruel","Norie")
family_members = siblings + parents
print(family_members)

#Exercises: Level 2
#Unpack siblings and parents from family_members
*siblings,father,mother = family_members
print(f"Siblings: {siblings}")
print(f"Father: {father}")
print(f"Mother: {mother}")
#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "mango", "banana","orange",)
vegetables =("celery","kangkong","spinach","squash","lettuce")
animal_products = ("milk","cheese","butter")
food_stuff_tp = fruits + vegetables + animal_products
#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
n = len(food_stuff_lt)
if n % 2 == 0:
    left_mid = n // 2 - 1
    right_mid = n // 2
    mid_item = food_stuff_lt[left_mid],food_stuff_lt[right_mid]
else:
    mid = n // 2
    mid_item = food_stuff_lt[mid]
print(len(food_stuff_lt))
print(food_stuff_lt)
print(mid_item)
#Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[3 :-3])
#Delete the food_staff_tp tuple completely
del food_stuff_tp

#Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#Check if 'Estonia' is a nordic country
if "Estonia" in nordic_countries:
    print("Estonia is a nordic country")
else:
    print("Estodia is not a nordic country")
#Check if 'Iceland' is a nordic country
if "Iceland" in nordic_countries:
    print("Iceland is a nordic country")
else:
    print("Iceland is not a nordic country")


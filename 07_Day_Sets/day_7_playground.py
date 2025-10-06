
"""st = set()
print(st)
print(type(st))

names = {"Lin", "Yel", "Dan"}
names.add("Lee")
print(names)

last_names = ["SG","SJ","MAC"]

names.update(last_names)
print(names)

removed_item = names.pop()
print(f"The removed name from the names set is: {removed_item}")
print(names)
names.clear()
print(names)

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1))
print(st1.difference(st2)) # {'item1', 'item4'} => st1\st2

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.difference(dragon))     
print(dragon.difference(python))
print(python.symmetric_difference(dragon))     
print(dragon.symmetric_difference(python))
"""


#💻 Exercises: Day 6
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercises: Level 1
#Find the length of the set it_companies
print(len(it_companies))
#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
#Insert multiple IT companies at once to the set it_companies
more_companies = "Shopee","Gcash","YouTube"
it_companies.update(more_companies)
print(it_companies)
#Remove one of the companies from the set it_companies
print(it_companies.pop())
#What is the difference between remove and discard
it_companies.discard("Safari")
#- remove() returns an error if the item that you want to remove is not in the list. discard() does not.

#Exercises: Level 2
#Join A and B
AB = A.union(B)
print(AB)
#Find A intersection B
print(A.intersection(B))
#Is A subset of B
print(A.issubset(B))
#Are A and B disjoint sets
print(A.isdisjoint(B))
#Join A with B and B with A
A.update(B)
B.update(A)
print(A)
print(B)
#What is the symmetric difference between A and B
print(A.symmetric_difference(B))
#Delete the sets completely
del A
del B

#Exercises: Level 3
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(len(age)) # --> 8
age = set(age)
print(type(age))
print(len(age)) # --> 5
#the bigger one is list because when it gets converted to set, the duplicates get discarded.

#Explain the difference between the following data types: string, list, tuple and set
#the string stores characters. the list is set of indexed and ordered objects,
#same as tuple but the tuple is immutable, which means its elements cannot be changed.
#and set is mutable but unordered collection of items.

#How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
sentence = sentence.split()
print(sentence)
unique_words = set(sentence)
print(f"The total number of unique words is {len(unique_words)}: {unique_words}")



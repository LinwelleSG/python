"""fruits = ['banana', 'orange', 'mango', 'lemon']                  # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print("Fruits:", fruits)

lst = "Lin" , 22 , False, {"country" : "philippines" , "city" : "olongapo"}
print(lst[-3])

lst = ['item1','item2','item3', 'item4', 'item5']
a, second_item, *rest, fifth = lst
print(a)     # item1
print(fifth) 

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']

countries[0] ="Philippines"
last_index = len(countries) -1
countries[last_index] = "Loonieverse"
countries.insert(4, 90)
countries.remove(90)
countries.remove('Belgium')
countries.pop(2)
del countries[0:5]
countries.clear()
print(countries)
print("Loonieverse" in countries)
countries_copy = countries
print(countries_copy)
countries_copycat = countries.copy()
print(countries_copycat)
positive_numbers = [1,2,3,4,5]
negative_numbers = [-1,-2,-3,-4,-5]
zero = [0]
positive_numbers.extend(negative_numbers)
positive_numbers.extend(zero)
positive_numbers.sort(reverse = True)
print(sorted(positive_numbers, reverse = True))

#EXERCISES
#DAY 5 - LISTS
#Declare an empty list
places = []
print(places)
#Declare a list with more than 5 items
items = ["a","b","c","d","e","f"]
#Find the length of your list
print(len(items))
#Get the first item, the middle item and the last item of the list
mid_item = int((len(items) / 2))
print(items[0], items[mid_item], items[-1])
#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Lin",22, 175, "Single", "Olongwapo"]

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
#Print the list using print()
print(it_companies)
#Print the number of companies in the list
print(len(it_companies))
#Print the first, middle and last company
middle_company = int((len(it_companies)) / 2)
print(it_companies[0], it_companies[middle_company], it_companies[-1])
#Print the list after modifying one of the companies
it_companies[0] = "YouTube"
#Add an IT company to it_companies
it_companies.append("Gmail")

#Insert an IT company in the middle of the companies list
it_companies.insert(middle_company,"Twitter")


#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper()


#Join the it_companies with a string '#;  '
#it_companies = '#;  '.join(it_companies) + "#;"


#Check if a certain company exists in the it_companies list.
print("TWITTER" in it_companies)

#Sort the list using sort() method
it_companies.sort()


#Reverse the list in descending order using reverse() method
it_companies.reverse()


#Slice out the first 3 companies from the list
print(it_companies[3:])
#Slice out the last 3 companies from the list
print(it_companies[:-3])
#Slice out the middle IT company or companies from the list
n = len(it_companies)
if n % 2 == 0:
    mid_index = n // 2
    sliced = it_companies[:mid_index] + it_companies[mid_index + 1:]

else:
    mid_index1 = (n // 2) - 1
    mid_index2 = (n // 2) + 1
    sliced = it_companies[:mid_index1] + it_companies[mid_index2:]

print(it_companies)
print(sliced)

#Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)  

it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon", "test"]

#Remove the middle IT company or companies from the list
n = len(it_companies)

if n % 2 == 0:
    mid_index1 = n // 2 - 1
    mid_index2 = n // 2
    pop1 = it_companies[mid_index2]
    pop2 = it_companies[mid_index1]
    popped = [pop1,pop2]
else:
    mid_index = n // 2
    popped = [it_companies.pop(mid_index)]
    
print("Popped: ", popped)
print("Remaining: ", it_companies)

#Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

#Remove all IT companies from the list
it_companies = []
print(it_companies)

#Destroy the IT companies list
del it_companies

#Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
index = full_stack.index("Redux")
full_stack.insert(index + 1,"Python")
full_stack.insert(index + 2,"SQL")
print(full_stack) 

#Exercises: Level 2
#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
ages.sort()
print(f"The oldest person is {ages[-1]} years old")
print(f"The youngest person is {ages[0]} years old")
#Add the min age and the max age again to the list
ages.append(ages[-1])
ages.append(ages[0])
ages.sort()
print(ages)
#Find the median age (one middle item or two middle items divided by two)
n = len(ages)
if n % 2 == 0:
    mid1 = n // 2 - 1
    mid2 = n // 2 
    median = (ages[mid1] + ages[mid2]) / 2
else:
    mid = n // 2
    median = mid
    
print(f"The median age of the ages set is {median}")
      
#Find the average age (sum of all items divided by their number )
sum = sum(ages)
ave = sum / n
print(f"The average of the ages set is {ave}")
#Find the range of the ages (max minus min)
range = ages[-1] - ages[0]
print(f"The range of the afes set is {range}")
#Compare the value of (min - average) and (max - average), use abs() method
min = min(ages)
max = max(ages)

min_ave = abs(min - ave)
max_ave = abs(max - ave)

print(f"The absolute value of min - average is {min_ave}")
print(f"The absolute value of max - average is {max_ave}") """

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

#Find the middle country(ies)
n = len(countries)

if n % 2 == 0:
    index1 = n // 2 - 1
    index2 =  n // 2 
    middle_country = countries[index1:index2+1]
else:
    index = n // 2
    middle_country = countries[index]

print(f"The middle country(ies) is/are: {middle_country}")

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
if n % 2 == 0:
    half = n // 2
    first_half = countries[:half]
    second_half = countries[half:]
else:
    half = n // 2 + 1
    first_half = countries[:half]
    second_half = countries[half:]
    
print(f"First Half: {first_half}")
print(f"Second Half: {second_half}")

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
cs = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
c1, c2, c3, *rest = cs
print(f"Unpacked: {c1,c2,c3}")
print(f"Scandic Countries: {rest}")

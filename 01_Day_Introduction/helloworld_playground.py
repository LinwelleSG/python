#TASK 1
#Write a program that asks the user for a number and tells whether it’s even or odd.
try:
    x = int(input("Enter a number do determine whether it's an odd or an even number: "))
    if x % 2 == 0:
        print (f"{x} is an even number")
    else:
            print (f"{x} is an odd number")
            
except ValueError:
    print("Invalid Input")

#TASK 2
#Imagine you have 317 candies, and you want to put them into bags with 2 candies in each bag.
#Use floor division (//) to find how many full bags you can make.
#Use modulus (%) to find how many candies are left over.

#Example Output:
#You can make 158 full bags.
#There will be 1 candy left over.

candies = 317
full_bags = candies // 2
left_over = candies % 2

print(f"You can make {full_bags} full bags.")
print(f"There will be {left_over} candy left over")

#with input version
candies = int(input("Enter the number of candies you have: "))
full_bags = candies // 2
left_over = candies % 2

print(f"You can make {full_bags} full bags with {candies} candies.")
print(f"There will be {left_over} candy left over with {full_bags} full bags.")

    
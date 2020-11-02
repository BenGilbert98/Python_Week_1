# What is concatenation?
#
# first_name = "James"
# middle_name = "Bond"
# last_name = "777"
# age = str(18)
#
# full_name = first_name + " " + middle_name + " " + last_name
# print(full_name)



# Casting is used to change data types of variables

# full_name_cast = first_name + " " + middle_name + " " + last_name + " " + age # this will give a TypeError as you are adding an int to a sting
# # to fix this error we use str( ) to convert age into a string
#
# last_name_2 = int("777")
# print(last_name_2, type(last_name_2))

name = input("Please enter your name    ")
age = input("Please enter your age    ")
house_number = input("What is your house number?    ")
address = input("What is the 1st line of your address?    ")
post_code = input("What is your post code?    ")


print("Hello", name + "!", "you are", age, "years old", "and you live at", house_number, address + ",", post_code)
# What is a Dictionary?
# a dictionary (array) is another way of managing data but more dynamically
# key value pairs to store and manage data
# Syntax : {"name": "james"}


# What type of data can we store / manage?
# any data types can be stored / managed


# Lets create a dictionary
#
devops_students_data = {
    "key" : "value",
    "name" : "Ben",
    "stream" : "tech",
    "completed_lessons" : 4,
    "completed_lesson_names" : ["operators", "data types", "variables"],
    "hobbies" : ["watching movies", "data types", "variables"]
 }
devops_students_data ["hobbies"].append("running")
print (devops_students_data)
devops_students_data ["hobbies"].remove("data types")
print (devops_students_data)
# print(devops_students_data.values())

# print(devops_students_data)
# print(type(devops_students_data))

# print(devops_students_data["name"]) # displays data inside specific key
# print(devops_students_data["completed_lessons"])

# print(devops_students_data.keys()) # displays keys within dictionary
# print(devops_students_data["completed_lesson_names"])

# # How can we fetch the value called "data types"
# print(devops_students_data["completed_lesson_names"][1]) # fetches the 1st index within the key "completed_lesson_names"

# # How can I change the value of specific key
# devops_students_data["completed_lessons"] = 3
# print(devops_students_data["completed_lessons"])
# print(devops_students_data.items()) # prints the keys and their pairs
# print(type(devops_students_data.items()))


# Task
# create a new dictionary to store user details
# all the details that you utilised in the last task (name, DOB, Address, course, grades, hobbies)
# methods of dictionary to remove, add, replace, display the type of items
# create a list of hobbies
# display data in reverse order of hobby list

# user_details = {
#     "name" : "Ben",
#     "DoB" : "04-03-1998",
#     "Address" : "123 avenue road",
#     "course" : "DevOps",
#     "Grades" : "A",
#     "Hobbies" : ["Cycling", "Painting", "Reading", "Sleeping"]
# }
#
# print(user_details.values()) # Prints the values in the list
#
# devops_students_data ["Hobbies"].remove("Cycling") # removes Cycling from hobbies
# print (devops_students_data)
#
# user_details["Pets"] = "Dog" # Adds "Pets" to the list with value "Dog"
# print(user_details)
#
# user_details["Hobbies"][2] = "Speed Reading" # Changes the 2nd index in Hobbies to "Speed Reading"
# print(user_details.values())
#
# print(type(user_details["Hobbies"]))
#
# print(user_details ["Hobbies"][::-1]) # prints the list Hobbies in reverse



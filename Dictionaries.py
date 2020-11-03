# What is a Dictionary?
# a dictionary (array) is another way of managing data but more dynamically
# key value pairs to store and manage data
# Syntax : {"name": "james"}


# What type of data can we store / manage?
# any data types can be stored / managed


# Lets create a dictionary

devops_students_data = {
    "key" : "value",
    "name" : "Ben",
    "stream" : "tech",
    "completed_lessons" : 4,
    "completed_lesson_names" : ["operators", "data types", "variables"]
}

# print(devops_students_data)
# print(type(devops_students_data))

# print(devops_students_data["name"]) # displays data inside specific key
# print(devops_students_data["completed_lessons"])

# print(devops_students_data.keys()) # displays keys within dictionary
print(devops_students_data["completed_lesson_names"])

# How can we fetch the value called "data types"
print(devops_students_data["completed_lesson_names"][1]) # fetches the 1st index within the key "completed_lesson_names"

# Collection in python
# Lists?
# A List is a collection which is ordered and changeable. Allows duplicate members.
# indexing starts on 0
# Syntax: ["Yoghurt, "Apple", "Milk"]


# Lets create a list

# shopping_list = ["Apple", "Milk", "Bread"]
# print(shopping_list)
# # print(type(shopping_list))
# #
# # # look at indexing in the list items
# #
# # print(shopping_list[1]) # prints "Milk"
# # print(shopping_list[2]) # prints "Bread"
# # print(shopping_list[1:3]) # prints "Milk", "Bread"
#
# # add an item to this list
# shopping_list.append("Eggs") # append method adds an item at the end of the list
# print(shopping_list)
#
# # remove an item from the list
# shopping_list.remove("Apple") # remove method removes an item from the list
# print(shopping_list)
#
# # remove last item from our list that we added earlier
# shopping_list.pop()
# print(shopping_list)
#
# # how can i replace an item within my list
# shopping_list[1] = "Baguette" # replaces the value at index 1 with "Baguette"
# print(shopping_list)

# can we have mixed data types within a list

#
# shopping_list = [1, 2, 3, "Apple", "Milk", "Bread"]
# print(shopping_list)

# Task: create a mixed data type list of 7 items
# display the type of the data
# add, delete, replace, pop
# use indexing to print the list in reverse order
# 10 minutes to complete and share your github link at 11:52

mixed_data_list = [1.3, 2, "Apple", "Bike", 4.6, "Pencil", 4]
print(len(mixed_data_list)) # finds the length of the list
for i in mixed_data_list:  # for loop to print the data type of each item in the list
    print(type(i))
mixed_data_list.append("Phone") # adds "Phone" to the end of the list
mixed_data_list.remove(1.3) # removes the list item 1.3
mixed_data_list[2] = "Mountain Bike" # replaces "Bike" with "Mountain Bike"
mixed_data_list.pop() # removes last value within the list
print(mixed_data_list) # prints the list
print(mixed_data_list[::-1]) # prints list in reverse
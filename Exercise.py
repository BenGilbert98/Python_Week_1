name = input("What is your name?     ")
dob = input("What is your date of birth?    (dd-mm-yyyy)     ")

try:
    age = int(input("How old are you?    "))
    if age <= 0:
        raise ValueError("Your age cannot be 0 or below")
except ValueError as err:
    print("Please enter a valid age, {}".format(err))
else:
    print (name, ", ", dob, ", ", age)
    print(type(name), ", ", type(dob), ", ", type(age))

my_dict = {"red": "apple",# key value pair
           "yellow": "banana",
           "purple": "grapes"}

print(my_dict["purple"])

my_dict["print"] = "dragonfruit"

print(my_dict) # adding a new key value pair

del my_dict["red"] # deleting a key value pair
print(my_dict)

#understanding dictionary
countryDB = {}

while True:
    print ("1, Insert a new country")# key value pair
    print ("2, Display all countries..") # .keys() method is used to display all the keys in the dictionary
    print ("3, Display all capitals...") #  .values() method is used to display all the values in the dictionary
    print ("4, Get capital of a country") # .get() method is used to get the value of a key in the dictionary. It takes the key as an argument and returns the value of that key. If the key is not found, it returns None. You can also specify a default value to return if the key is not found by passing it as the second argument to the get() method.
    print ("5, Delete")

    choice = int(input("Enter your choice(1-5): "))

    if choice == 1:
        country = input("Enter the name of the country: ").upper()#.upper() converts the input to uppercase letters
        capital = input("Enter the name of the capital: ").upper()
        countryDB[country] = capital

    elif choice == 2:
        print(list(countryDB.keys()))

    elif choice == 3:
        print(list(countryDB.values()))

    elif choice == 4:
        country = input("Enter the name of the country: ").upper()
        prinnt(countryDB.get(country))

    elif choice == 5:
        country = input("Enter the name of the country: ").upper()
        del countryDB[country]

    else:
        break